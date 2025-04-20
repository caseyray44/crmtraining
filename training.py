import streamlit as st
import json
import os
import logging
from datetime import datetime

# Import chapter modules and quizzes for Chapters 1-6
from chapter1 import CH1_MODULES, CH1_FINAL_QUIZ
from chapter2 import CH2_MODULES, CH2_FINAL_QUIZ
from chapter3 import CH3_MODULES, CH3_FINAL_QUIZ
from chapter4 import CH4_MODULES, CH4_FINAL_QUIZ
from chapter5 import CH5_MODULES, CH5_FINAL_QUIZ
from chapter6 import CH6_MODULES, CH6_FINAL_QUIZ, show_chapter_6  # Import Chapter 6

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
        if "user" in st.session_state and st.session_state.user == username:
            st.session_state.completed_modules = []
            st.session_state.quiz_scores = {}
            st.session_state.completion_dates = {}
        return True
    except Exception as e:
        logging.error(f"Error resetting progress for {username}: {e}")
        return False

################################################################
#         UNIVERSAL show_chapter() FUNCTION (for Chapters 1-5) #
################################################################
def show_chapter(chapter_name: str, modules, final_quiz):
    """
    Unified function to present module content (and tasks) for a chapter.
    Uses only session_state to save the current module index.
    
    chapter_name: "Chapter 1", "Chapter 2", "Chapter 3", "Chapter 4", "Chapter 5"
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
        index=st.session_state[f"{chapter_name}_module_index"],
        key=f"{chapter_name}_module_select"
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

        if st.button("Submit Final Quiz", key=f"{chapter_name}_submit_final_quiz"):
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

    # ---------- Custom Task for Chapter 6 ----------
    if task_type == "custom" and chapter_name == "Chapter 6":
        show_chapter_6()
        return

    # ---------- Reflection Tasks ----------
    if task_type == "reflection":
        response = st.text_area("Your Reflection:", key=f"{chapter_name}_reflection_{module_index}")
        if st.button("Submit Reflection", key=f"{chapter_name}_submit_reflection_{module_index}"):
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

    # ---------- Scenario Tasks (single correct answer) ----------
    elif task_type == "scenario":
        options = mod.get("options", [])
        answer = st.radio("Select the correct answer:", options, key=f"{chapter_name}_scenario_{module_index}")
        if st.button("Submit Scenario Answer", key=f"{chapter_name}_submit_scenario_{module_index}"):
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

            if st.button("Submit Mini Quiz", key=f"{chapter_name}_submit_miniquiz_{module_index}"):
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
    selected_trainee = st.selectbox("Select Trainee to View Progress", trainees, key="admin_trainee_select")

    if selected_trainee:
        # Load trainee's progress
        completed_modules, quiz_scores, completion_dates = load_user_progress(selected_trainee)
        total_modules = 32  # 6 (Ch1) + 6 (Ch2) + 6 (Ch3) + 7 (Ch4) + 6 (Ch5) + 1 (Ch6)
        progress = len(completed_modules) / total_modules

        # Display progress bar
        st.subheader(f"Progress for {selected_trainee}")
        st.progress(progress)
        st.write(f"Progress: {int(progress * 100)}% ({len(completed_modules)}/{total_modules} completed)")

        # Define chapter metadata for friendly names
        chapter_metadata = {
            "chapter_1": {
                "name": "Chapter 1: Customer Basics",
                "total_modules": 7,  # 6 modules + final quiz
                "modules": {
                    "chapter_1_m1": "Module 1: What is a CRM?",
                    "chapter_1_m2": "Module 2: Logging into Markate",
                    "chapter_1_m3": "Module 3: Navigating to Customers",
                    "chapter_1_m4": "Module 4: Creating Basic Customers",
                    "chapter_1_m5": "Module 5: Creating Advanced Customers",
                    "chapter_1_m6": "Module 6: Creating Commercial Customers",
                    "chapter_1_m7": "Module 7: Creating Your Test Account",
                    "chapter_1_final": "Final Quiz"
                }
            },
            "chapter_2": {
                "name": "Chapter 2: Leads",
                "total_modules": 7,  # 6 modules + final quiz
                "modules": {
                    "chapter_2_m1": "Module 1: Understanding Leads",
                    "chapter_2_m2": "Module 2: Viewing Leads",
                    "chapter_2_m3": "Module 3: The 7 Stages of Leads",
                    "chapter_2_m4": "Module 4: Creating New Leads",
                    "chapter_2_m5": "Module 5: Creating New Opportunities",
                    "chapter_2_m6": "Module 6: Assigning Employees",
                    "chapter_2_m7": "Module 7: Create Your Test Opportunity",
                    "chapter_2_final": "Final Quiz"
                }
            },
            "chapter_3": {
                "name": "Chapter 3: Estimates",
                "total_modules": 6,  # 5 modules + final quiz
                "modules": {
                    "chapter_3_m1": "Module 1: Introduction to Estimates",
                    "chapter_3_m2": "Module 2: Estimate Types",
                    "chapter_3_m3": "Module 3: Creating a Standard Estimate",
                    "chapter_3_m4": "Module 4: Creating an Options Estimate",
                    "chapter_3_m5": "Module 5: Managing Estimates",
                    "chapter_3_m6": "Module 6: Create Estimates for Yourself",
                    "chapter_3_final": "Final Quiz"
                }
            },
            "chapter_4": {
                "name": "Chapter 4: Work Orders",
                "total_modules": 7,  # 6 modules + final quiz
                "modules": {
                    "chapter_4_m1": "Module 1: Our Five Divisions",
                    "chapter_4_m2": "Module 2: What Are Work Orders?",
                    "chapter_4_m3": "Module 3: Navigating Work Orders",
                    "chapter_4_m4": "Module 4: Creating a Work Order (Method 1)",
                    "chapter_4_m5": "Module 5: Creating a Work Order (Method 2)",
                    "chapter_4_m6": "Module 6: Practice and Tips",
                    "chapter_4_final": "Final Quiz"
                }
            },
            "chapter_5": {
                "name": "Chapter 5: Understanding Commissions",
                "total_modules": 6,  # 5 modules + final quiz
                "modules": {
                    "chapter_5_m1": "Module 1: Introduction to Commissions",
                    "chapter_5_m2": "Module 2: Earning 10% Commission",
                    "chapter_5_m3": "Module 3: Earning 5% Commission",
                    "chapter_5_m4": "Module 4: The Payroll Process",
                    "chapter_5_m5": "Module 5: Hourly Rates",
                    "chapter_5_final": "Final Quiz"
                }
            },
            "chapter_6": {
                "name": "Chapter 6: Speed Test with Live Markate",
                "total_modules": 1,  # 1 module (speed test)
                "modules": {
                    "chapter_6_final": "Speed Test with Live Markate"
                }
            }
        }

        # Group completed modules by chapter
        progress_by_chapter = {}
        for module_id in completed_modules:
            chapter_key = "_".join(module_id.split("_")[:2])  # e.g., "chapter_1"
            if chapter_key not in progress_by_chapter:
                progress_by_chapter[chapter_key] = []
            progress_by_chapter[chapter_key].append(module_id)

        # Display detailed progress by chapter
        st.subheader("Detailed Progress by Chapter")
        for chapter_key, chapter_info in chapter_metadata.items():
            chapter_name = chapter_info["name"]
            total_modules = chapter_info["total_modules"]
            completed_in_chapter = progress_by_chapter.get(chapter_key, [])
            num_completed = len(completed_in_chapter)
            is_completed = num_completed == total_modules

            # Display chapter summary with expander
            status_icon = "✅" if is_completed else "⏳"
            with st.expander(f"{status_icon} {chapter_name} ({num_completed}/{total_modules} completed)", expanded=False):
                if not completed_in_chapter:
                    st.write("No modules completed in this chapter yet.")
                else:
                    for module_id in completed_in_chapter:
                        module_name = chapter_info["modules"].get(module_id, module_id)
                        score = quiz_scores.get(module_id, "N/A")
                        date = completion_dates.get(module_id, "Unknown")
                        # Simplify score display
                        if "N/A" in score:
                            score_display = "Passed (Reflection)" if "Reflection" in score else "Completed (Speed Test)"
                        elif "Final Quiz" in module_name:
                            score_display = f"Score: {score}"
                        else:
                            score_display = "Passed"
                        st.write(f"- {module_name}: {score_display} (Completed on {date})")

        # Display written answers with full question context
        st.subheader("Written Answers")
        answers = load_user_answers(selected_trainee)
        if answers:
            # Define questions for context
            written_questions = {
                "Chapter 4 Final Quiz Q6": "Jane Doe calls and asks if she’s been scheduled for her pest control yet. How can you check that information?",
                "Chapter 5 Final Quiz Q6": "You’re calling an existing customer, Jane Smith, to offer new services. Where can you find information about her past jobs to start the conversation?"
                # Add more questions here if other chapters get written questions
            }
            for question_key, answer in answers.items():
                question_text = written_questions.get(question_key, "Unknown question")
                st.write(f"**Question: {question_text}**")
                st.write(f"Answer: {answer}")
                st.write("---")
        else:
            st.write("No written answers submitted by this trainee.")

        # Reset progress button
        if st.button(f"Reset Progress for {selected_trainee}", key=f"reset_progress_{selected_trainee}"):
            if reset_user_progress(selected_trainee):
                st.success(f"Progress for {selected_trainee} has been reset.")
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
    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False

    # If not logged in, show login
    if not st.session_state.logged_in:
        st.sidebar.header("Login")
        username = st.sidebar.text_input("Username:", key="login_username")
        password = st.sidebar.text_input("Password:", type="password", key="login_password")
        if st.sidebar.button("Login", key="login_button"):
            if username in USERS and USERS[username]["password"] == password:
                st.session_state.user = username
                st.session_state.role = USERS[username]["role"]
                # Load progress from file
                completed_modules, quiz_scores, completion_dates = load_user_progress(username)
                st.session_state.completed_modules = completed_modules
                st.session_state.quiz_scores = quiz_scores
                st.session_state.completion_dates = completion_dates
                st.session_state.logged_in = True
                st.success(f"Welcome, {username}!")
            else:
                st.error("Incorrect username or password.")
        return

    # Show progress bar in sidebar
    total_modules = 32  # 6 (Ch1) + 6 (Ch2) + 6 (Ch3) + 7 (Ch4) + 6 (Ch5) + 1 (Ch6)
    progress = len(st.session_state.completed_modules) / total_modules
    st.sidebar.progress(progress)
    st.sidebar.write(f"Progress: {int(progress * 100)}%")

    # Logout button
    if st.sidebar.button("Logout", key="logout_button"):
        # Clear session state
        st.session_state.user = ""
        st.session_state.role = ""
        st.session_state.completed_modules = []
        st.session_state.quiz_scores = {}
        st.session_state.completion_dates = {}
        st.session_state.logged_in = False
        st.success("You have been logged out.")

    # Admin view
    if st.session_state.role == "admin":
        show_admin_view()
        return

    # Trainee view: Let user pick a chapter
    chapter_options = {
        "Chapter 1": {"type": "module_list", "modules": CH1_MODULES, "quiz": CH1_FINAL_QUIZ},
        "Chapter 2": {"type": "module_list", "modules": CH2_MODULES, "quiz": CH2_FINAL_QUIZ},
        "Chapter 3": {"type": "module_list", "modules": CH3_MODULES, "quiz": CH3_FINAL_QUIZ},
        "Chapter 4": {"type": "module_list", "modules": CH4_MODULES, "quiz": CH4_FINAL_QUIZ},
        "Chapter 5": {"type": "module_list", "modules": CH5_MODULES, "quiz": CH5_FINAL_QUIZ},
        "Chapter 6": {"type": "module_list", "modules": CH6_MODULES, "quiz": CH6_FINAL_QUIZ}
    }

    chapter = st.sidebar.selectbox("Select Chapter", list(chapter_options.keys()), key="chapter_select")

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
