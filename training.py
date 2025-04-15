import streamlit as st
import json
import os
import logging

# Import chapter modules and final quizzes from chapter1, chapter2, and chapter3
from chapter1 import CH1_MODULES, CH1_FINAL_QUIZ
from chapter2 import CH2_MODULES, CH2_FINAL_QUIZ
from chapter3 import CH3_MODULES, CH3_FINAL_QUIZ
# Chapter4 has been deleted, so we no longer import it.

# Set up logging for debugging
logging.basicConfig(
    level=logging.INFO,
    filename="training.log",
    filemode="a",
    format="%(asctime)s - %(levelname)s - %(message)s"
)

################################################################
#                     USER CREDENTIALS                         #
################################################################
USERS = {
    "Damon123": {"password": "pass123", "role": "trainee"},
    "jake123":  {"password": "pass123", "role": "trainee"},
    "Admin":    {"password": "admin123", "role": "admin"}
}

################################################################
#            FALLBACK FUNCTION FOR RE-RUN BEHAVIOR             #
################################################################
def rerun_app():
    """
    Try to call st.experimental_rerun(). If unavailable, warn the user.
    """
    if hasattr(st, "experimental_rerun"):
        st.experimental_rerun()
    else:
        st.warning("st.experimental_rerun() is not available. Please manually select the next module in the sidebar.")

################################################################
#         UNIVERSAL show_chapter() FUNCTION                    #
################################################################
def show_chapter(chapter_name: str, modules, final_quiz):
    """
    Unified function to present module content (and tasks) for a chapter.
    Uses only session_state to save the current module index.
    
    chapter_name: "Chapter 1", "Chapter 2", or "Chapter 3"
    modules: list of dicts (with keys: title, content, task_type, task, etc.)
    final_quiz: list of quiz questions for the chapter
    """
    # Build list of module titles plus a "Final Quiz" option
    module_titles = [mod["title"] for mod in modules] + ["Final Quiz"]

    # Initialize the current module index in session_state if not set
    if f"{chapter_name}_module_index" not in st.session_state:
        st.session_state[f"{chapter_name}_module_index"] = 0

    # Show a selectbox for modules, with default coming from session_state if present
    chapter_keys = list(chapter_options.keys())
    if "selected_chapter" in st.session_state and st.session_state["selected_chapter"] in chapter_keys:
        default_index = chapter_keys.index(st.session_state["selected_chapter"])
        # We don't preselect the module here; that's handled in the next line.
    selected_module = st.sidebar.selectbox(
        f"Select {chapter_name} Module",
        module_titles,
        index=st.session_state.get(f"{chapter_name}_module_index", 0)
    )

    # ---------- If user chose "Final Quiz" ----------
    if selected_module == "Final Quiz":
        st.markdown(f"# {chapter_name} Final Quiz")

        quiz_score = 0
        user_answers = {}
        total_questions = len(final_quiz)

        # Display final quiz questions
        for i, q in enumerate(final_quiz):
            st.markdown(f"**Question {i+1}:** {q['question']}")
            user_answers[i] = st.radio("Select an option:", q["options"], key=f"{chapter_name}_final_q_{i}")

        if st.button("Submit Final Quiz"):
            # Grade the final quiz
            for i, q in enumerate(final_quiz):
                correct_index = q["answer"]
                correct_answer = q["options"][correct_index]
                if user_answers.get(i) == correct_answer:
                    quiz_score += 1

            st.info(f"You scored {quiz_score} out of {total_questions}!")

            # Pass if user got 4 or more correct out of 5
            if quiz_score >= 4:
                st.success(f"Great job! You have completed {chapter_name}.")
                st.info("Please click top left for the next chapter.")
            else:
                st.error("You did not reach the passing score (4/5). Please review the modules and try again.")
        return

    # ---------- Otherwise, user selected a normal module ----------
    module_index = module_titles.index(selected_module)
    mod = modules[module_index]

    # Display module title and content
    st.markdown(f"# {mod['title']}")
    st.markdown(mod["content"])

    # If there's a 'task', display it
    if "task" in mod and mod["task"]:
        st.markdown(mod["task"])

    # Check the task type
    task_type = mod.get("task_type", "")

    # ---------- Reflection Tasks ----------
    if task_type == "reflection":
        response = st.text_area("Your Reflection:")
        if st.button("Submit Reflection"):
            st.success("Reflection submitted!")
            # Move to next module automatically
            next_module_index = module_index + 1
            if next_module_index < len(module_titles):
                st.session_state[f"{chapter_name}_module_index"] = next_module_index
                rerun_app()

    # ---------- Scenario Tasks (single correct answer) ----------
    elif task_type == "scenario":
        options = mod.get("options", [])
        answer = st.radio("Select the correct answer:", options, key=f"{chapter_name}_scenario_{module_index}")
        if st.button("Submit Scenario Answer"):
            if "correct_answer" in mod and mod["correct_answer"] < len(options):
                if options[mod["correct_answer"]] == answer:
                    st.success("Correct answer!")
                    # Advance to next module
                    next_module_index = module_index + 1
                    if next_module_index < len(module_titles):
                        st.session_state[f"{chapter_name}_module_index"] = next_module_index
                        rerun_app()
                else:
                    st.error("Incorrect answer. Please review the module and try again.")

    # ---------- Mini-Quiz Tasks (multiple questions) ----------
    elif task_type == "miniquiz":
        if "miniquiz_questions" in mod:
            user_answers = {}
            score = 0
            quiz_qs = mod["miniquiz_questions"]
            total = len(quiz_qs)

            for i, q in enumerate(quiz_qs):
                st.markdown(f"**Question {i+1}:** {q['question']}")
                user_answers[i] = st.radio("Select an option:", q["options"], key=f"{chapter_name}_miniquiz_{module_index}_{i}")

            if st.button("Submit Mini Quiz"):
                for i, q in enumerate(quiz_qs):
                    correct_index = q["correct_answer"]
                    correct_answer = q["options"][correct_index]
                    if user_answers.get(i) == correct_answer:
                        score += 1

                st.info(f"You scored {score} out of {total}!")

                # If all answers correct, auto-advance
                if score == total:
                    st.success("Great job! Moving to the next module.")
                    next_module_index = module_index + 1
                    if next_module_index < len(module_titles):
                        st.session_state[f"{chapter_name}_module_index"] = next_module_index
                        rerun_app()
                else:
                    st.error("Not all answers are correct. Please review and try again.")
        else:
            st.warning("No miniquiz questions found for this module.")

    else:
        st.info("No task available for this module.")

