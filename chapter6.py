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
 NORMALLY WOULD BE HERE BUT ITS CUT OFF
---
Timestamp: April 20, 2025, 19:41
Conversation Summary: - You expressed frustration with the CC Inc. Training App, noting that the entire page doesn’t load and an `ImportError` occurs due to a circular import between `chapter6.py` and `training.py`. I analyzed the traceback, identified the circular import issue (`training.py` importing from `chapter6.py` and vice versa), and suggested moving the import of `save_user_progress` inside the `show_chapter_6()` function to resolve it.
- You mentioned that the error occurs after selecting Chapter 6, and you were able to test other chapters successfully, confirming that the issue is isolated to Chapter 6’s imports. I provided an updated `chapter6.py` with the fix, along with steps to redeploy on Streamlit Cloud and test the app.
- You asked about proceeding with adding Scenario 3 for Chapter 6 once the issue was fixed, and I agreed, outlining that we’d continue adding scenarios up to 10 and then adjust the layout to display past results on the left side of the screen.
- You confirmed that the app is hosted on Streamlit Cloud and shared that you’re using GitHub to manage the repository, asking about the deployment process. I explained how to push changes to GitHub and trigger a redeploy on Streamlit Cloud, either manually or via auto-deploy.
---
Timestamp: April 20, 2025, 20:11
Conversation Summary: - You reported that the CC Inc. Training App no longer showed the previous `ImportError` in Chapter 6, but a new issue emerged where buttons (e.g., "Start Chapter 6 Quiz", "I Give Up, Teach Me") required double clicks to work, and this problem extended to all chapters after further testing. I analyzed the issue, attributing it to Streamlit’s rerun behavior and state management, and suggested removing manual `st.rerun()` calls to fix it.
- You mentioned that the double-click issue didn’t exist in earlier versions of the app before Chapter 6 changes, and I agreed to compare the current `training.py` with the original to identify the cause. I proposed restructuring the app to handle state transitions more naturally, avoiding the need for manual reruns.
- You expressed frustration with the persistent double-click issue, noting it affects the user experience across the app, including login and other chapters. I acknowledged the impact and provided an updated `training.py` and `chapter6.py` with the fix, emphasizing testing across all chapters to ensure single-click functionality.
- You asked to proceed with adding more scenarios for Chapter 6 after resolving the double-click issue, and I agreed, suggesting we fix the issue first to avoid compounding problems with new scenarios.
---
Timestamp: April 20, 2025, 20:22
Conversation Summary: - You shared the original `training.py` before Chapter 6 changes, noting that the double-click issue didn’t exist back then, and expressed frustration that the issue still persisted after recent updates, affecting all chapters. I compared the original and current versions, identifying that the removal of `rerun_app()` (which used `st.experimental_rerun()`) caused the double-click problem due to Streamlit’s natural rerun cycle not advancing the UI.
- You confirmed that the double-click issue was consistent across all buttons in all chapters, including login, and asked for a solution to fix it before adding more scenarios. I proposed reintroducing manual reruns with `st.rerun()` (the modern equivalent) and provided an updated `training.py` and `chapter6.py` to restore the original behavior while addressing the `AttributeError` for `st.rerun()`.
- You expressed a desire to move forward with adding scenarios once the double-click issue was fixed, and I agreed, suggesting we test the updated files thoroughly to ensure single-click functionality across all chapters.
- I asked for confirmation of the button behavior and access to the earlier `training.py`, which you provided, allowing us to pinpoint the cause of the double-click issue.
---
Timestamp: April 20, 2025, 20:35
Conversation Summary: - You reported that the `AttributeError` for `st.rerun()` reappeared in the CC Inc. Training App after updates, affecting login, Chapter 6 start, and logout, and noted that the double-click issue persisted despite login working on the first click. I analyzed the issue, attributing the error to a potential Streamlit version mismatch on Streamlit Cloud (not recognizing `st.rerun()` despite pinning 1.30.0), and suggested restructuring the app to avoid `st.rerun()` calls entirely.
- You confirmed that the login worked on the first click but Chapter 6 still required double clicks, and other chapters were affected similarly, as shown in error screenshots. I provided an updated `training.py` with a `safe_rerun()` function and optimized state management using `st.session_state.view` to eliminate the double-click issue, along with steps to verify the Streamlit version on Cloud.
- You expressed a desire to proceed with adding scenarios once the double-click issue was resolved, and I agreed, emphasizing the need to confirm the Streamlit version and test the updated app thoroughly.
- I suggested checking the Streamlit Cloud logs to confirm the version and rebuilding the app to ensure the correct dependencies were applied, addressing the `AttributeError` issue.
---
Timestamp: April 20, 2025, 20:48
Conversation Summary: - You reported that the CC Inc. Training App no longer showed the `AttributeError` for `st.rerun()`, and login worked on the first click, but Chapter 6 still required double clicks, while other chapters worked perfectly with single clicks. I analyzed the issue, noting that Chapter 6’s internal state transitions (e.g., "intro" to "quiz") weren’t advancing the UI on the first click due to Streamlit’s rendering behavior, unlike the sidebar-driven transitions in Chapters 1–5.
- You expressed frustration that the double-click issue persisted in Chapter 6 despite progress elsewhere, and wanted to make changes and add scenarios but needed the issue fixed first. I suggested restructuring Chapter 6’s state transitions to isolate rendering logic, adding early returns after state changes to prevent re-rendering the old view, and provided an updated `chapter6.py` with the fix.
- You confirmed that the issue was isolated to Chapter 6 buttons (e.g., "Start Chapter 6 Quiz", "Submit"), and I focused on ensuring Chapter 6’s UI updates mirrored the successful single-click behavior of other chapters.
- I outlined a testing plan to verify the fix across all Chapter 6 buttons and ensure other chapters remained unaffected, setting the stage for adding new scenarios once resolved.

