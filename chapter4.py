"""
chapter4.py

Chapter 4: Understanding Work Orders in Markate

This file is your guide to mastering work orders in Markate, perfect for sales reps learning the ropes. We’ll walk you through what work orders are, how to navigate them, and how to create them two different ways. Each module includes examples and quizzes to make sure you’ve got it down!
"""

CH4_MODULES = [
    {
        "title": "Module 1: What Are Work Orders and Why Do They Matter?",
        "content": (
            "Hey there, awesome sales rep! You’ve learned a lot about Markate so far, and now we’re diving into something super important: work orders. Let’s break it down.\n\n"
            "**What’s this module about?**\n"
            "We’re starting with the basics—what a work order is, why it’s a big deal, and how it fits into your sales role.\n\n"
            "**So, what’s a work order?**\n"
            "A work order is like a to-do list for a specific job that needs to get done for a customer. It tells the team what work to do, where to do it, and when. In Markate, work orders are created after a customer agrees to a service—like window washing or pest control—and they help schedule technicians to get the job done.\n\n"
            "**Why should you care?**\n"
            "Even though you’re a sales rep and might not schedule work orders every day, understanding them helps you see the big picture. Work orders make sure the services you sell actually happen, keeping customers happy. Plus, knowing how they work can help you answer customer questions, like 'When will my windows be cleaned?' You’re part of the team that keeps things running smoothly!\n\n"
            "**Real-life example:**\n"
            "You sold a $300 window washing job to Sarah. After she accepts your estimate, a work order is created in Markate to schedule a technician to her house on Monday. The work order includes all the details—Sarah’s address, the service, and the date—so the job gets done right. Sarah’s thrilled, and you look like a rockstar!\n\n"
            "Let’s make sure you’ve got the basics with a quick quiz!"
        ),
        "task_type": "miniquiz",
        "miniquiz_questions": [
            {
                "question": "What is a work order in Markate?",
                "options": [
                    "A. A list of all your leads",
                    "B. A job assignment with details like what, where, and when",
                    "C. An email to a customer",
                    "D. A report of your sales"
                ],
                "correct_answer": 1
            },
            {
                "question": "Why is it helpful for sales reps to understand work orders?",
                "options": [
                    "A. So they can do the technician’s job",
                    "B. To answer customer questions and ensure services happen",
                    "C. To create more leads",
                    "D. To skip scheduling"
                ],
                "correct_answer": 1
            }
        ]
    },
    {
        "title": "Module 2: Navigating Work Orders in Markate",
        "content": (
            "Great job on the basics! Now, let’s explore how to find and understand work orders in Markate. Don’t worry—it’s easier than it sounds!\n\n"
            "**What’s this module about?**\n"
            "We’re learning how to access work orders in Markate and what the different views and statuses mean, so you can see what’s happening with all the jobs.\n\n"
            "**How to find work orders:**\n"
            "1. Log into Markate (https://stg.markate.com, Username: Markate, Password: crm4you, Email: support@xecutetech.com, Password: Windows4).\n"
            "2. Hover over 'Sales' at the top.\n"
            "3. Click 'Work Orders' from the dropdown menu.\n\n"
            "**Choosing your view:**\n"
            "Once you’re on the Work Orders page, you’ll see two view options at the top left: 'Table' and 'Pipeline.' We’re focusing on Table View because it’s easier to see everything at once. Click 'Table' to select it.\n\n"
            "**Understanding statuses in Table View:**\n"
            "Table View shows all work orders in a list, with different categories you can click on:\n"
            "- **All Work Orders:** Every work order created, no matter the status.\n"
            "- **New:** Jobs that haven’t been scheduled yet—these need attention!\n"
            "- **Scheduled:** Jobs with a set date and technician.\n"
            "- **Started:** Jobs the technician has begun.\n"
            "- **Paused:** Jobs on hold (maybe the customer wasn’t home).\n"
            "- **Completed:** Jobs finished but not yet invoiced.\n"
            "- **Invoiced:** Jobs billed to the customer.\n"
            "- **Withdrawn:** Jobs canceled before starting.\n"
            "- **Closed:** Jobs fully done and paid.\n"
            "- **Archive:** Old or irrelevant work orders.\n\n"
            "**Extra tip:**\n"
            "You can also filter by 'Job Type' (like window washing or pest control) to see only certain kinds of jobs. Feel free to click around and explore—you won’t break anything!\n\n"
            "**Real-life example:**\n"
            "Jake checks the Work Orders page and clicks 'New' in Table View. He sees 10 jobs waiting to be scheduled, including a pest control job for Mike. He clicks it to see the details: Mike’s address and the scope of work. Now Jake knows it’s ready for the office admin to schedule!\n\n"
            "Let’s test your navigation skills with a quiz!"
        ),
        "task_type": "miniquiz",
        "miniquiz_questions": [
            {
                "question": "How do you access the Work Orders page in Markate?",
                "options": [
                    "A. Sales > Customers",
                    "B. Sales > Work Orders",
                    "C. Reports > Work Orders",
                    "D. Leads > New"
                ],
                "correct_answer": 1
            },
            {
                "question": "What does the 'New' status mean in Table View?",
                "options": [
                    "A. Jobs that are finished",
                    "B. Jobs that haven’t been scheduled yet",
                    "C. Jobs that are paused",
                    "D. Jobs that are invoiced"
                ],
                "correct_answer": 1
            }
        ]
    },
    {
        "title": "Module 3: Creating a Work Order – Method 1 (From Work Orders Page)",
        "content": (
            "You’re doing awesome! Now, let’s learn how to create a work order in Markate using the first method—straight from the Work Orders page.\n\n"
            "**What’s this module about?**\n"
            "We’re walking through the steps to create a work order from scratch, making sure every detail is perfect for the technician and customer.\n\n"
            "**Steps to create a work order (Method 1):**\n"
            "1. **Go to Work Orders:** Hover over 'Sales' > 'Work Orders.'\n"
            "2. **Start a new work order:** On the top right, click 'New Work Order.'\n"
            "3. **Select a customer:** Type the customer’s name (e.g., 'John Doe') or pick from the list.\n"
            "4. **Choose job location:** Pick their billing address or another service address—this is where the technician will go.\n"
            "5. **Add work order items:** This is the scope of work—type what the job is (e.g., 'Window Washing - Exterior Only').\n"
            "6. **Assign an employee:** Scroll down and pick a technician to do the job.\n"
            "7. **Schedule it:** Set the start and end date. Most of our jobs start and finish on the same day (e.g., April 20, 2025).\n"
            "8. **Set customer notification:** Choose how to notify the customer (e.g., email or text) and when (e.g., 24 hours before the job).\n"
            "9. **Add job details:**\n"
            "   - **Date Issued:** This auto-fills as today’s date for reference.\n"
            "   - **Job Type:** Pick the type (e.g., Window Washing, Pest Control)—this helps the office know who to assign.\n"
            "   - **Job Name:** Always use the format 'Customer Name - Job Description' (e.g., 'John Doe - Window Washing'). This shows up on the calendar and notifications.\n"
            "   - **Job Description:** Add public notes the customer can see (e.g., 'Please ensure windows are accessible').\n"
            "   - **Technician Instructions:** Add private notes just for the technician (e.g., 'Bring extra ladders—tall windows').\n"
            "10. **Save it:** Click 'Save' to create the work order—it’ll now show up in Table View under 'New' until it’s scheduled.\n\n"
            "**Real-life example:**\n"
            "Sarah creates a work order for John Doe from the Work Orders page. She selects John, sets the job location as his home address, adds 'Window Washing' as the scope, and assigns it to a technician for April 20, 2025. She names it 'John Doe - Window Washing,' adds a note for John to clear the window area, and a private note for the technician to bring a specific cleaner. John gets a text notification, and the job is ready to go!\n\n"
            "Let’s see if you’ve got the steps down with a quiz!"
        ),
        "task_type": "miniquiz",
        "miniquiz_questions": [
            {
                "question": "What’s the correct format for a job name in Markate?",
                "options": [
                    "A. Window Washing - John Doe",
                    "B. John Doe - Window Washing",
                    "C. Job Type - Customer Name",
                    "D. John Doe - 2025"
                ],
                "correct_answer": 1
            },
            {
                "question": "Who can see the Technician Instructions on a work order?",
                "options": [
                    "A. The customer",
                    "B. Only the technician",
                    "C. Everyone",
                    "D. The sales rep only"
                ],
                "correct_answer": 1
            }
        ]
    },
    {
        "title": "Module 4: Creating a Work Order – Method 2 (From Customer Profile)",
        "content": (
            "You’re a pro at creating work orders one way—now let’s try a faster method! This one’s a game-changer when you’re already looking at a customer’s info.\n\n"
            "**What’s this module about?**\n"
            "We’re learning a second way to create a work order in Markate, starting from the customer’s profile, which saves you time.\n\n"
            "**Steps to create a work order (Method 2):**\n"
            "1. **Find the customer:** Hover over 'Sales' > 'Customers.'\n"
            "2. **Search for them:** Type the customer’s name (e.g., 'Jane Smith') or scroll to find them, then click their name to open their profile.\n"
            "3. **Create a work order:** At the top of their profile, you’ll see a 'Work Orders' section. Click 'Create Work Order.'\n"
            "4. **Fill in the details:** Markate will auto-fill the customer’s name and info—nice, right? Now, just like Method 1:\n"
            "   - **Job Location:** Confirm or change the address.\n"
            "   - **Work Order Items:** Add the scope (e.g., 'Pest Control - 2x Treatment').\n"
            "   - **Assign Employee:** Pick a technician.\n"
            "   - **Schedule:** Set the start and end date (e.g., April 22, 2025).\n"
            "   - **Customer Notification:** Choose how to notify Jane.\n"
            "   - **Job Details:** Add Job Type (e.g., Pest Control), Job Name (e.g., 'Jane Smith - Pest Control 2x'), Job Description, and Technician Instructions.\n"
            "5. **Save it:** Click 'Save'—it’ll show up in the Work Orders page under 'New.'\n\n"
            "**Why this method rocks:**\n"
            "This way is faster because you’re already on the customer’s profile, so Markate pre-fills their info. It’s perfect when you’re following up with a customer and want to set up a job right away!\n\n"
            "**Real-life example:**\n"
            "Jake is checking Jane Smith’s profile after she calls to ask about pest control. Right there, he clicks 'Create Work Order,' adds the details for a $200 job, names it 'Jane Smith - Pest Control 2x,' and schedules it for April 22, 2025. Jane gets a notification, and Jake saved a few clicks by not starting from the Work Orders page!\n\n"
            "Let’s test this method with a quiz!"
        ),
        "task_type": "miniquiz",
        "miniquiz_questions": [
            {
                "question": "What’s the first step to create a work order from a customer’s profile?",
                "options": [
                    "A. Go to Sales > Work Orders",
                    "B. Go to Sales > Customers",
                    "C. Go to Reports > Customers",
                    "D. Go to Leads > New"
                ],
                "correct_answer": 1
            },
            {
                "question": "Why is Method 2 faster for creating a work order?",
                "options": [
                    "A. It skips scheduling",
                    "B. Markate pre-fills the customer’s info",
                    "C. It doesn’t need a job name",
                    "D. It auto-assigns a technician"
                ],
                "correct_answer": 1
            }
        ]
    },
    {
        "title": "Module 5: Practice and Tips for Work Orders",
        "content": (
            "You’re almost a work order expert! Let’s wrap up by practicing what you’ve learned and sharing some handy tips to make your life easier.\n\n"
            "**What’s this module about?**\n"
            "We’re putting your skills to the test by creating a work order for yourself, plus giving you tips to use work orders like a pro.\n\n"
            "**Practice time! Create a work order for yourself:**\n"
            "1. Use Method 2 (it’s faster!): Go to 'Sales' > 'Customers,' search for your own name (you should have an account from earlier chapters), and click your profile.\n"
            "2. Click 'Create Work Order.'\n"
            "3. Fill it out:\n"
            "   - **Job Location:** Use your own address.\n"
            "   - **Work Order Items:** Add something simple, like 'Window Washing - Test Job.'\n"
            "   - **Assign Employee:** Pick a technician (or yourself if you’re listed).\n"
            "   - **Schedule:** Set it for tomorrow (e.g., April 16, 2025).\n"
            "   - **Customer Notification:** Choose email or text to see what the customer gets.\n"
            "   - **Job Details:** Name it 'Your Name - Window Washing Test,' set Job Type as Window Washing, add a Job Description ('Test job for training'), and Technician Instructions ('This is a test—bring a small ladder').\n"
            "4. Save it and check your email or phone for the notification—now you know what customers see!\n\n"
            "**Pro tips for work orders:**\n"
            "- **Use filters:** On the Work Orders page, filter by Job Type to quickly find all pest control jobs, for example.\n"
            "- **Check statuses often:** Keep an eye on 'New' work orders to see what needs scheduling, so jobs don’t get delayed.\n"
            "- **Be clear in notes:** Make Job Descriptions customer-friendly (e.g., 'Please move patio furniture') and Technician Instructions specific (e.g., 'Use eco-friendly cleaner').\n"
            "- **Double-check notifications:** Always test notifications on your own account to understand the customer experience.\n\n"
            "**Real-life example:**\n"
            "Lisa created a test work order for herself and set a notification for 24 hours before the job. She got a text saying 'Lisa - Window Washing Test scheduled for April 16, 2025,' and realized how helpful it is for customers to get a heads-up. She also used the Job Type filter to find all window washing jobs, making her follow-ups easier!\n\n"
            "Let’s finish with a quiz to see how you’ll use work orders!"
        ),
        "task_type": "miniquiz",
        "miniquiz_questions": [
            {
                "question": "Why should you test a work order on your own account?",
                "options": [
                    "A. To do the job yourself",
                    "B. To see the customer notification experience",
                    "C. To skip scheduling",
                    "D. To change the job type"
                ],
                "correct_answer": 1
            },
            {
                "question": "What’s a good tip for managing work orders in Markate?",
                "options": [
                    "A. Ignore the 'New' status",
                    "B. Use filters to find specific job types",
                    "C. Skip technician instructions",
                    "D. Don’t set notifications"
                ],
                "correct_answer": 1
            }
        ]
    }
]

