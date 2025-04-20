import streamlit as st
import time
import json
import os
from datetime import datetime

# Chapter 6 Scenarios
CH6_SCENARIOS = [
    # Scenario 1: Susan Hicks
    [
        {
            "customer": "Susan Hicks",
            "question": "You’re talking to Susan Hicks. She asks, 'What just got scheduled?'",
            "options": ["Window Washing", "Rodent Control", "Pest Control 2x", "Pest Control 3x"],
            "correct_answer": "Pest Control 3x",
            "type": "multiple_choice",
            "explanation": "The correct answer is Pest Control 3x. In the Markate dashboard, search for the customer 'Susan Hicks' to find her recent work orders. Locate the most recent work order (ID 1), which shows the service as 'Pest Control 3x' with a status of 'Scheduled'. This indicates it’s the latest scheduled service."
        },
        {
            "customer": "Susan Hicks",
            "question": "She asks, 'When is that scheduled?'",
            "options": ["May 5th-May 9th", "June 10th, 2-3 PM", "April 20th, 10-11 AM"],
            "correct_answer": "May 5th-May 9th",
            "type": "multiple_choice",
            "explanation": "The correct answer is May 5th-May 9th. In the Markate dashboard, go to Susan Hicks’ work orders and find the 'Pest Control 3x' work order (ID 1). The 'scheduled_date' field shows 'May 5th-May 9th', indicating when the service is planned."
        },
        {
            "customer": "Susan Hicks",
            "question": "She asks, 'Why is that scheduled for May 5th-May 9th?' (Type your answer)",
            "correct_keywords": ["techs", "week", "weather", "schedule"],
            "reference_answer": "Because that’s when techs will be on site. We schedule pest control generally a week because of weather and schedule changes to accommodate.",
            "type": "written",
            "explanation": "A correct answer includes at least two of these ideas: techs, week, weather, or schedule. For example, 'Because that’s when techs will be on site. We schedule pest control generally a week because of weather and schedule changes to accommodate.' In the Markate dashboard, note that the 'Pest Control 3x' work order for Susan Hicks spans multiple days (May 5th-May 9th). This suggests scheduling considerations like technician availability, weather impacts, or customer scheduling preferences."
        }
    ],
    # Scenario 2: Marilyn Koehler
    [
        {
            "customer": "Marilyn Koehler",
            "question": "Marilyn Koehler calls and asks, 'How much is it to do house washing?'",
            "options": ["$535.80", "$384.40", "$267.36", "$245.89"],
            "correct_answer": "$535.80",
            "type": "multiple_choice",
            "explanation": "The correct answer is $535.80. In the Markate dashboard, search for the customer 'Marilyn Koehler' to find her estimate. Locate the service labeled 'House washing (Main/Garage)'. The total price, including tax (7.375%), is $535.80. This price covers both the house and garage."
        },
        {
            "customer": "Marilyn Koehler",
            "question": "Marilyn Koehler asks, 'What does the house washing cover?'",
            "options": ["House only", "Garage only", "House and garage", "House, garage, and windows"],
            "correct_answer": "House and garage",
            "type": "multiple_choice",
            "explanation": "The correct answer is House and garage. In Marilyn Koehler’s estimate, under the 'House washing (Main/Garage)' service, check the description. It states 'Full soap/scrub/rinse house cleaning on all siding, soffit, trim' and specifies 'House/Garage,' indicating coverage for both. Windows are listed as separate services."
        },
        {
            "customer": "Marilyn Koehler",
            "question": "Marilyn Koehler asks, 'When did I get the windows done last?'",
            "options": ["Sep 12, 2023", "Oct 2, 2024", "Nov 15, 2024", "Dec 1, 2024"],
            "correct_answer": "Oct 2, 2024",
            "type": "multiple_choice",
            "explanation": "The correct answer is Oct 2, 2024. In the Markate dashboard, click on the customer’s name, 'Marilyn Koehler,' to access her profile. Navigate to the 'Work Orders' section to view past services. Find the most recent work order for window washing (Work Order #WO-008112). The 'Scheduled' column shows the date as Oct 2, 2024, indicating the last time the windows were done."
        }
    ]
    # Placeholder for Scenarios 3-10 to be added later
]

def format_time(seconds):
    """Format time in minutes and seconds."""
    minutes = seconds // 60
    remaining_seconds = seconds % 60
    return f"{minutes} minutes {remaining_seconds} seconds"

