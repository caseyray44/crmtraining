import streamlit as st
import json
import os
import logging
from datetime import datetime

# Import chapter modules and quizzes for Chapters 1-4
from chapter1 import CH1_MODULES, CH1_FINAL_QUIZ
from chapter2 import CH2_MODULES, CH2_FINAL_QUIZ
from chapter3 import CH3_MODULES, CH3_FINAL_QUIZ
from chapter4 import CH4_MODULES, CH4_FINAL_QUIZ

# Set up logging for debugging
logging.basicConfig(level=logging.INFO, filename="training.log", filemode="a",
                    format="%(asctime)s - %(levelname)s - %(message)s")

################################################################
#                     USER CREDENTIALS                         #
################################################################
USERS = {
    "Damon123": {"password": "pass123", "role": "trainee"},
    "jake123":  {"password": "pass123", "role": "trainee"},
    "Admin":    {"password": "admin123", "role": "admin"}
}

################################################################
#            PROGRESS AND ANSWER FILE MANAGEMENT               #
################################################################
def load_user_progress(username):
    """Load user's progress from their progress file."""
    progress_file = f"progress_{username}.json"
    if os.path.exists(progress_file):
        try:
            with open(progress_file, "r") as f:
                data = json.load(f)
                return data.get("completed_modules", []), data.get("quiz_scores", {}), data.get("completion_dates", {})
        except Exception as e:
            logging.error(f"Error loading progress for {username}: {e}")
            return [], {}, {}
    return [], {}, {}

def save_user_progress(username, completed_modules, quiz_scores, completion_dates):
    """Save user's progress to their progress file."""
    progress_file = f"progress_{username}.json"
    data = {
        "completed_modules": completed_modules,
        "quiz_scores": quiz_scores,
        "completion_dates": completion_dates
    }
    try:
        with open(progress_file, "w") as f:
            json.dump(data, f, indent=4)
    except Exception as e:
        logging.error(f"Error saving progress for {username}: {e}")

def load_user_answers(username):
    """Load user's written answers from their answers file."""
    answers_file = f"answers_{username}.json"
    if os.path.exists(answers_file):
        try:
            with open(answers_file, "r") as f:
                return json.load(f)
        except Exception as e:
            logging.error(f"Error loading answers for {username}: {e}")
            return {}
    return {}

def save_user_answer(username, question, answer):
    """Save user's written answer to their answers file."""
    answers_file = f"answers_{username}.json"
    answers = load_user_answers(username)
    answers[question] = answer
    try:
        with open(answers_file, "w") as f:
            json.dump(answers, f, indent=4)
    except Exception as e:
        logging.error(f"Error saving answer for {username}: {e}")