CH4_FINAL_QUIZ = [
    {
        "question": "What’s the main purpose of a work order in Markate?",
        "options": [
            "A. To track your sales leads",
            "B. To schedule and detail a job for a customer",
            "C. To send an invoice",
            "D. To create a new customer"
        ],
        "answer": 1
    },
    {
        "question": "You’re on the Work Orders page and want to see unscheduled jobs. What status do you click?",
        "options": [
            "A. Completed",
            "B. Invoiced",
            "C. New",
            "D. Closed"
        ],
        "answer": 2
    },
    {
        "question": "You’re creating a work order for Tom Brown for pest control. What should the Job Name be?",
        "options": [
            "A. Pest Control - Tom Brown",
            "B. Tom Brown - Pest Control",
            "C. Pest Control - 2025",
            "D. Tom Brown - Job Type"
        ],
        "answer": 1
    },
    {
        "question": "You’re on Jane Doe’s profile and want to create a work order. What’s your first step?",
        "options": [
            "A. Go to Sales > Work Orders",
            "B. Click 'Create Work Order' on her profile",
            "C. Schedule the job first",
            "D. Filter by Job Type"
        ],
        "answer": 1
    },
    {
        "question": "You created a work order and want to see what the customer sees. What should you do?",
        "options": [
            "A. Delete the work order",
            "B. Create a test work order for yourself and check the notification",
            "C. Ignore the notification settings",
            "D. Ask the technician"
        ],
        "answer": 1
    }
]