def load_scenario_results(username):
    """Load user's scenario results from a file."""
    results_file = f"scenario_results_{username}.json"
    if os.path.exists(results_file):
        try:
            with open(results_file, "r") as f:
                return json.load(f)
        except:
            return []
    return []

def save_scenario_results(username, results):
    """Save user's scenario results to a file."""
    results_file = f"scenario_results_{username}.json"
    try:
        with open(results_file, "w") as f:
            json.dump(results, f, indent=4)
    except Exception as e:
        st.error(f"Error saving scenario results: {e}")

def show_chapter_6():
    """Display Chapter 6: Speed Test with Live Markate."""
    # Import save_user_progress inside the function to avoid circular import
    from training import save_user_progress

    st.markdown("# Chapter 6: Speed Test with Live Markate")
    
    # Initialize session state variables
    if "ch6_quiz_started" not in st.session_state:
        st.session_state.ch6_quiz_started = False
    if "ch6_current_scenario" not in st.session_state:
        st.session_state.ch6_current_scenario = 0
    if "ch6_current_question" not in st.session_state:
        st.session_state.ch6_current_question = 0
    if "ch6_start_time" not in st.session_state:
        st.session_state.ch6_start_time = None
    if "ch6_total_time" not in st.session_state:
        st.session_state.ch6_total_time = 0
    if "ch6_attempts" not in st.session_state:
        st.session_state.ch6_attempts = []
    if "ch6_correct_answers" not in st.session_state:
        st.session_state.ch6_correct_answers = 0
    if "ch6_scenario_results" not in st.session_state:
        st.session_state.ch6_scenario_results = load_scenario_results(st.session_state.user)
    if "ch6_show_results" not in st.session_state:
        st.session_state.ch6_show_results = False
    if "ch6_show_history" not in st.session_state:
        st.session_state.ch6_show_history = False
    if "ch6_action" not in st.session_state:
        st.session_state.ch6_action = None

    # Process actions from previous interactions
    if st.session_state.ch6_action:
        action = st.session_state.ch6_action
        st.session_state.ch6_action = None  # Clear the action after processing

        if action == "start_quiz":
            st.session_state.ch6_quiz_started = True
            st.session_state.ch6_start_time = time.time()
            st.session_state.ch6_total_time = 0
            st.session_state.ch6_attempts = []
            st.session_state.ch6_correct_answers = 0
            st.session_state.ch6_current_scenario = 0
            st.session_state.ch6_current_question = 0
            st.session_state.ch6_show_results = False
            st.session_state.ch6_show_history = False
        elif action == "next_scenario":
            st.session_state.ch6_current_scenario += 1
            st.session_state.ch6_current_question = 0
            st.session_state.ch6_start_time = time.time()
            st.session_state.ch6_total_time = 0
            st.session_state.ch6_attempts = []
            st.session_state.ch6_correct_answers = 0
            st.session_state.ch6_show_results = False
        elif action == "restart_quiz":
            st.session_state.ch6_quiz_started = False
            st.session_state.ch6_current_scenario = 0
            st.session_state.ch6_current_question = 0
            st.session_state.ch6_start_time = None
            st.session_state.ch6_total_time = 0
            st.session_state.ch6_attempts = []
            st.session_state.ch6_correct_answers = 0
            st.session_state.ch6_show_results = False
            st.session_state.ch6_show_history = False
        elif action == "view_history":
            st.session_state.ch6_show_history = True
            st.session_state.ch6_show_results = False
        elif action == "back_to_start":
            st.session_state.ch6_quiz_started = False
            st.session_state.ch6_current_scenario = 0
            st.session_state.ch6_current_question = 0
            st.session_state.ch6_start_time = None
            st.session_state.ch6_total_time = 0
            st.session_state.ch6_attempts = []
            st.session_state.ch6_correct_answers = 0
            st.session_state.ch6_show_results = False
            st.session_state.ch6_show_history = False
        elif action.startswith("give_up_"):
            scenario, question = map(int, action.split("_")[2:])
            st.session_state[f"ch6_explanation_{scenario}_{question}"] = True
            st.session_state.ch6_total_time += 300  # 5-minute penalty
        elif action.startswith("submit_"):
            scenario, question = map(int, action.split("_")[2:])
            current_scenario = CH6_SCENARIOS[scenario]
            current_question = current_scenario[question]
            selected = st.session_state[f"selected_{scenario}_{question}"]
            is_correct = False
            if current_question["type"] == "multiple_choice":
                if not selected:
                    st.session_state[f"error_{scenario}_{question}"] = "Please select an answer."
                    return
                is_correct = selected == current_question["correct_answer"]
            else:
                if not selected:
                    st.session_state[f"error_{scenario}_{question}"] = "Please enter an answer."
                    return
                response = selected.lower()
                matched_keywords = [kw for kw in current_question["correct_keywords"] if kw in response]
                is_correct = len(matched_keywords) >= 2

            st.session_state.ch6_attempts.append({
                "scenario": scenario,
                "question": question,
                "selected": selected,
                "correct": is_correct
            })

            if is_correct:
                st.session_state.ch6_correct_answers += 1
                st.session_state.ch6_current_question += 1
                if f"ch6_explanation_{scenario}_{st.session_state.ch6_current_question}" in st.session_state:
                    del st.session_state[f"ch6_explanation_{scenario}_{st.session_state.ch6_current_question}"]
                if st.session_state.ch6_current_question >= len(current_scenario):
                    # Scenario completed
                    scenario_time = int(time.time() - st.session_state.ch6_start_time) + st.session_state.ch6_total_time
                    st.session_state.ch6_scenario_results.append({
                        "scenario": st.session_state.ch6_current_scenario + 1,
                        "time": scenario_time,
                        "correct": st.session_state.ch6_correct_answers,
                        "total_questions": len(current_scenario),
                        "attempts": len([a for a in st.session_state.ch6_attempts if a["scenario"] == st.session_state.ch6_current_scenario]),
                        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    })
                    save_scenario_results(st.session_state.user, st.session_state.ch6_scenario_results)
                    st.session_state.ch6_show_results = True
            else:
                st.session_state[f"error_{scenario}_{question}"] = (
                    "Incorrect answer. Try again." if current_question["type"] == "multiple_choice"
                    else "Your answer is not quite right. Try including details about " + ", ".join(current_question["correct_keywords"]) + "."
                )

    # Intro page
    if not st.session_state.ch6_quiz_started:
        st.markdown("""
        Welcome to Chapter 6 of your CRM training! 🎉 In this exciting challenge, you’ll be working with real-life scenarios using the **live Markate account** (not staging). Your goal? Answer customer questions as quickly and accurately as possible while navigating the Markate dashboard.

        First, make sure you’re logged into the live Markate account. Click here to log in: [www.markate.com](https://www.markate.com). Once you’re logged in, come back here to start the quiz.

        This quiz is timed, and the goal is to keep your time as short as possible. If you’re stuck, you can use the “I Give Up, Teach Me” button to see the answer and learn how to find it, but this will add a 5-minute penalty to your time. Ready to test your speed and skills? Let’s get started!
        """)
        if st.button("Start Chapter 6 Quiz", key="start_quiz"):
            st.session_state.ch6_action = "start_quiz"
        return

    # Results page
    if st.session_state.ch6_show_results:
        scenario_time = st.session_state.ch6_scenario_results[-1]["time"]
        st.markdown(f"## Scenario Completed!")
        st.write(f"**Scenario {st.session_state.ch6_current_scenario + 1} Time:** {format_time(scenario_time)}")
        st.write(f"**Correct Answers:** {st.session_state.ch6_correct_answers}/{len(CH6_SCENARIOS[st.session_state.ch6_current_scenario])}")
        st.write(f"**Total Attempts:** {len([a for a in st.session_state.ch6_attempts if a['scenario'] == st.session_state.ch6_current_scenario])}")

        if st.session_state.ch6_current_scenario < len(CH6_SCENARIOS) - 1:
            if st.button("Next Scenario", key="next_scenario"):
                st.session_state.ch6_action = "next_scenario"
        else:
            st.success("You have completed all scenarios in Chapter 6!")
            # Mark Chapter 6 as completed
            module_id = "chapter_6_final"
            if module_id not in st.session_state.get('completed_modules', []):
                st.session_state.completed_modules.append(module_id)
                st.session_state.quiz_scores[module_id] = "N/A (Speed Test)"
                st.session_state.completion_dates[module_id] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                save_user_progress(st.session_state.user, st.session_state.completed_modules,
                                  st.session_state.quiz_scores, st.session_state.completion_dates)
            if st.button("Restart Chapter 6", key="restart_quiz"):
                st.session_state.ch6_action = "restart_quiz"

        if st.button("View Past Results", key="view_history"):
            st.session_state.ch6_action = "view_history"
        return

    # History page
    if st.session_state.ch6_show_history:
        st.markdown("## Past Results")
        if st.session_state.ch6_scenario_results:
            for result in st.session_state.ch6_scenario_results:
                st.markdown(f"### Attempt ({result['timestamp']}) - Scenario {result['scenario']}")
                st.write(f"Time: {format_time(result['time'])}")
                st.write(f"Correct: {result['correct']}/{result['total_questions']}")
                st.write(f"Attempts: {result['attempts']}")
                st.markdown("---")
        else:
            st.write("No past results available.")
        if st.button("Back to Start", key="back_to_start"):
            st.session_state.ch6_action = "back_to_start"
        return

    # Quiz logic
    current_scenario = CH6_SCENARIOS[st.session_state.ch6_current_scenario]
    current_question = current_scenario[st.session_state.ch6_current_question]

    # Display timer
    if st.session_state.ch6_start_time:
        elapsed = int(time.time() - st.session_state.ch6_start_time) + st.session_state.ch6_total_time
        minutes = elapsed // 60
        seconds = elapsed % 60
        st.markdown(f"<div style='font-size: 24px; font-weight: bold; color: #d32f2f;'>Time: {minutes} minutes {seconds} seconds</div>", unsafe_allow_html=True)

    # Progress bar
    progress = (st.session_state.ch6_current_question / len(current_scenario))
    st.progress(progress)
    st.write(f"Scenario {st.session_state.ch6_current_scenario + 1} of {len(CH6_SCENARIOS)}")
    st.write(f"Question {st.session_state.ch6_current_question + 1} of {len(current_scenario)}")

    # Display question
    st.markdown(f"<div style='background-color: #f9f9f9; padding: 15px; border-radius: 5px; margin-bottom: 20px;'><strong>{current_question['customer']}:</strong> {current_question['question']}</div>", unsafe_allow_html=True)
    st.markdown("<p><em>Note: Use the live Markate dashboard in another tab to find the answers.</em></p>", unsafe_allow_html=True)

    # Answer input
    if current_question["type"] == "multiple_choice":
        selected = st.radio("Select an answer:", current_question["options"], key=f"q_{st.session_state.ch6_current_scenario}_{st.session_state.ch6_current_question}")
    else:
        selected = st.text_area("Type your answer:", key=f"q_{st.session_state.ch6_current_scenario}_{st.session_state.ch6_current_question}")
    
    # Store the selected answer in session state
    st.session_state[f"selected_{st.session_state.ch6_current_scenario}_{st.session_state.ch6_current_question}"] = selected

    # Display explanation if "I Give Up, Teach Me" was clicked
    if f"ch6_explanation_{st.session_state.ch6_current_scenario}_{st.session_state.ch6_current_question}" in st.session_state:
        st.markdown(f"<div style='background-color: #fff3cd; padding: 10px; border-radius: 5px; margin-top: 10px;'>{current_question['explanation']}</div>", unsafe_allow_html=True)

    # Error message placeholder
    error_key = f"error_{st.session_state.ch6_current_scenario}_{st.session_state.ch6_current_question}"
    if error_key in st.session_state:
        st.error(st.session_state[error_key])

    # Buttons
    col1, col2 = st.columns(2)
    with col1:
        if st.button("I Give Up, Teach Me", key=f"give_up_{st.session_state.ch6_current_scenario}_{st.session_state.ch6_current_question}"):
            st.session_state.ch6_action = f"give_up_{st.session_state.ch6_current_scenario}_{st.session_state.ch6_current_question}"
    with col2:
        if st.button("Submit", key=f"submit_{st.session_state.ch6_current_scenario}_{st.session_state.ch6_current_question}"):
            st.session_state.ch6_action = f"submit_{st.session_state.ch6_current_scenario}_{st.session_state.ch6_current_question}"

# Export for training.py
CH6_MODULES = [
    {"title": "Speed Test with Live Markate", "content": "Complete the speed test scenarios to practice using the live Markate dashboard.", "task_type": "custom"}
]
CH6_FINAL_QUIZ = []  # No final quiz for Chapter 6, handled within show_chapter_6