def reset_user_progress(username):
    """Reset user's progress and answers by deleting their files."""
    progress_file = f"progress_{username}.json"
    answers_file = f"answers_{username}.json"
    try:
        if os.path.exists(progress_file):
            os.remove(progress_file)
        if os.path.exists(answers_file):
            os.remove(answers_file)
        # Clear in-memory progress if user is currently logged in
        if st.session_state.user == username:
            st.session_state.completed_modules = []
            st.session_state.quiz_scores = {}
            st.session_state.completion_dates = {}
        return True
    except Exception as e:
        logging.error(f"Error resetting progress for {username}: {e}")
        return False

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
#         UNIVERSAL show_chapter() FUNCTION (for Chapters 1-4) #
################################################################
def show_chapter(chapter_name: str, modules, final_quiz):
    """
    Unified function to present module content (and tasks) for a chapter.
    Uses only session_state to save the current module index.
    
    chapter_name: "Chapter 1", "Chapter 2", "Chapter 3", "Chapter 4"
    modules: list of dicts (with keys: title, content, task_type, task, etc.)
    final_quiz: list of quiz questions for the chapter
    """
    # Build list of module titles plus a "Final Quiz" option
    module_titles = [mod["title"] for mod in modules] + ["Final Quiz"]

    # Initialize the current module index in session_state if not set
    if f"{chapter_name}_module_index" not in st.session_state:
        st.session_state[f"{chapter_name}_module_index"] = 0

    # Show a selectbox for modules
    selected_module = st.sidebar.selectbox(
        f"Select {chapter_name} Module",
        module_titles,
        index=st.session_state[f"{chapter_name}_module_index"]
    )

    # ---------- If user chose "Final Quiz" ----------
    if selected_module == "Final Quiz":
        st.markdown(f"# {chapter_name} Final Quiz")

        quiz_score = 0
        user_answers = {}
        total_questions = sum(1 for q in final_quiz if not q.get("is_written", False))  # Count only non-written questions
        written_answer = ""
        has_written_question = any(q.get("is_written", False) for q in final_quiz)  # Check if there's a written question

        # Display final quiz questions
        for i, q in enumerate(final_quiz):
            st.markdown(f"**Question {i+1}:** {q['question']}")
            if "is_written" in q and q["is_written"]:
                user_answers[i] = st.text_area("Your Answer:", key=f"{chapter_name}_final_q_{i}")
            else:
                user_answers[i] = st.radio("Select an option:", q["options"], key=f"{chapter_name}_final_q_{i}")

        if st.button("Submit Final Quiz"):
            # Grade the final quiz (excluding written question)
            for i, q in enumerate(final_quiz):
                if "is_written" in q and q["is_written"]:
                    written_answer = user_answers[i].strip()
                    if written_answer:
                        save_user_answer(st.session_state.user, f"{chapter_name} Final Quiz Q{i+1}", written_answer)
                else:
                    correct_index = q["answer"]
                    correct_answer = q["options"][correct_index]
                    if user_answers.get(i) == correct_answer:
                        quiz_score += 1

            # Check written answer for non-empty response if applicable
            written_complete = not has_written_question or bool(written_answer)

            st.info(f"You scored {quiz_score} out of {total_questions} on the multiple-choice questions!")
            if has_written_question:
                if written_complete:
                    st.success("Written answer submitted! Check with your trainer for feedback.")
                else:
                    st.error("Please provide an answer for the written question.")

            # Pass if user got 4 or more correct out of 5 MCQs (if applicable) and completed written answer (if applicable)
            mcq_passing_threshold = 4 if total_questions >= 5 else total_questions  # Adjust threshold for smaller quizzes
            if (total_questions == 0 or quiz_score >= mcq_passing_threshold) and written_complete:
                st.success(f"Great job! You have completed {chapter_name}.")
                st.info("Please click top left for next chapter.")
                # Add final quiz completion to progress
                final_quiz_id = f"{chapter_name.lower().replace(' ', '_')}_final"
                if final_quiz_id not in st.session_state.get('completed_modules', []):
                    st.session_state.completed_modules.append(final_quiz_id)
                    st.session_state.quiz_scores[final_quiz_id] = f"{quiz_score}/{total_questions}" if total_questions > 0 else "N/A"
                    st.session_state.completion_dates[final_quiz_id] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    save_user_progress(st.session_state.user, st.session_state.completed_modules,
                                      st.session_state.quiz_scores, st.session_state.completion_dates)
            else:
                if total_questions > 0 and quiz_score < mcq_passing_threshold:
                    st.error(f"You did not reach the passing score ({mcq_passing_threshold}/{total_questions}) on the multiple-choice questions. Please review the modules and try again.")
                if has_written_question and not written_complete:
                    st.error("You need to provide a written answer to complete the quiz.")
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
                # Add module to completed_modules
                module_id = f"{chapter_name.lower().replace(' ', '_')}_m{module_index + 1}"
                if module_id not in st.session_state.get('completed_modules', []):
                    st.session_state.completed_modules.append(module_id)
                    st.session_state.quiz_scores[module_id] = "N/A (Reflection)"
                    st.session_state.completion_dates[module_id] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    save_user_progress(st.session_state.user, st.session_state.completed_modules,
                                      st.session_state.quiz_scores, st.session_state.completion_dates)
                rerun_app()

    # ---------- Scenario Tasks (single correct answer) ----------
    elif task_type == "scenario":
        options = mod.get("options", [])
        answer = st.radio("Select the correct answer:", options, key=f"{chapter_name}_scenario_{module_index}")
        if st.button("Submit Scenario Answer"):
            if "correct_answer" in mod and mod["correct_answer"] < len(options):
                if options[mod["correct_answer"]] == answer:
                    st.success("Correct answer!")
                    # Advance to next
                    next_module_index = module_index + 1
                    if next_module_index < len(module_titles):
                        st.session_state[f"{chapter_name}_module_index"] = next_module_index
                        # Add module to completed_modules
                        module_id = f"{chapter_name.lower().replace(' ', '_')}_m{module_index + 1}"
                        if module_id not in st.session_state.get('completed_modules', []):
                            st.session_state.completed_modules.append(module_id)
                            st.session_state.quiz_scores[module_id] = "1/1"
                            st.session_state.completion_dates[module_id] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                            save_user_progress(st.session_state.user, st.session_state.completed_modules,
                                              st.session_state.quiz_scores, st.session_state.completion_dates)
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
                    # Add module to completed_modules
                    module_id = f"{chapter_name.lower().replace(' ', '_')}_m{module_index + 1}"
                    if module_id not in st.session_state.get('completed_modules', []):
                        st.session_state.completed_modules.append(module_id)
                        st.session_state.quiz_scores[module_id] = f"{score}/{total}"
                        st.session_state.completion_dates[module_id] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                        save_user_progress(st.session_state.user, st.session_state.completed_modules,
                                          st.session_state.quiz_scores, st.session_state.completion_dates)
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
#                     ADMIN VIEW FUNCTION                      #
################################################################
def show_admin_view():
    """Display the admin view to track trainee progress."""
    st.title("Admin Dashboard - CC Inc. Training App")

    # Get list of trainees (non-admin users)
    trainees = [username for username, info in USERS.items() if info["role"] != "admin"]
    
    # Dropdown to select a trainee
    selected_trainee = st.selectbox("Select Trainee to View Progress", trainees)

    if selected_trainee:
        # Load trainee's progress
        completed_modules, quiz_scores, completion_dates = load_user_progress(selected_trainee)
        total_modules = 25  # 6 (Ch1) + 6 (Ch2) + 6 (Ch3) + 7 (Ch4)
        progress = len(completed_modules) / total_modules

        # Display progress bar
        st.subheader(f"Progress for {selected_trainee}")
        st.progress(progress)
        st.write(f"Progress: {int(progress * 100)}% ({len(completed_modules)}/{total_modules} completed)")

        # Display detailed progress
        st.subheader("Detailed Progress")
        for module_id in completed_modules:
            score = quiz_scores.get(module_id, "N/A")
            date = completion_dates.get(module_id, "Unknown")
            st.write(f"- {module_id}: Score {score}, Completed on {date}")

        # Display written answers
        st.subheader("Written Answers")
        answers = load_user_answers(selected_trainee)
        if answers:
            for question, answer in answers.items():
                st.write(f"**{question}:** {answer}")
        else:
            st.write("No written answers submitted yet.")

        # Reset progress button
        if st.button(f"Reset Progress for {selected_trainee}"):
            if reset_user_progress(selected_trainee):
                st.success(f"Progress for {selected_trainee} has been reset.")
                rerun_app()
            else:
                st.error(f"Failed to reset progress for {selected_trainee}. Check logs for details.")

