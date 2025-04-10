import streamlit as st
import json
import os
import logging

# Import chapter modules and final quizzes from chapter1.py and chapter2.py
from chapter1 import CH1_MODULES, CH1_FINAL_QUIZ
from chapter2 import CH2_MODULES, CH2_FINAL_QUIZ

# Set up logging for debugging
logging.basicConfig(level=logging.INFO, filename="training.log", filemode="a",
                    format="%(asctime)s - %(levelname)s - %(message)s")

################################################################
#              REMOVED PROGRESS FILE FUNCTIONS                 #
# (We no longer use file-based progress; session_state only)   #
################################################################
# def load_progress(file_path):
#     try:
#         if os.path.exists(file_path):
#             with open(file_path, "r") as f:
#                 data = json.load(f)
#                 logging.info(f"Progress loaded successfully from {file_path}.")
#                 return data
#         logging.info(f"No progress file found at {file_path}. Initializing new progress.")
#         return {}
#     except (json.JSONDecodeError, IOError) as e:
#         logging.error(f"Error loading progress from {file_path}: {e}")
#         return {}
#
# def save_progress(data, file_path):
#     try:
#         with open(file_path, "w") as f:
#             json.dump(data, f)
#         logging.info(f"Progress saved successfully to {file_path}.")
#     except IOError as e:
#         logging.error(f"Error saving progress to {file_path}: {e}")
#         st.error("Error saving progress. Progress may not be saved.")

################################################################
#                 USER CREDENTIALS (SAME FOR BOTH)             #
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
#          UNIVERSAL show_chapter() FUNCTION                   #
################################################################
def show_chapter(chapter_name: str, modules, final_quiz):
    """
    Unified function to present module content (and tasks) for a chapter.
    Uses only session_state to save the current module index.
    
    chapter_name: "Chapter 1" or "Chapter 2"
    modules: list of dicts (with keys: title, content, task_type, task, etc.)
    final_quiz: list of quiz questions for the chapter
    """
    # Build list of module titles plus a "Final Quiz" option.
    module_titles = [mod["title"] for mod in modules] + ["Final Quiz"]

    # Initialize the current module index in session_state if not already set.
    if f"{chapter_name}_module_index" not in st.session_state:
        st.session_state[f"{chapter_name}_module_index"] = 0

    selected_module = st.sidebar.selectbox(
        f"Select {chapter_name} Module",
        module_titles,
        index=st.session_state[f"{chapter_name}_module_index"]
    )

    # --- Final Quiz Handling ---
    if selected_module == "Final Quiz":
        st.markdown(f"# {chapter_name} Final Quiz")
        quiz_score = 0
        user_answers = {}
        for i, q in enumerate(final_quiz):
            st.markdown(f"**Question {i+1}:** {q['question']}")
            user_answers[i] = st.radio("Select an option:", q["options"], key=f"final_q_{i}")
        if st.button("Submit Final Quiz"):
            for i, q in enumerate(final_quiz):
                correct_index = q["answer"]
                correct_answer = q["options"][correct_index]
                if user_answers.get(i) == correct_answer:
                    quiz_score += 1
            st.success(f"You scored {quiz_score} out of {len(final_quiz)}!")
        return  # End final quiz processing

    # --- Regular Module Handling ---
    # Get the current module based on the selected title.
    module_index = module_titles.index(selected_module)
    mod = modules[module_index]
    
    # Always display the module "content".
    st.markdown(f"# {mod['title']}")
    st.markdown(mod["content"])

    # If there's a 'task' field (the question/prompt), display it.
    if "task" in mod and mod["task"]:
        st.markdown(mod["task"])

    task_type = mod.get("task_type", "")

    # --- Reflection Task (no right/wrong) ---
    if task_type == "reflection":
        response = st.text_area("Your Reflection:")
        if st.button("Submit Reflection"):
            st.success("Reflection submitted!")
            # Automatically navigate to next module.
            next_module_index = module_index + 1
            if next_module_index < len(module_titles) - 1:  # Do not skip Final Quiz
                st.session_state[f"{chapter_name}_module_index"] = next_module_index
                rerun_app()

    # --- Scenario Task (single correct answer) ---
    elif task_type == "scenario":
        options = mod.get("options", [])
        answer = st.radio("Select the correct answer:", options, key=f"scenario_{module_index}")
        if st.button("Submit Scenario Answer"):
            if "correct_answer" in mod and mod["correct_answer"] < len(options):
                if options[mod["correct_answer"]] == answer:
                    st.success("Correct answer!")
                    # Auto-navigate only if the answer is correct.
                    next_module_index = module_index + 1
                    if next_module_index < len(module_titles) - 1:
                        st.session_state[f"{chapter_name}_module_index"] = next_module_index
                        rerun_app()
                else:
                    st.error("Incorrect answer. Please review the module content and try again.")

    # --- Miniquiz Task (multiple questions) ---
    elif task_type == "miniquiz":
        if "miniquiz_questions" in mod:
            user_answers = {}
            score = 0
            total_questions = len(mod["miniquiz_questions"])
            for i, q in enumerate(mod["miniquiz_questions"]):
                st.markdown(f"**Question {i+1}:** {q['question']}")
                user_answers[i] = st.radio("Select an option:", q["options"], key=f"miniquiz_{module_index}_{i}")
            if st.button("Submit Mini Quiz"):
                for i, q in enumerate(mod["miniquiz_questions"]):
                    correct_index = q["correct_answer"]
                    correct_answer = q["options"][correct_index]
                    if user_answers.get(i) == correct_answer:
                        score += 1
                st.success(f"You scored {score} out of {total_questions}!")
                # Auto-navigate if the mini quiz is answered perfectly.
                if score == total_questions:
                    st.info("Great job! Moving to the next module.")
                    next_module_index = module_index + 1
                    if next_module_index < len(module_titles) - 1:
                        st.session_state[f"{chapter_name}_module_index"] = next_module_index
                        rerun_app()
                else:
                    st.error("Not all answers are correct. Please review your answers and try again.")

    else:
        st.info("No task available for this module.")

################################################################
#                     MAIN APP LOGIC                           #
################################################################
def main():
    st.title("CC Inc. Training App")
    
    # Initialize session_state for user and role if not present.
    if "user" not in st.session_state:
        st.session_state.user = ""
    if "role" not in st.session_state:
        st.session_state.role = ""
    
    # Display a simple login form if the user is not logged in.
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
        return  # Do not proceed until login is successful.

    # Allow the user to choose a chapter.
    chapter = st.sidebar.selectbox("Select Chapter", ["Chapter 1", "Chapter 2"])
    
    if chapter == "Chapter 1":
        try:
            show_chapter("Chapter 1", CH1_MODULES, CH1_FINAL_QUIZ)
        except Exception as e:
            st.error(f"Error displaying Chapter 1: {e}")
    elif chapter == "Chapter 2":
        try:
            show_chapter("Chapter 2", CH2_MODULES, CH2_FINAL_QUIZ)
        except Exception as e:
            st.error(f"Error displaying Chapter 2: {e}")

if __name__ == "__main__":
    main()
