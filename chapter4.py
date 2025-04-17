"""
chapter4.py

This module contains the Chapter 4 training content for the CRM Training App, a 
Streamlit-based training platform for CC Inc. employees learning to use the Markate CRM.
It includes the CH4_MODULES list with modules and tasks, as well as the CH4_FINAL_QUIZ 
list for the final quiz questions.
"""

# -------------------------------------------------------------------
# CHAPTER 4 MODULES & FINAL QUIZ
# -------------------------------------------------------------------

CH4_MODULES = [
    {
        "title": "Chapter 4, Module 1: Our Five Divisions and Why Work Orders Are Division-Specific",
        "content": """
        Welcome, sales rep! Our business has five divisions: House Washing, Pest Control, Window Washing, Painting/Staining, and Holiday Lights. Each division has its own truck and trained technicians. This keeps us organized but means work orders must be specific to one division.

        **Why separate work orders?**
        - Each truck carries tools for one service. A window washing truck can’t do pest control.
        - Technicians are trained for one division. A house washing tech can’t paint.
        - Combining services on one work order causes confusion. For example:
          - If a customer wants window washing and pest control, create two work orders: one for each division. A window washing tech can’t spray for pests!
          - If a work order says “John Doe - House Washing and Holiday Lights,” the house washing truck won’t have lights, and the tech won’t know what to do.

        **Real-life example:**
        The office admin books a job for Jane because James, the customer, requested it. Jane wants house washing and window washing. The admin creates two work orders: “Jane Smith - House Washing” and “Jane Smith - Window Washing.” This ensures the right trucks and techs are sent, keeping Jane happy.

        Let’s check your understanding with a quiz!
        """,
        "task_type": "miniquiz",
        "miniquiz_questions": [
            {
                "question": "Why must work orders be specific to one division?",
                "options": ["A. To save time", "B. Each division has its own truck and techs", "C. To increase prices", "D. To skip scheduling"],
                "correct_answer": 1
            }
        ]
    },
    {
        "title": "Chapter 4, Module 2: What Are Work Orders and Why Do They Matter?",
        "content": """
        Great start! Work orders are job assignments in Markate. In layman’s terms, work orders are things that need to be done—a clear list of tasks to complete. They are jobs that need to be done and sent to production. Work orders list what to do, where, and when. They’re created after a customer accepts an estimate, like for window washing.

        **Why care?**
        Work orders ensure the services you sell happen. They help schedule techs and keep customers happy. You can answer questions like “When’s my pest control job?”

        **Example:**
        You sell a $300 window washing job to Tom. A work order schedules a tech for Monday. It includes Tom’s address and service details. Tom’s thrilled!

        Try a quick quiz!
        """,
        "task_type": "miniquiz",
        "miniquiz_questions": [
            {
                "question": "What is a work order in Markate?",
                "options": ["A. A list of leads", "B. A job assignment with details", "C. An email", "D. A sales report"],
                "correct_answer": 1
            }
        ]
    },
    {
        "title": "Chapter 4, Module 3: Navigating Work Orders in Markate",
        "content": """
        Nice work! Let’s find work orders in Markate. It’s easy!

        **Steps:**
        1. Log into Markate (stg.markate.com, Username: Markate, Password: crm4you).
        2. Hover over “Sales” at the top. A dropdown will appear. Select “Work Orders.” From here, you have two views: Table View or Pipeline. Select Table View—this is preferred when looking at work orders.

        **Table View:**
        From Table View, you can see the stages of work orders:
        - **New:** Unscheduled jobs.
        - **Scheduled:** Jobs with a tech and date assigned.
        - **Completed:** Finished jobs.
        - **Invoiced:** Jobs that are finished and an invoice has been sent out.
        - **Started:** Jobs the technician started but hasn’t finished.
        - **Paused:** Jobs that have been started and paused, meaning we’re not done and need to go back.
        - **Withdrawn:** Jobs that are canceled or changed for some reason.
        - **Closed:** Paid jobs.
        - **Archive:** Jobs that have had no movement for a long time, for various reasons.

        **Tip:**
        Always view the job title to help understand the scope of work (e.g., “Jane Doe - Window Washing”).

        Test your skills!
        """,
        "task_type": "miniquiz",
        "miniquiz_questions": [
            {
                "question": "How do you access Work Orders in Markate?",
                "options": ["A. Sales > Customers", "B. Sales > Work Orders", "C. Reports > Work Orders", "D. Leads > New"],
                "correct_answer": 1
            }
        ]
    },
    {
        "title": "Chapter 4, Module 4: Creating a Work Order – Method 1 (From Work Orders Page)",
        "content": """
        You’re rocking it! Let’s create a work order from the Work Orders page.

        **Steps:**
        1. Go to “Sales” > “Work Orders.”
        2. Click “New Work Order.”
        3. Pick a customer (e.g., John Doe).
        4. Set job location (e.g., John’s home).
        5. Add work order items (e.g., “Window Washing”).
        6. Assign a tech.
        7. Schedule (e.g., April 18, 2025 and time).
        8. Add details:
           - **Job Type:** This is a dropdown bar to select division (e.g., Window Washing).
           - **Job Name (THE IMPORTANT ONE):** It’s very important that the job title on the work order process, in the section titled “Job Name*” (has a small red star next to it), includes the scope of work here. Examples are “John Doe - Window Washing,” “Chris Tucker - House Washing,” “Susie Smith - Pest Control.” The program will auto-fill the customer’s name in this section, but you must always add “- [division]” like in the samples.
           - **Job Description:** Public note (e.g., “wash windows etc”)—usually not needed.
           - **Technician Instructions:** Private note (e.g., “Bring tall ladder,” “large dog on site,” or “Rodent box locations”).
        9. Click “Save.”

        **Example:**
        Office admin creates a work order for John’s window washing. Admin names it “John Doe - Window Washing” and schedules it. John gets a text, and the tech gets clear instructions.

        Try a quiz!
        """,
        "task_type": "miniquiz",
        "miniquiz_questions": [
            {
                "question": "What’s the correct job name format?",
                "options": ["A. Window Washing - John Doe", "B. John Doe - Window Washing", "C. Job Type - Customer", "D. John Doe - 2025"],
                "correct_answer": 1
            },
            {
                "question": "Why is the Job Name field so important?",
                "options": ["A. It sets the price", "B. It defines the scope of work for the division", "C. It schedules the job", "D. It sends the invoice"],
                "correct_answer": 1
            }
        ]
    },
    {
        "title": "Chapter 4, Module 5: Creating a Work Order – Method 2 (From Customer Profile)",
        "content": """
        Awesome! Now, create a work order from a customer’s profile. It’s faster!

        **Steps:**
        1. Go to “Sales” > “Customers.”
        2. Search for a customer (e.g., Jane Smith).
        3. Click their name.
        4. Click “Create Work Order” (first row, big green button).
        5. Markate auto-fills customer info.
        6. Add work order items (e.g., “Pest Control 2x”).
        7. Assign a tech.
        8. Schedule (e.g., April 18, 2025).
        9. Add details:
           - **Job Type:** This is a dropdown bar to select division (e.g., Pest Control).
           - **Job Name (THE IMPORTANT ONE):** It’s very important that the job title on the work order process, in the section titled “Job Name*” (has a small red star next to it), includes the scope of work here. Examples are “John Doe - Window Washing,” “Chris Tucker - House Washing,” “Susie Smith - Pest Control.” The program will auto-fill the customer’s name in this section, but you must always add “- [division]” like in the samples.
           - **Job Description:** Public note (e.g., “wash windows etc”)—usually not needed.
           - **Technician Instructions:** Private note (e.g., “Bring tall ladder,” “large dog on site,” or “Rodent box locations”).
        10. Click “Save.”

        **Example:**
        The admin is on Jane’s profile, creates a pest control work order named “Jane Smith - Pest Control,” and it’s faster because Jane’s info is pre-filled.

        Quiz time!
        """,
        "task_type": "miniquiz",
        "miniquiz_questions": [
            {
                "question": "Why is Method 2 faster?",
                "options": ["A. It skips scheduling", "B. Markate pre-fills customer info", "C. No job name needed", "D. Auto-assigns tech"],
                "correct_answer": 1
            }
        ]
    },
    {
        "title": "Chapter 4, Module 6: Practice and Tips for Work Orders",
        "content": """
        You’re almost a pro! Let’s practice creating work orders for yourself to see what customers see.

        **Practice 1: Method 1 (Work Orders Page):**
        1. Go to “Sales” > “Work Orders.”
        2. Click “New Work Order.”
        3. Select yourself as the customer (from Chapter 1).
        4. Set your address.
        5. Add work order items (e.g., “Window Washing - Test”).
        6. Assign a tech.
        7. Schedule for April 18, 2025.
        8. Add details:
           - **Job Type:** This is a dropdown bar to select division (e.g., Window Washing).
           - **Job Name (THE IMPORTANT ONE):** It’s very important that the job title on the work order process, in the section titled “Job Name*” (has a small red star next to it), includes the scope of work here (e.g., “Your Name - Window Washing Test”).
           - **Job Description:** Public note (e.g., “Test job”)—usually not needed.
           - **Technician Instructions:** Private note (e.g., “Test—bring small ladder”).
        9. Save and check your email.

        **Practice 2: Method 2 (Customer Profile):**
        1. Go to “Sales” > “Customers.”
        2. Find your profile.
        3. Click “Create Work Order” (first row, big green button).
        4. Markate auto-fills your info.
        5. Add work order items (e.g., “Pest Control - Test”).
        6. Assign a tech.
        7. Schedule for April 18, 2025.
        8. Add details:
           - **Job Type:** This is a dropdown bar to select division (e.g., Pest Control).
           - **Job Name (THE IMPORTANT ONE):** It’s very important that the job title on the work order process, in the section titled “Job Name*” (has a small red star next to it), includes the scope of work here (e.g., “Your Name - Pest Control Test”).
           - **Job Description:** Public note (e.g., “Test job”)—usually not needed.
           - **Technician Instructions:** Private note (e.g., “Test—check sprayer”).
        9. Save and check your phone.

        **Tips:**
        - Use job titles to find jobs (e.g., Window Washing or Pest Control).
        - Always check the New status—these are people who want things done, willing to give us money, but aren’t scheduled. They should be scheduled and sent to production. We want the New bucket as low as possible so customers aren’t waiting and wondering when jobs will get done. Once it’s in production, it’s done and in rotation.
        - Keep Job Descriptions clear for customers.
        - Test notifications to understand customer experience.

        Let’s make sure you understand the key points with a quiz!
        """,
        "task_type": "miniquiz",
        "miniquiz_questions": [
            {
                "question": "Why test a work order on your account?",
                "options": ["A. To do the job", "B. To see customer notifications", "C. To skip scheduling", "D. To change job type"],
                "correct_answer": 1
            }
        ]
    }
]