################################################################
#                     MAIN APP LOGIC                           #
################################################################
def main():
    st.title("CC Inc. Training App")
    
    # Initialize user login and progress in session_state
    if "user" not in st.session_state:
        st.session_state.user = ""
    if "role" not in st.session_state:
        st.session_state.role = ""
    if "completed_modules" not in st.session_state:
        st.session_state.completed_modules = []
    if "quiz_scores" not in st.session_state:
        st.session_state.quiz_scores = {}
    if "completion_dates" not in st.session_state:
        st.session_state.completion_dates = {}

    # If not logged in, show login
    if not st.session_state.user:
        st.sidebar.header("Login")
        username = st.sidebar.text_input("Username:")
        password = st.sidebar.text_input("Password:", type="password")
        if st.sidebar.button("Login"):
            if username in USERS and USERS[username]["password"] == password:
                st.session_state.user = username
                st.session_state.role = USERS[username]["role"]
                # Load progress from file
                completed_modules, quiz_scores, completion_dates = load_user_progress(username)
                st.session_state.completed_modules = completed_modules
                st.session_state.quiz_scores = quiz_scores
                st.session_state.completion_dates = completion_dates
                st.success(f"Welcome, {username}!")
                rerun_app()
            else:
                st.error("Incorrect username or password.")
        return

    # Show progress bar in sidebar
    total_modules = 25  # 6 (Ch1) + 6 (Ch2) + 6 (Ch3) + 7 (Ch4)
    progress = len(st.session_state.completed_modules) / total_modules
    st.sidebar.progress(progress)
    st.sidebar.write(f"Progress: {int(progress * 100)}%")

    # Logout button
    if st.sidebar.button("Logout"):
        # Clear session state
        st.session_state.user = ""
        st.session_state.role = ""
        st.session_state.completed_modules = []
        st.session_state.quiz_scores = {}
        st.session_state.completion_dates = {}
        st.success("You have been logged out.")
        rerun_app()

    # Admin view
    if st.session_state.role == "admin":
        show_admin_view()
        return

    # Trainee view: Let user pick a chapter
    chapter_options = {
        "Chapter 1": {"type": "module_list", "modules": CH1_MODULES, "quiz": CH1_FINAL_QUIZ},
        "Chapter 2": {"type": "module_list", "modules": CH2_MODULES, "quiz": CH2_FINAL_QUIZ},
        "Chapter 3": {"type": "module_list", "modules": CH3_MODULES, "quiz": CH3_FINAL_QUIZ},
        "Chapter 4": {"type": "module_list", "modules": CH4_MODULES, "quiz": CH4_FINAL_QUIZ}
    }

    chapter = st.sidebar.selectbox("Select Chapter", list(chapter_options.keys()))

    if chapter in chapter_options:
        chapter_data = chapter_options[chapter]
        show_chapter(
            chapter_name=chapter,
            modules=chapter_data["modules"],
            final_quiz=chapter_data["quiz"]
        )
    else:
        st.warning("Please select a chapter to begin.")

if __name__ == "__main__":
    main()
