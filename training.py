# =============================================================
#  CC Inc. Training App – FULL SOURCE
#  • chapter5.py (ASCII‑clean, unchanged wording)
#  • training.py (complete file with Mason123 added)
# =============================================================

# -------------------------------------------------------------------
#  chapter5.py  (exact text supplied earlier – unchanged below)
# -------------------------------------------------------------------
"""
[chapter5.py content retained – scroll above in the canvas if needed]
"""

# -------------------------------------------------------------------
#  training.py  (copy/paste this ENTIRE file into your project)
# -------------------------------------------------------------------
import streamlit as st
import json
import os
import logging
from datetime import datetime

# Import chapter modules and quizzes
from chapter1 import CH1_MODULES, CH1_FINAL_QUIZ
from chapter2 import CH2_MODULES, CH2_FINAL_QUIZ
from chapter3 import CH3_MODULES, CH3_FINAL_QUIZ
from chapter4 import CH4_MODULES, CH4_FINAL_QUIZ
from chapter5 import CH5_MODULES, CH5_FINAL_QUIZ

# -------------------------------------------------------------------
#  LOGGING
# -------------------------------------------------------------------
logging.basicConfig(
    level=logging.INFO,
    filename="training.log",
    filemode="a",
    format="%(asctime)s - %(levelname)s - %(message)s",
)

# -------------------------------------------------------------------
#  USER CREDENTIALS  (Mason123 added)
# -------------------------------------------------------------------
USERS = {
    "Damon123": {"password": "pass123", "role": "trainee"},
    "jake123":  {"password": "pass123", "role": "trainee"},
    "Mason123": {"password": "pass123", "role": "trainee"},  # NEW
    "Admin":    {"password": "admin123", "role": "admin"},
}

# -------------------------------------------------------------------
#  FILE HELPERS (progress & answers)
# -------------------------------------------------------------------

def load_user_progress(username):
    path = f"progress_{username}.json"
    if os.path.exists(path):
        try:
            with open(path, "r") as f:
                data = json.load(f)
                return (
                    data.get("completed_modules", []),
                    data.get("quiz_scores", {}),
                    data.get("completion_dates", {}),
                )
        except Exception as exc:
            logging.error(f"Error loading progress for {username}: {exc}")
    return [], {}, {}


def save_user_progress(username, completed, scores, dates):
    path = f"progress_{username}.json"
    data = {
        "completed_modules": completed,
        "quiz_scores": scores,
        "completion_dates": dates,
    }
    try:
        with open(path, "w") as f:
            json.dump(data, f, indent=4)
    except Exception as exc:
        logging.error(f"Error saving progress for {username}: {exc}")


def load_user_answers(username):
    path = f"answers_{username}.json"
    if os.path.exists(path):
        try:
            with open(path, "r") as f:
                return json.load(f)
        except Exception as exc:
            logging.error(f"Error loading answers for {username}: {exc}")
    return {}


def save_user_answer(username, question, answer):
    path = f"answers_{username}.json"
    answers = load_user_answers(username)
    answers[question] = answer
    try:
        with open(path, "w") as f:
            json.dump(answers, f, indent=4)
    except Exception as exc:
        logging.error(f"Error saving answer for {username}: {exc}")


def reset_user_progress(username):
    ok = True
    for suffix in ("progress", "answers"):
        path = f"{suffix}_{username}.json"
        if os.path.exists(path):
            try:
                os.remove(path)
            except Exception as exc:
                logging.error(f"Error deleting {path}: {exc}")
                ok = False
    if ok and st.session_state.get("user") == username:
        st.session_state.completed_modules = []
        st.session_state.quiz_scores = {}
        st.session_state.completion_dates = {}
    return ok

# -------------------------------------------------------------------
#  UTILITY
# -------------------------------------------------------------------

def rerun_app():
    if hasattr(st, "experimental_rerun"):
        st.experimental_rerun()
    else:
        st.warning("Please reload manually to continue.")

# -------------------------------------------------------------------
#  GENERIC CHAPTER RENDERER  (works for all Chapters 1‑5)
# -------------------------------------------------------------------

def show_chapter(chapter_name, modules, final_quiz):
    module_titles = [m["title"] for m in modules] + ["Final Quiz"]

    key_idx = f"{chapter_name}_idx"
    if key_idx not in st.session_state:
        st.session_state[key_idx] = 0

    sel = st.sidebar.selectbox(f"{chapter_name} Modules", module_titles, index=st.session_state[key_idx])

    if sel == "Final Quiz":
        render_final_quiz(chapter_name, final_quiz)
        return

    idx = module_titles.index(sel)
    mod = modules[idx]

    st.markdown(f"# {mod['title']}")
    st.markdown(mod["content"])

    task_type = mod.get("task_type", "")
    if task_type == "miniquiz":
        run_mini_quiz(chapter_name, idx, mod)
    elif task_type == "reflection":
        run_reflection(chapter_name, idx)
    elif task_type == "scenario":
        run_scenario(chapter_name, idx, mod)

