"""
chapter4.py

Chapter 4: Advanced Sales Process & Pipeline Optimization

This file contains the complete training for Chapter 4, designed to help sales reps master their Markate pipeline. It’s written in a friendly, step-by-step style, just like Chapters 1–3, assuming you’re new to Markate. Each module includes detailed guidance, real-life examples, and quizzes to ensure you understand everything clearly.
"""

CH4_MODULES = [
    {
        "title": "Module 1: Getting to Know Your Pipeline Inside Out",
        "content": (
            "Welcome back, rockstar! You’ve already learned how to create customers, manage leads, and send estimates in Markate. Now, we’re diving deeper to make your pipeline work *for* you. Think of this as leveling up from driving a bike to a race car!\n\n"
            "**What’s this module about?**\n"
            "We’re learning how to analyze your pipeline to spot opportunities and avoid missing deals. Your pipeline has seven buckets: New, Assigned, Attempted to Contact, Scheduled, Estimate Sent, First Follow-Up, and Second Follow-Up. Let’s see what’s happening in each one.\n\n"
            "**Key things to check:**\n"
            "- **How long are leads sitting?** If a lead’s been in 'New' for three days, it’s like leaving a pizza in the oven too long—it’s not getting better! Markate’s reports show you this (we’ll practice finding them).\n"
            "- **Are leads moving forward?** Check how many leads go from 'Scheduled' to 'Estimate Sent.' If it’s low, you might need to tweak your calls.\n"
            "- **How fast is your pipeline?** The quicker a lead goes from 'New' to an accepted estimate, the more deals you close.\n\n"
            "**How to do it in Markate:**\n"
            "1. Log into Markate (https://stg.markate.com, same login as Chapter 1).\n"
            "2. Go to 'Reports' at the top (hover over 'Sales,' then click 'Reports').\n"
            "3. Select 'Pipeline Summary.' You’ll see a chart showing how many leads are in each bucket and how long they’ve been there.\n"
            "4. Look for leads stuck too long (like over 2 days in 'Attempted to Contact') and make a plan to follow up.\n\n"
            "**Real-life example:**\n"
            "Jake noticed a lead, Maria, was stuck in 'Attempted to Contact' for a week. He checked the Pipeline Summary and saw he’d called her at 7 PM. He tried again at 10 AM, left a voicemail, and added a note: 'Called 10 AM, left message.' Maria called back that afternoon and scheduled a meeting!\n\n"
            "Don’t worry if reports sound new—we’ll practice this together in the quiz. Ready to check your pipeline like a pro?"
        ),
        "task_type": "miniquiz",
        "miniquiz_questions": [
            {
                "question": "What does the 'Pipeline Summary' report show you in Markate?",
                "options": [
                    "A. Your favorite leads’ birthdays",
                    "B. How many leads are in each bucket and how long they’ve been there",
                    "C. Only the total number of customers",
                    "D. The weather forecast"
                ],
                "correct_answer": 1
            },
            {
                "question": "If a lead’s been in 'New' for three days, what should you do?",
                "options": [
                    "A. Ignore it—it’ll move eventually",
                    "B. Assign it to yourself and contact them",
                    "C. Delete it to clean your pipeline",
                    "D. Wait another week"
                ],
                "correct_answer": 1
            }
        ]
    },
    {
        "title": "Module 2: Planning Your Day Like a Superstar",
        "content": (
            "You’re killing it! Now, let’s make your day super productive so you can talk to more leads and close more deals.\n\n"
            "**What’s this module about?**\n"
            "It’s about setting up a daily routine that keeps your pipeline moving. A good plan is like a roadmap—it gets you to your destination faster!\n\n"
            "**Your daily game plan:**\n"
            "1. **Start with Markate:** Log in first thing (you know the drill: https://stg.markate.com, Username: Markate, Password: crm4you, then Email: support@xecutetech.com, Password: Windows4).\n"
            "2. **Check your buckets:** Look at 'New' and 'Assigned' first. These are your hottest leads!\n"
            "3. **Make a to-do list:** Write down who to call. Example: 'Call Sarah at 9 AM, follow up with Tom at 2 PM.'\n"
            "4. **Time it right:** Call new leads in the morning (they’re fresher), and save follow-ups for the afternoon.\n"
            "5. **Clean up:** If you see two leads for 'John Smith,' merge them in Markate (click 'Customers,' find the duplicate, and hit 'Merge').\n\n"
            "**How to merge duplicates in Markate:**\n"
            "- Go to 'Sales' > 'Customers.'\n"
            "- Search for the lead’s name (e.g., 'John Smith').\n"
            "- If you see two entries, click the one you want to keep, then 'Merge,' and select the duplicate to combine.\n"
            "- Double-check the info (like email and phone) to make sure it’s correct.\n\n"
            "**Real-life example:**\n"
            "Lisa starts her day at 8 AM by checking Markate. She sees three new leads in 'Assigned.' She calls one at 9 AM, schedules a meeting, and moves them to 'Scheduled.' By noon, she’s merged a duplicate lead and followed up with two others. That’s a morning well spent!\n\n"
            "Let’s practice planning your day with the quiz below!"
        ),
        "task_type": "miniquiz",
        "miniquiz_questions": [
            {
                "question": "What’s the first bucket you should check each morning?",
                "options": [
                    "A. Follow-Up Two",
                    "B. New or Assigned",
                    "C. Estimate Sent",
                    "D. There’s no need to check"
                ],
                "correct_answer": 1
            },
            {
                "question": "Why merge duplicate leads in Markate?",
                "options": [
                    "A. To make your pipeline look bigger",
                    "B. To avoid calling the same person twice",
                    "C. To create new leads",
                    "D. To reset the pipeline"
                ],
                "correct_answer": 1
            }
        ]
    },
    {
        "title": "Module 3: Talking to Leads with Confidence",
        "content": (
            "You’re on fire! This module is all about making your calls and emails so good that leads can’t wait to say yes to your estimates.\n\n"
            "**What’s this module about?**\n"
            "We’re learning how to follow up with leads in a friendly, clear way and handle their questions like a pro. It’s like having a great chat with a friend!\n\n"
            "**Steps for awesome follow-ups:**\n"
            "1. **Make it personal:** Use their name and mention your last talk. Example: 'Hi Tom, it was great chatting about your cabin last week!'\n"
            "2. **Spell out the next step:** Say what’s happening, like 'I sent your window washing estimate—want to go over it Monday?'\n"
            "3. **Remind them of the deal:** Repeat the key points, like 'It’s $150 for all exterior windows, just like we discussed.'\n"
            "4. **Send it right:** In Markate, go to 'Leads,' find their name, click 'Email,' and type your message. Double-check 'Both Email & Text' is selected in their profile (you learned this in Chapter 1!).\n\n"
            "**Handling tough questions:**\n"
            "- If they say, 'It’s too expensive,' try: 'I hear you, Tom! Our price includes a deep clean that lasts longer—most customers love the results. Can I answer any questions about it?'\n"
            "- If they’re unsure, say: 'No rush! Want to talk about what’s best for your schedule?'\n"
            "- Practice these with a coworker—it’s like a rehearsal for the real thing.\n\n"
            "**Real-life example:**\n"
            "Sarah had a lead, Mike, in 'Estimate Sent.' He emailed back, 'Seems pricey.' Sarah replied, 'Hi Mike, I get it! This covers all 20 windows plus a free check-up to keep them sparkling. Want to discuss?' Mike called back, asked a few questions, and accepted the estimate!\n\n"
            "Ready to practice your follow-up skills? Let’s try the quiz!"
        ),
        "task_type": "miniquiz",
        "miniquiz_questions": [
            {
                "question": "What’s a good way to start a follow-up email?",
                "options": [
                    "A. 'To whom it may concern'",
                    "B. 'Hi [Name], loved our last chat about your [detail]!'",
                    "C. 'Here’s your bill'",
                    "D. 'Call me back now'"
                ],
                "correct_answer": 1
            },
            {
                "question": "If a lead says the price is too high, you should:",
                "options": [
                    "A. Hang up",
                    "B. Explain the value and offer to answer questions",
                    "C. Agree and cut the price",
                    "D. Ignore their concern"
                ],
                "correct_answer": 1
            }
        ]
    },
    {
        "title": "Module 4: Using Markate’s Tools to Shine",
        "content": (
            "You’re almost a pipeline master! Let’s explore some of Markate’s advanced tools to make your job easier and your deals faster.\n\n"
            "**What’s this module about?**\n"
            "We’re learning how to use Markate’s dashboard, tags, and alerts to stay on top of your leads. These tools are like having a personal assistant!\n\n"
            "**Cool tools to use:**\n"
            "- **Custom Dashboard:** Set it to show only 'hot' leads or leads stuck in 'Attempted to Contact.' Go to 'Settings' > 'Dashboard,' and pick 'Show Hot Leads Only.'\n"
            "- **Tags:** Add labels like 'Urgent' or 'Big Job.' In 'Leads,' click a lead, then 'Add Tag,' and type your label.\n"
            "- **Alerts:** Link Markate to your email for reminders. Go to 'Settings' > 'Notifications,' and turn on 'Email Alerts' for follow-ups.\n"
            "- **Reports:** Check 'Sales' > 'Reports' > 'Lead Activity' to see who you haven’t called lately.\n\n"
            "**How to set a tag in Markate:**\n"
            "1. Go to 'Sales' > 'Leads.'\n"
            "2. Click a lead’s name (e.g., 'Jane Doe').\n"
            "3. Click 'Add Tag' and type something like 'Hot Lead.'\n"
            "4. Save it—now you’ll see that tag on your dashboard!\n\n"
            "**Real-life example:**\n"
            "Damon tagged a lead 'Rush Job' because they needed a quote fast. His dashboard showed only 'Rush Job' leads, so he called them first, sent an estimate, and closed the deal in a day! He also set an alert for another lead’s follow-up, so he never forgot.\n\n"
            "Let’s practice using one of these tools in the quiz below!"
        ),
        "task_type": "miniquiz",
        "miniquiz_questions": [
            {
                "question": "What does a custom dashboard let you do?",
                "options": [
                    "A. Delete all your leads",
                    "B. Show only the leads you want, like 'hot' ones",
                    "C. Change Markate’s colors",
                    "D. Stop all notifications"
                ],
                "correct_answer": 1
            },
            {
                "question": "How do you add a tag to a lead in Markate?",
                "options": [
                    "A. Go to 'Leads,' click the lead, and select 'Add Tag'",
                    "B. Call the lead and ask them",
                    "C. Delete the lead first",
                    "D. Tags add themselves"
                ],
                "correct_answer": 0
            }
        ]
    },
    {
        "title": "Module 5: Practicing to Be the Best",
        "content": (
            "You’re so close to being a sales superstar! This module is about practicing everything you’ve learned so it feels like second nature.\n\n"
            "**What’s this module about?**\n"
            "We’re doing hands-on exercises to make sure you’re ready for real leads, plus sharing tips with your team to get even better.\n\n"
            "**Ways to practice:**\n"
            "1. **Try a fake lead:** In Markate’s staging environment, move a test lead through all buckets. Add notes like 'Called at 10 AM, scheduled for tomorrow.'\n"
            "2. **Play pretend:** With a coworker, pretend you’re calling a lead. They say, 'I’m not sure about this price.' You reply, 'I get it! Let’s talk about why it’s a great deal.'\n"
            "3. **Team up:** Meet with your team weekly to share tricks. Maybe someone found that calling at 5 PM works best—try it out!\n\n"
            "**How to practice a lead in Markate:**\n"
            "- Go to 'Sales' > 'Leads.'\n"
            "- Click '+ New Lead,' name it 'Test Lead,' and add fake details (email: test@example.com, phone: 555-123-4567).\n"
            "- Move it from 'New' to 'Assigned,' then 'Scheduled,' and so on, adding notes each time.\n"
            "- Check your work in the 'Pipeline Summary' report.\n\n"
            "**Real-life example:**\n"
            "Tom practiced a fake lead in Markate and realized he forgot to add notes sometimes. During a team meeting, Lisa shared that she tags leads 'Evening Call' for better responses. Tom tried it, and his next lead accepted an estimate faster!\n\n"
            "Let’s wrap up with a quiz to practice what you’ve learned!"
        ),
        "task_type": "miniquiz",
        "miniquiz_questions": [
            {
                "question": "What’s one way to practice in Markate?",
                "options": [
                    "A. Delete all test leads",
                    "B. Move a fake lead through the pipeline",
                    "C. Skip team meetings",
                    "D. Avoid adding notes"
                ],
                "correct_answer": 1
            },
            {
                "question": "Why share tips with your team?",
                "options": [
                    "A. To keep your best ideas secret",
                    "B. To learn new ways to close deals",
                    "C. To make more work for everyone",
                    "D. To reset Markate"
                ],
                "correct_answer": 1
            }
        ]
    }
]