CH4_FINAL_QUIZ = [
    {
        "question": "Why create separate work orders for each service?",
        "options": ["A. To save time", "B. To match division-specific trucks and techs", "C. To increase prices", "D. To skip notifications"],
        "answer": 1
    },
    {
        "question": "What’s the main purpose of a work order?",
        "options": ["A. To track and organize things that need to be done", "B. Schedule a job", "C. Send invoice", "D. Create customer"],
        "answer": 0
    },
    {
        "question": "To see unscheduled jobs, which status do you check?",
        "options": ["A. Completed", "B. Invoiced", "C. New", "D. Closed"],
        "answer": 2
    },
    {
        "question": "What’s the job name for Tom Brown’s pest control?",
        "options": ["A. Pest Control - Tom Brown", "B. Tom Brown - Pest Control", "C. Pest Control - 2025", "D. Tom Brown - Job Type"],
        "answer": 1
    },
    {
        "question": "How do you start a work order from Jane Doe’s profile?",
        "options": ["A. Sales > Work Orders", "B. Click 'Create Work Order' on profile", "C. Schedule first", "D. Filter Job Type"],
        "answer": 1
    },
    {
        "question": "Jane Doe calls and asks if she’s been scheduled for her pest control yet. How can you check that information?",
        "options": [],  # Written answer, no options
        "answer": None,  # Will check for non-empty response
        "is_written": True
    }
]