# -------------------------------------------------------------------
#  MINI‑QUIZ / REFLECTION / SCENARIO HELPERS  (unchanged)
# -------------------------------------------------------------------

def run_mini_quiz(chapter, m_idx, mod):
    qs = mod["miniquiz_questions"]
    answers = {}
    score = 0
    for i, q in enumerate(qs):
        st.markdown(f"**Q{i+1}: {q['question']}**")
        answers[i] = st.radio("Choose:", q["options"], key=f"{chapter}_{m_idx}_{i}")
    if st.button("Submit Quiz", key=f"btn_{chapter}_{m_idx}"):
        for i, q in enumerate(qs):
            if answers.get(i) == q["options"][q["correct_answer"]]:
                score += 1
        st.info(f"Score: {score}/{len(qs)}")
        if score == len(qs):
            st.success("Perfect! Moving on...")
            record_completion(chapter, m_idx, f"{score}/{len(qs)}")
            st.session_state[f"{chapter}_idx"] += 1
            rerun_app()


def run_reflection(chapter, m_idx):
    txt = st.text_area("Your thoughts:")
    if st.button("Submit Reflection", key=f"ref_{chapter}_{m_idx}") and txt.strip():
        st.success("Saved!")
        record_completion(chapter, m_idx, "N/A (reflection)")
        st.session_state[f"{chapter}_idx"] += 1
        rerun_app()


def run_scenario(chapter, m_idx, mod):
    ans = st.radio("Choose:", mod["options"], key=f"sc_{chapter}_{m_idx}")
    if st.button("Submit Answer", key=f"sb_{chapter}_{m_idx}"):
        if ans == mod["options"][mod["correct_answer"]]:
            st.success("Correct!")
            record_completion(chapter, m_idx, "1/1")
            st.session_state[f"{chapter}_idx"] += 1
            rerun_app()
        else:
            st.error("Try again.")

# -------------------------------------------------------------------
#  FINAL QUIZ HANDLER (unchanged logic)
# -------------------------------------------------------------------

def render_final_quiz(chapter, quiz):
    st.markdown(f"# {chapter} – Final Quiz")
    answers = {}
    mc_total = sum(1 for q in quiz if not q.get("is_written"))
    mc_score = 0
    written_ok = True

    for i, q in enumerate(quiz):
        st.markdown(f"**Q{i+1}: {q['question']}**")
        if q.get("is_written"):
            ans = st.text_area("Your answer:", key=f"w_{chapter}_{i}")
            answers[i] = ans.strip()
            if not answers[i]:
                written_ok = False
        else:
            answers[i] = st.radio("Choose:", q["options"], key=f"mc_{chapter}_{i}")

    if st.button("Submit Final Quiz", key=f"fin_{chapter}"):
        for i, q in enumerate(quiz):
            if not q.get("is_written") and answers[i] == q["options"][q["answer"]]:
                mc_score += 1
        st.info(f"MCQ Score: {mc_score}/{mc_total}")
        if mc_score == mc_total and written_ok:
            st.success("Chapter complete!")
            record_completion(chapter, "final", f"{mc_score}/{mc_total}")
        else:
            st.error("Please answer all questions correctly and fill any written sections.")

# -------------------------------------------------------------------
#  PROGRESS RECORDING
# -------------------------------------------------------------------

def record_completion(chapter, mod_idx, score):
    user = st.session_state.user
    compl = st.session_state.completed_modules
    scores = st.session_state.quiz_scores
    dates = st.session_state.completion_dates

    mod_id = f"{chapter.lower().replace(' ', '_')}_m{mod_idx+1}" if mod_idx != "final" else f"{chapter.lower().replace(' ', '_')}_final"
    if mod_id not in compl:
        compl.append(mod_id)
        scores[mod_id] = score
        dates[mod_id] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        save_user_progress(user, compl, scores, dates)

# -------------------------------------------------------------------
#  ADMIN DASHBOARD (unchanged)
# -------------------------------------------------------------------

def admin_view():
    st.title("Admin Dashboard")
    trainees = [u for u, d in USERS.items() if d["role"] != "admin"]
    sel = st.selectbox("Select trainee", trainees)
    if sel:
        comp, scores, dates = load_user_progress(sel)
        st.write(f"Completed modules: {len(comp)}")
        for mid in comp:
            st.write(f"- {mid}: {scores.get(mid, '')} ({dates.get(mid, '')})")
        if st.button("Reset Progress", key=f"reset_{sel}"):
            if reset_user_progress(sel):
                st.success("Reset!")
            else:
                st.error("Failed.")

# -------------------------------------------------------------------
#  MAIN
# -------------------------------------------------------------------

def main():
    st.sidebar.title("CC Inc. Training")

    if "user" not in st.session_state:
        st.session_state.user = ""
        st.session_state.role = ""
        st.session_state.completed_modules = []
        st.session_state.quiz