CH4_FINAL_QUIZ = [
    {
        "question": "You see a lead’s been in 'Attempted to Contact' for four days. What do you do?",
        "options": [
            "A. Move it to 'Estimate Sent' without calling",
            "B. Check your notes and try contacting them at a better time",
            "C. Delete the lead to clean up",
            "D. Wait another four days"
        ],
        "answer": 1
    },
    {
        "question": "A lead emails, 'Your price seems high.' How do you reply?",
        "options": [
            "A. 'Sorry, that’s the price!'",
            "B. 'I understand! Our service includes a thorough clean that saves you time. Can we chat about it?'",
            "C. Ignore the email",
            "D. Lower the price immediately"
        ],
        "answer": 1
    },
    {
        "question": "Your dashboard shows 15 leads in 'Estimate Sent.' What tool helps you focus on the best ones?",
        "options": [
            "A. A custom filter for 'hot' leads",
            "B. Closing Markate",
            "C. Calling all 15 at once",
            "D. Removing all tags"
        ],
        "answer": 0
    },
    {
        "question": "In a practice call, your coworker says, 'I’m not ready yet.' What’s a good response?",
        "options": [
            "A. 'You have to decide now!'",
            "B. 'No problem! Can I ask what’s on your mind so we can find the right time?'",
            "C. 'I’ll call someone else.'",
            "D. Say nothing and end the call"
        ],
        "answer": 1
    },
    {
        "question": "Your team suggests texting leads in the evening works well. What’s your next step?",
        "options": [
            "A. Text all leads at midnight",
            "B. Try texting in the evening and track if it helps",
            "C. Stop texting entirely",
            "D. Delete the team’s suggestion"
        ],
        "answer": 1
    }
]