################################################################
#                     MAIN APP LOGIC                           #
################################################################
def main():
    st.title("CC Inc. Training App")

    # Initialize user login in session_state
    if "user" not in st.session_state:
        st.session_state.user = ""
    if "role" not in st.session_state:
        st.session_state.role = ""

    # ----- Search Bar in the Sidebar -----
    search_query = st.sidebar.text_input("Search Training Content", "")
    if search_query:
        st.sidebar.markdown("### Search Results")
        # Search only among available chapters (1-3)
        search_chapters = {
            "Chapter 1": CH1_MODULES,
            "Chapter 2": CH2_MODULES,
            "Chapter 3": CH3_MODULES
        }
        search_results = []
        for chap_name, modules in search_chapters.items():
            for idx, mod in enumerate(modules):
                # Search in both title and content
                if (search_query.lower() in mod["title"].lower()) or (search_query.lower() in mod["content"].lower()):
                    search_results.append((chap_name, idx, mod["title"]))
        if search_results:
            for result in search_results:
                chap, idx, title = result
                if st.sidebar.button(f"{chap} - {title}", key=f"search_{chap}_{idx}"):
                    st.session_state["selected_chapter"] = chap
                    st.session_state[f"{chap}_module_index"] = idx
                    st.experimental_rerun()
        else:
            st.sidebar.write("No results found.")

    # If not logged in, show login
    if not st.session_state.user:
        st.sidebar.header("Login")
        username = st.sidebar.text_input("Username:")
        password = st.sidebar.text_input("Password:", type="password")
        if st.sidebar.button("Login"):
            if username in USERS and USERS[username]["password"] == password:
                st.session_state.user = username
                st.session_state.role = USERS[username]["role"]
                st.success(f"Welcome, {username}!")
            else:
                st.error("Incorrect username or password.")
        return

    # Let user pick a chapter (only Chapters 1-3 available)
    chapter_options = {
        "Chapter 1": {"modules": CH1_MODULES, "quiz": CH1_FINAL_QUIZ},
        "Chapter 2": {"modules": CH2_MODULES, "quiz": CH2_FINAL_QUIZ},
        "Chapter 3": {"modules": CH3_MODULES, "quiz": CH3_FINAL_QUIZ}
    }
    
    # Preselect chapter if one was chosen from search
    chapter_keys = list(chapter_options.keys())
    if "selected_chapter" in st.session_state and st.session_state["selected_chapter"] in chapter_keys:
        default_index = chapter_keys.index(st.session_state["selected_chapter"])
        chapter = st.sidebar.selectbox("Select Chapter", chapter_keys, index=default_index)
    else:
        chapter = st.sidebar.selectbox("Select Chapter", chapter_keys)

    if chapter in chapter_options:
        show_chapter(
            chapter_name=chapter,
            modules=chapter_options[chapter]["modules"],
            final_quiz=chapter_options[chapter]["quiz"]
        )
    else:
        st.warning("Please select a chapter to begin.")

if __name__ == "__main__":
    main()