===

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

    # Initialize session state variables
    if "ch6_view" not in st.session_state:
        st.session_state.ch6_view = "intro"
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

    # Render the appropriate view based on ch6_view
    st.markdown("# Chapter 6: Speed Test with Live Markate")

    # Intro page
    if st.session_state.ch6_view == "intro":
        st.markdown("""
        Welcome to Chapter 6 of your CRM training! 🎉 In this exciting challenge, you’ll be working with real-life scenarios using the **live Markate account** (not staging). Your goal? Answer customer questions as quickly and accurately as possible while navigating the Markate dashboard.

        First, make sure you’re logged into the live Markate account. Click here to log in: [www.markate.com](https://www.markate.com). Once you’re logged in, come back here to start the quiz.

        This quiz is timed, and the goal is to keep your time as short as possible. If you’re stuck, you can use the “I Give Up, Teach Me” button to see the answer and learn how to find it, but this will add a 5-minute penalty to your time. Ready to test your speed and skills? Let’s get started!
        """)
        if st.button("Start Chapter 6 Quiz", key="start_quiz"):
            st.session_state.ch6_view = "quiz"
            st.session_state.ch6_start_time = time.time()
            st.session_state.ch6_total_time = 0
            st.session_state.ch6_attempts = []
            st.session_state.ch6_correct_answers = 0
            st.session_state.ch6_current_scenario = 0
            st.session_state.ch6_current_question = 0
            # Clear any temporary state
            for key in list(st.session_state.keys()):
                if key.startswith("error_") or key.startswith("ch6_explanation_"):
                    del st.session_state[key]
            # Dummy widget to force Streamlit to recognize the state change
            st.empty()
        return

    # Results page
    if st.session_state.ch6_view == "results":
        scenario_time = st.session_state.ch6_scenario_results[-1]["time"] if st.session_state.ch6_scenario_results else 0
        st.markdown(f"## Scenario Completed!")
        st.write(f"**Scenario {st.session_state.ch6_current_scenario + 1} Time:** {format_time(scenario_time)}")
        st.write(f"**Correct Answers:** {st.session_state.ch6_correct_answers}/{len(CH6_SCENARIOS[st.session_state.ch6_current_scenario])}")
        st.write(f"**Total Attempts:** {len([a for a in st.session_state.ch6_attempts if a['scenario'] == st.session_state.ch6_current_scenario])}")

        if st.session_state.ch6_current_scenario < len(CH6_SCENARIOS) - 1:
            if st.button("Next Scenario", key=f"next_scenario_{st.session_state.ch6_current_scenario}"):
                st.session_state.ch6_current_scenario += 1
                st.session_state.ch6_current_question = 0
                st.session_state.ch6_start_time = time.time()
                st.session_state.ch6_total_time = 0
                st.session_state.ch6_attempts = []
                st.session_state.ch6_correct_answers = 0
                st.session_state.ch6_view = "quiz"
                # Clear any temporary state
                for key in list(st.session_state.keys()):
                    if key.startswith("error_") or key.startswith("ch6_explanation_"):
                        del st.session_state[key]
                # Dummy widget to force Streamlit to recognize the state change
                st.empty()
                return
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
                st.session_state.ch6_view = "intro"
                st.session_state.ch6_current_scenario = 0
                st.session_state.ch6_current_question = 0
                st.session_state.ch6_start_time = None
                st.session_state.ch6_total_time = 0
                st.session_state.ch6_attempts = []
                st.session_state.ch6_correct_answers = 0
                # Clear any temporary state
                for key in list(st.session_state.keys()):
                    if key.startswith("error_") or key.startswith("ch6_explanation_"):
                        del st.session_state[key]
                # Dummy widget to force Streamlit to recognize the state change
                st.empty()
                return

        if st.button("View Past Results", key="view_history"):
            st.session_state.ch6_view = "history"
            # Clear any temporary state
            for key in list(st.session_state.keys()):
                if key.startswith("error_") or key.startswith("ch6_explanation_"):
                    del st.session_state[key]
            # Dummy widget to force Streamlit to recognize the state change
            st.empty()
            return
        return

    # History page
    if st.session_state.ch6_view == "history":
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
            st.session_state.ch6_view = "intro"
            st.session_state.ch6_current_scenario = 0
            st.session_state.ch6_current_question = 0
            st.session_state.ch6_start_time = None
            st.session_state.ch6_total_time = 0
            st.session_state.ch6_attempts = []
            st.session_state.ch6_correct_answers = 0
            # Clear any temporary state
            for key in list(st.session_state.keys()):
                if key.startswith("error_") or key.startswith("ch6_explanation_"):
                    del st.session_state[key]
            # Dummy widget to force Streamlit to recognize the state change
            st.empty()
            return
        return

    # Quiz logic (ch6_view == "quiz")
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
    selected_key = f"q_{st.session_state.ch6_current_scenario}_{st.session_state.ch6_current_question}"
    if current_question["type"] == "multiple_choice":
        selected = st.radio("Select an answer:", current_question["options"], key=selected_key)
    else:
        selected = st.text_area("Type your answer:", value="", key=selected_key)

    # Display explanation if "I Give Up, Teach Me" was clicked
    explanation_key = f"ch6_explanation_{st.session_state.ch6_current_scenario}_{st.session_state.ch6_current_question}"
    if explanation_key in st.session_state:
        st.markdown(f"<div style='background-color: #fff3cd; padding: 10px; border-radius: 5px; margin-top: 10px;'>{current_question['explanation']}</div>", unsafe_allow_html=True)

    # Error message placeholder
    error_key = f"error_{st.session_state.ch6_current_scenario}_{st.session_state.ch6_current_question}"
    if error_key in st.session_state:
        st.error(st.session_state[error_key])

    # Buttons
    col1, col2 = st.columns(2)
    with col1:
        if st.button("I Give Up, Teach Me", key=f"give_up_{st.session_state.ch6_current_scenario}_{st.session_state.ch6_current_question}"):
            st.session_state[explanation_key] = True
            st.session_state.ch6_total_time += 300  # 5-minute penalty
            # Dummy widget to force Streamlit to recognize the state change
            st.empty()
            return
    with col2:
        if st.button("Submit", key=f"submit_{st.session_state.ch6_current_scenario}_{st.session_state.ch6_current_question}"):
            if error_key in st.session_state:
                del st.session_state[error_key]  # Clear previous error
            is_correct = False
            if current_question["type"] == "multiple_choice":
                if not selected:
                    st.session_state[error_key] = "Please select an answer."
                    # Dummy widget to force Streamlit to recognize the state change
                    st.empty()
                    return
                is_correct = selected == current_question["correct_answer"]
            else:
                if not selected:
                    st.session_state[error_key] = "Please enter an answer."
                    # Dummy widget to force Streamlit to recognize the state change
                    st.empty()
                    return
                response = selected.lower()
                matched_keywords = [kw for kw in current_question["correct_keywords"] if kw in response]
                is_correct = len(matched_keywords) >= 2

            st.session_state.ch6_attempts.append({
                "scenario": st.session_state.ch6_current_scenario,
                "question": st.session_state.ch6_current_question,
                "selected": selected,
                "correct": is_correct
            })

            if is_correct:
                st.session_state.ch6_correct_answers += 1
                st.session_state.ch6_current_question += 1
                if explanation_key in st.session_state:
                    del st.session_state[explanation_key]
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
                    st.session_state.ch6_view = "results"
                    # Clear any temporary state
                    for key in list(st.session_state.keys()):
                        if key.startswith("error_") or key.startswith("ch6_explanation_"):
                            del st.session_state[key]
                    # Dummy widget to force Streamlit to recognize the state change
                    st.empty()
                    return
            else:
                st.session_state[error_key] = (
                    "Incorrect answer. Try again." if current_question["type"] == "multiple_choice"
                    else "Your answer is not quite right. Try including details about " + ", ".join(current_question["correct_keywords"]) + "."
                )
                # Dummy widget to force Streamlit to recognize the state change
                st.empty()
                return

# Export for training.py
CH6_MODULES = [
    {"title": "Speed Test with Live Markate", "content": "Complete the speed test scenarios to practice using the live Markate dashboard.", "task_type": "custom"}
]
CH6_FINAL_QUIZ = []  # No final quiz for Chapter 6, handled within show_chapter_6
