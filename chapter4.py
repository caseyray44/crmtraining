import streamlit as st

def display_chapter():
    st.header("Chapter 4: Understanding Work Orders in Markate")

    # Module 1: Our Five Divisions and Why Work Orders Are Division-Specific
    st.subheader("Module 1: Our Five Divisions and Why Work Orders Are Division-Specific")
    st.markdown("""
    Welcome, sales rep! Our business has five divisions: House Washing, Pest Control, Window Washing, Painting/Staining, and Holiday Lights. Each division has its own truck and trained technicians. This keeps us organized but means work orders must be specific to one division.

    **Why separate work orders?**
    - Each truck carries tools for one service. A window washing truck can’t do pest control.
    - Technicians are trained for one division. A house washing tech can’t paint.
    - Combining services on one work order causes confusion. For example:
      - If a customer wants window washing and pest control, create two work orders: one for each division. A window washing tech can’t spray for pests!
      - If a work order says “John Doe - House Washing and Holiday Lights,” the house washing truck won’t have lights, and the tech won’t know what to do.

    **Real-life example:**
    Sarah books a job for Jane, who wants house washing and window washing. Sarah creates two work orders: “Jane Smith - House Washing” and “Jane Smith - Window Washing.” This ensures the right trucks and techs are sent, keeping Jane happy.

    Let’s check your understanding with a quiz!
    """)
    st.markdown("**Quiz: Our Five Divisions**")
    q1 = st.radio("Why must work orders be specific to one division?",
                  ["A. To save time", "B. Each division has its own truck and techs", "C. To increase prices", "D. To skip scheduling"],
                  key="q4_1")
    if st.button("Submit Module 1 Quiz", key="submit_4_1"):
        if q1 == "B. Each division has its own truck and techs":
            st.success("Correct! Separate work orders match our trucks and techs.")
            if "ch4_m1" not in st.session_state.get('completed_modules', []):
                st.session_state.completed_modules = st.session_state.get('completed_modules', []) + ["ch4_m1"]
        else:
            st.error("Not quite. Each division has its own truck and techs. Review Module 1!")

    # Module 2: What Are Work Orders and Why Do They Matter?
    st.subheader("Module 2: What Are Work Orders and Why Do They Matter?")
    st.markdown("""
    Great start! Work orders are job assignments in Markate. They list what to do, where, and when. They’re created after a customer accepts an estimate, like for window washing.

    **Why care?**
    Work orders ensure the services you sell happen. They help schedule techs and keep customers happy. You can answer questions like “When’s my pest control job?”

    **Example:**
    You sell a $300 window washing job to Tom. A work order schedules a tech for Monday. It includes Tom’s address and service details. Tom’s thrilled!

    Try a quick quiz!
    """)
    st.markdown("**Quiz: What Are Work Orders?**")
    q2 = st.radio("What is a work order in Markate?",
                  ["A. A list of leads", "B. A job assignment with details", "C. An email", "D. A sales report"],
                  key="q4_2")
    if st.button("Submit Module 2 Quiz", key="submit_4_2"):
        if q2 == "B. A job assignment with details":
            st.success("Correct! Work orders assign jobs with details.")
            if "ch4_m2" not in st.session_state.get('completed_modules', []):
                st.session_state.completed_modules = st.session_state.get('completed_modules', []) + ["ch4_m2"]
        else:
            st.error("Not quite. Work orders are job assignments. Review Module 2!")

    # Module 3: Navigating Work Orders in Markate
    st.subheader("Module 3: Navigating Work Orders in Markate")
    st.markdown("""
    Nice work! Let’s find work orders in Markate. It’s easy!

    **Steps:**
    1. Log into Markate (stg.markate.com, Username: Markate, Password: crm4you).
    2. Click “Sales” at the top.
    3. Select “Work Orders.”

    **Table View:**
    Choose “Table” view. It shows all work orders. Statuses include:
    - **New:** Unscheduled jobs.
    - **Scheduled:** Jobs with a tech and date.
    - **Completed:** Finished jobs.
    - **Closed:** Paid jobs.

    **Tip:**
    Filter by Job Type (e.g., Pest Control) to see specific jobs.

    **Example:**
    Jake checks “New” in Table View. He sees a house washing job for Mike. He clicks to see Mike’s address and details.

    Test your skills!
    """)
    st.markdown("**Quiz: Navigating Work Orders**")
    q3 = st.radio("How do you access Work Orders in Markate?",
                  ["A. Sales > Customers", "B. Sales > Work Orders", "C. Reports > Work Orders", "D. Leads > New"],
                  key="q4_3")
    if st.button("Submit Module 3 Quiz", key="submit_4_3"):
        if q3 == "B. Sales > Work Orders":
            st.success("Correct! Go to Sales > Work Orders.")
            if "ch4_m3" not in st.session_state.get('completed_modules', []):
                st.session_state.completed_modules = st.session_state.get('completed_modules', []) + ["ch4_m3"]
        else:
            st.error("Not quite. It’s Sales > Work Orders. Review Module 3!")

    # Module 4: Creating a Work Order – Method 1 (From Work Orders Page)
    st.subheader("Module 4: Creating a Work Order – Method 1 (From Work Orders Page)")
    st.markdown("""
    You’re rocking it! Let’s create a work order from the Work Orders page.

    **Steps:**
    1. Go to “Sales” > “Work Orders.”
    2. Click “New Work Order.”
    3. Pick a customer (e.g., John Doe).
    4. Set job location (e.g., John’s home).
    5. Add scope (e.g., “Window Washing”).
    6. Assign a tech.
    7. Schedule (e.g., April 18, 2025).
    8. Choose notification (email or text).
    9. Add details:
       - **Job Type:** E.g., Window Washing.
       - **Job Name:** E.g., “John Doe - Window Washing.”
       - **Job Description:** Public note (e.g., “Clear windows”).
       - **Technician Instructions:** Private note (e.g., “Bring tall ladder”).
    10. Click “Save.”

    **Example:**
    Sarah creates a work order for John’s window washing. She names it “John Doe - Window Washing” and schedules it. John gets a text. The tech gets clear instructions.

    Try a quiz!
    """)
    st.markdown("**Quiz: Creating a Work Order (Method 1)**")
    q4 = st.radio("What’s the correct job name format?",
                  ["A. Window Washing - John Doe", "B. John Doe - Window Washing", "C. Job Type - Customer", "D. John Doe - 2025"],
                  key="q4_4")
    if st.button("Submit Module 4 Quiz", key="submit_4_4"):
        if q4 == "B. John Doe - Window Washing":
            st.success("Correct! Use Customer Name - Job Description.")
            if "ch4_m4" not in st.session_state.get('completed_modules', []):
                st.session_state.completed_modules = st.session_state.get('completed_modules', []) + ["ch4_m4"]
        else:
            st.error("Not quite. It’s Customer Name - Job Description. Review Module 4!")

    # Module 5: Creating a Work Order – Method 2 (From Customer Profile)
    st.subheader("Module 5: Creating a Work Order – Method 2 (From Customer Profile)")
    st.markdown("""
    Awesome! Now, create a work order from a customer’s profile. It’s faster!

    **Steps:**
    1. Go to “Sales” > “Customers.”
    2. Search for a customer (e.g., Jane Smith).
    3. Click their name.
    4. Click “Create Work Order.”
    5. Markate auto-fills customer info.
    6. Add scope (e.g., “Pest Control”).
    7. Assign a tech.
    8. Schedule (e.g., April 18, 2025).
    9. Set notification.
    10. Add details:
        - **Job Type:** E.g., Pest Control.
        - **Job Name:** E.g., “Jane Smith - Pest Control.”
        - **Job Description:** Public note.
        - **Technician Instructions:** Private note.
    11. Click “Save.”

    **Example:**
    Jake’s on Jane’s profile. He creates a pest control work order named “Jane Smith - Pest Control.” It’s fast because Jane’s info is pre-filled.

    Quiz time!
    """)
    st.markdown("**Quiz: Creating a Work Order (Method 2)**")
    q5 = st.radio("Why is Method 2 faster?",
                  ["A. It skips scheduling", "B. Markate pre-fills customer info", "C. No job name needed", "D. Auto-assigns tech"],
                  key="q4_5")
    if st.button("Submit Module 5 Quiz", key="submit_4_5"):
        if q5 == "B. Markate pre-fills customer info":
            st.success("Correct! Pre-filled info saves time.")
            if "ch4_m5" not in st.session_state.get('completed_modules', []):
                st.session_state.completed_modules = st.session_state.get('completed_modules', []) + ["ch4_m5"]
        else:
            st.error("Not quite. Markate pre-fills customer info. Review Module 5!")

    # Module 6: Practice and Tips for Work Orders
    st.subheader("Module 6: Practice and Tips for Work Orders")
    st.markdown("""
    You’re almost a pro! Let’s practice creating work orders for yourself to see what customers see.

    **Practice 1: Method 1 (Work Orders Page):**
    1. Go to “Sales” > “Work Orders.”
    2. Click “New Work Order.”
    3. Select yourself as the customer (from Chapter 1).
    4. Set your address.
    5. Add scope: “Window Washing - Test.”
    6. Assign a tech.
    7. Schedule for April 18, 2025.
    8. Choose email notification.
    9. Set Job Type: Window Washing, Job Name: “Your Name - Window Washing Test,” Job Description: “Test job,” Technician Instructions: “Test—bring small ladder.”
    10. Save and check your email.

    **Practice 2: Method 2 (Customer Profile):**
    1. Go to “Sales” > “Customers.”
    2. Find your profile.
    3. Click “Create Work Order.”
    4. Add scope: “Pest Control - Test.”
    5. Assign a tech.
    6. Schedule for April 18, 2025.
    7. Choose text notification.
    8. Set Job Type: Pest Control, Job Name: “Your Name - Pest Control Test,” Job Description: “Test job,” Technician Instructions: “Test—check sprayer.”
    9. Save and check your phone.

    **Tips:**
    - Use filters to find jobs (e.g., Window Washing).
    - Check “New” status often.
    - Keep Job Descriptions clear for customers.
    - Test notifications to understand customer experience.

    **Example:**
    Lisa creates two test work orders: one for window washing (Method 1) and one for pest control (Method 2). She gets an email and text, seeing how customers are notified.

    Final quiz!
    """)
    st.markdown("**Quiz: Practice and Tips**")
    q6 = st.radio("Why test a work order on your account?",
                  ["A. To do the job", "B. To see customer notifications", "C. To skip scheduling", "D. To change job type"],
                  key="q4_6")
    if st.button("Submit Module 6 Quiz", key="submit_4_6"):
        if q6 == "B. To see customer notifications":
            st.success("Correct! Testing shows what customers see.")
            if "ch4_m6" not in st.session_state.get('completed_modules', []):
                st.session_state.completed_modules = st.session_state.get('completed_modules', []) + ["ch4_m6"]
        else:
            st.error("Not quite. Testing shows notifications. Review Module 6!")

    # Final Quiz
    st.subheader("Chapter 4 Final Quiz")
    st.markdown("Let’s wrap up with a final quiz!")
    final_questions = [
        {"q": "Why create separate work orders for each service?", "opts": ["A. To save time", "B. To match division-specific trucks and techs", "C. To increase prices", "D. To skip notifications"], "ans": 1},
        {"q": "What’s the main purpose of a work order?", "opts": ["A. Track leads", "B. Schedule a job", "C. Send invoice", "D. Create customer"], "ans": 1},
        {"q": "To see unscheduled jobs, which status do you check?", "opts": ["A. Completed", "B. Invoiced", "C. New", "D. Closed"], "ans": 2},
        {"q": "What’s the job name for Tom Brown’s pest control?", "opts": ["A. Pest Control - Tom Brown", "B. Tom Brown - Pest Control", "C. Pest Control - 2025", "D. Tom Brown - Job Type"], "ans": 1},
        {"q": "How do you start a work order from Jane Doe’s profile?", "opts": ["A. Sales > Work Orders", "B. Click 'Create Work Order' on profile", "C. Schedule first", "D. Filter Job Type"], "ans": 1}
    ]
    for i, q in enumerate(final_questions, 1):
        st.markdown(f"**Question {i}: {q['q']}**")
        ans = st.radio("", q["opts"], key=f"final_q{i}")
        if st.button(f"Submit Question {i}", key=f"submit_final_q{i}"):
            if ans == q["opts"][q["ans"]]:
                st.success("Correct!")
            else:
                st.error(f"Not quite. Review the relevant module!")

if __name__ == "__main__":
    display_chapter()
