#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
chapter2.py

This module contains the Chapter 2 training content for the CRM Training App, a 
Streamlit-based training platform for CC Inc. employees learning to use the Markate CRM.
It includes the CH2_MODULES list with modules and tasks, as well as the CH2_FINAL_QUIZ 
list for the final quiz questions. The content, wording, and structure of the training 
material remain unchanged as per the app's requirements.
"""

################################################################
#            CHAPTER 2 MODULES & FINAL QUIZ (DETAILED)         #
################################################################
CH2_MODULES = [
    {
        "title": "Chapter 2, Module 1: Understanding & Managing Leads in Markate",
        "content": """
**Welcome to Chapter 2: Leads Training!**  
Great job completing Chapter 1—you’ve learned how to create customer accounts in Markate, which is a huge part of your job at CC Inc. Now, we’re moving on to Chapter 2, where you’ll learn about *leads*. Leads are a big part of how CC Inc. finds new customers, and Markate helps us manage them. Don’t worry if you’ve never heard of leads before—I’ll explain everything step-by-step, just like in Chapter 1. Let’s get started!

**What is a Lead?**  
A lead is anyone who has shown interest in CC Inc.’s services. Think of a lead as someone raising their hand and saying, “I might want to buy something from you!” Here are some examples of leads:  
- **A New Customer**: Someone who calls and says, “I need a quote for house washing.” They’re not a customer yet, but they’re interested in our services.  
- **An Existing Customer**: A customer you already created in Chapter 1 (like John Doe) who calls and says, “I want to add holiday lights to my house.” They’re already a customer, but they’re a lead for a new service.  
- **A Quick Meeting**: Someone who says, “I’d like to meet with a sales rep to talk about pest control.” They’re not ready to buy yet, but they’re interested enough to talk.

At CC Inc., every lead starts in a special category called “Leads” in Markate. We don’t make them a customer right away—instead, we move them through different stages to turn them into a customer. This process is called *managing leads*, and it’s a big part of your job as a sales rep.

**Why Are Leads Important at CC Inc.?**  
Leads are like the seeds of our business—they’re the starting point for finding new customers and growing our company. Here’s why leads matter:  
- **They Bring in New Business**: Every new customer starts as a lead. For example, if someone calls and says, “I need a quote for house washing,” that’s a lead, and if you turn them into a customer, CC Inc. gets a new job!  
- **They Help Existing Customers**: Leads aren’t just new people—they can also be existing customers who want more services. For example, if John Doe already had house washing but now wants pest control, that’s a lead for a new service, which means more business for CC Inc.  
- **They Keep Our Pipeline Full**: At CC Inc., we want to always have new leads coming in, so there’s always work for our service teams. If we don’t have leads, we won’t have new customers, and our business won’t grow.

**How Do We Manage Leads in Markate?**  
Markate has a special section called “Leads” where we keep track of all our leads. It’s like a to-do list for people who are interested in our services. In Markate, leads move through different stages as we work with them. We’ll learn about these stages in detail in Module 3, but here’s a quick overview:  
- **New**: This is where all leads start. It’s like a “new leads” bucket that we want to keep full.  
- **Assigned**: When a lead needs a sales rep (like you!) to follow up, we move them here.  
- **Attempted to Contact**: If we try to reach the lead but can’t, we move them here and add notes.  
- **Scheduled**: If we schedule a meeting with the lead, they move here.  
- **Estimation / Waiting for Response**: After we send a quote (an estimate), the lead moves here while they decide.  
- **First Follow-Up**: If they don’t decide right away, we follow up and move them here.  
- **Second Follow-Up**: If they still don’t decide, we follow up one more time and move them here.

By the end of this process, a lead either becomes a customer (yay!) or decides not to buy (and we keep their info for later). Markate helps us manage this process by keeping all our leads organized and showing us what stage they’re in.

- **How Does This Fit into Your Role at CC Inc.?**  
  As a sales rep at CC Inc., your job is to find new customers and keep existing ones happy, and leads are a big part of that. You’ll be responsible for:  
  - **Finding New Leads**: It’s everyone’s job at CC Inc. to bring in new leads, whether it’s through phone calls, website inquiries, referrals, or repeat customers asking for new services. For example, if you meet someone at a community event who says, “I might need my windows washed,” you’ll add them as a new lead in Markate.  
  - **Following Up on Leads**: You’ll contact leads to see if they’re ready to become customers. For example, if a lead says, “I need a quote for pest control,” you’ll schedule a meeting, send them a quote, and follow up to see if they’re ready to book the service.  
  - **Turning Leads into Customers**: Your goal is to move leads through the stages (which we’ll learn about in Module 3) until they become customers. For example, if a lead agrees to a house washing job, you’ll create a customer account for them in Markate (like you learned in Chapter 1) and schedule the service.  
  - **Keeping Leads Moving**: You’ll make sure leads don’t get stuck in one stage for too long. For example, if a lead hasn’t responded to a quote, you’ll follow up to keep the conversation going. This ensures CC Inc. doesn’t miss out on potential business.

By managing leads in Markate, you’re helping CC Inc. grow its customer base and keep our service teams busy. It’s a key part of your role, and Markate makes it easier by keeping everything organized in one place.

**What’s Next?**  
In the next module, we’ll learn how to view leads in Markate using two different views: Pipeline View and Table View. This will help you see where each lead is in the process and decide what to do next. To make sure you understand what leads are, I’ve prepared a reflection task for you. Let’s do this!
""",
        "task_type": "reflection",
        "task": "Reflection: Why do you think it’s important to keep the 'New' leads bucket full at CC Inc.? How do you think managing leads will help you succeed as a sales rep?"
    },
    {
        "title": "Chapter 2, Module 2: Viewing Leads in Markate (Pipeline vs. Table View)",
        "content": """
**Let’s Learn How to View Leads in Markate!**  
Now that you understand what leads are and why they’re important, it’s time to learn how to view them in Markate. Markate gives us two different ways to look at our leads: *Pipeline View* and *Table View*. Each view has its own benefits, and you’ll use both as a sales rep at CC Inc. I’ll explain how to access these views, what they show, and how to use them to manage your leads. Let’s get started!

**What You’ll Do in This Module**  
You’ll learn how to find the Leads section in Markate and explore the two ways to view leads: Pipeline View and Table View. You’ll also think about which view you might prefer for your work as a sales rep. This will help you get comfortable with seeing and organizing leads in Markate, so you can start managing them effectively.

**How to Find the Leads Section in Markate**  
Let’s start by navigating to the Leads section in Markate. Follow these steps carefully:  
1. **Make Sure You’re on the Markate Dashboard**: You should already be logged into Markate’s staging environment (https://stg.markate.com/, Username: Markate, Password: crm4you, then Email: support@xecutetech.com, Password: Windows4). If you’re not, go back to Chapter 1, Module 2, and follow the login steps. You’ll know you’re on the dashboard because you’ll see a menu bar at the top with options like “Sales,” “Leads,” and “Customers.”  
2. **Find the “Sales” Tab**: Look at the top of the screen. You’ll see a menu with options like “Sales,” “Leads,” “Schedule,” and more. Find the one that says “Sales.” You used this in Chapter 1 to get to the Customers page—it’s usually one of the first options on the left.  
3. **Hover Over the “Sales” Tab**: Move your mouse cursor over the word “Sales” (don’t click yet!). A dropdown menu will appear with more options, just like when you found the Customers page.  
4. **Click on “Leads”**: In the dropdown menu, find the option that says “Leads” and click on it.  
   - **What If I Don’t See “Leads”?** If you don’t see “Leads” in the dropdown menu, make sure you’re hovering over “Sales” and not another tab like “Customers.” If you still don’t see it, try refreshing the page by pressing F5 on your keyboard, or log out and log back in.  
5. **Welcome to the Leads Section!**: After clicking “Leads,” you’ll be taken to the Leads section in Markate. This is where you’ll see all the leads we’re working with at CC Inc. (in the staging environment, these will be fake leads for practice). It’s like a to-do list of people who are interested in our services, and you’ll use this section to manage them.

**Understanding Pipeline View**  
When you first get to the Leads section, you’ll see the *Pipeline View* by default. Here’s what it looks like and how it works:  
- **What It Looks Like**: Pipeline View shows your leads in columns, with each column representing a stage in the process (like “New,” “Assigned,” “Scheduled,” etc.). It’s like a big board with sticky notes—each lead is a sticky note, and you can move it from one column to another as you work with them.  
- **How It Works**: Each lead is displayed as a card with basic info, like the lead’s name and what they’re interested in (e.g., “John Doe - House Washing”). You can drag and drop the card to move it from one stage to another. For example, if you schedule a meeting with John Doe, you can drag his card from “New” to “Scheduled.”  
- **Why It’s Useful**: Pipeline View is great for seeing the big picture—it shows you where all your leads are in the process at a glance. For example, you can quickly see how many leads are in the “New” stage (waiting for you to contact them) or how many are in “Waiting for Response” (waiting for the customer to decide). It’s like a visual map of your work, which helps you stay organized and prioritize what to do next.

**Understanding Table View**  
Markate also gives you another way to view leads: *Table View*. Here’s how to switch to it and what it shows:  
- **How to Switch to Table View**: On the Leads page, look for a button or icon near the top that says “Table View” or looks like a grid (it might be next to “Pipeline View”). Click on it to switch from Pipeline View to Table View.  
  - **What If I Can’t Find It?** If you don’t see a “Table View” button, look for a small icon that looks like a table (rows and columns) or a toggle switch. If you still can’t find it, try refreshing the page or ask for help—we’ll make sure you can access it!  
- **What It Looks Like**: Table View shows your leads in a list, like a spreadsheet. Each lead is a row, and there are columns for different details, like the lead’s name, contact info, stage, and more. For example, you might see a row for “John Doe” with columns showing his email, phone number, and current stage (“New”).  
- **How It Works**: You can sort and filter the list to find specific leads. For example, you can sort by stage to see all the “New” leads at the top, or filter to show only leads that are “Waiting for Response.” You can also click on a lead to see more details, like any notes you’ve added.  
- **Why It’s Useful**: Table View is great for digging into details—it lets you sort and filter to find exactly what you’re looking for. For example, if you want to see all the leads that are “Waiting for Response” so you can follow up, Table View makes it easy to filter and find them. It’s like having a searchable list, which helps you focus on specific tasks.

**Pipeline View vs. Table View: Which Should You Use?**  
Both views are useful, and you’ll probably use them both depending on what you’re doing:  
- **Use Pipeline View When**: You want to see the big picture and move leads between stages. For example, if you’re planning your day and want to see how many leads are in each stage, Pipeline View is perfect. It’s also great for dragging leads to a new stage after you take action.  
- **Use Table View When**: You need to find specific leads or sort them in a certain way. For example, if you want to see all the leads that are “Waiting for Response,” Table View makes it easy to filter and find them. It’s also helpful for seeing detailed info without clicking into each lead.

**Why This Matters for You**  
- **Stay Organized**: Both Pipeline View and Table View help you keep track of your leads, so you always know what to do next.  
- **Work Efficiently**: Knowing how to use both views lets you work faster and smarter.  
- **Understand the Process**: Seeing leads in different stages helps you move them along until they become customers.

**How This Fits into Your Role at CC Inc.**  
As a sales rep, you’ll spend a lot of time in the Leads section of Markate, and knowing how to view your leads is the first step to managing them. By using both Pipeline and Table View, you’ll stay organized and focused on the right leads at the right time.

**What’s Next?**  
In the next module, we’ll dive deeper into the 7 stages of managing leads at CC Inc. You’ll learn what each stage means and how to move leads through them. Let’s do this!
""",
        "task_type": "reflection",
        "task": "Reflection: Which view do you think you’ll use more as a sales rep—Pipeline View or Table View—and why? How do you think these views will help you manage your leads at CC Inc.?"
    },
    {
        "title": "Chapter 2, Module 3: The 7 Stages of Leads at CC Inc.",
        "content": """
**Let’s Learn the 7 Stages of Managing Leads!**  
Now that you know how to view leads in Markate using Pipeline View and Table View, it’s time to learn the process we use to manage them at CC Inc. We move leads through 7 stages in Markate, from the moment they show interest to the moment they become a customer (or decide not to). I’ll explain each stage in detail, what you need to do, and why it’s important. Let’s dive in!

**The 7 Stages**  
1. **New**  
2. **Assigned**  
3. **Attempted to Contact**  
4. **Scheduled**  
5. **Estimation / Waiting for Response**  
6. **First Follow-Up**  
7. **Second Follow-Up**

You’ll move a lead from stage to stage as you work with them, adding notes along the way. After the second follow-up, the lead either becomes a customer or you mark them as “No” (but keep their info).
        """,
        "task_type": "miniquiz",
        "miniquiz_questions": [
            {
                "question": "Which of the following is the correct first stage for a new lead in Markate?",
                "options": [
                    "New",
                    "Assigned",
                    "Attempted to Contact"
                ],
                "correct_answer": 0
            },
            {
                "question": "Which stage in Markate indicates a lead needs immediate attention from a sales rep, requiring action within 24 hours?",
                "options": [
                    "New",
                    "Assigned",
                    "Attempted to Contact",
                    "Estimation / Waiting for Response"
                ],
                "correct_answer": 1
            },
            {
                "question": "Which stage should a lead be moved to if you have already attempted contact (e.g., you called them, left a voicemail, but did not reach them) and you still haven’t heard back from them?",
                "options": [
                    "New",
                    "Scheduled",
                    "Attempted to Contact and left notes",
                    "Second Follow-Up"
                ],
                "correct_answer": 2
            }
        ]
    },
    {
        "title": "Chapter 2, Module 4: Creating New Leads (10 Entries)",
        "content": """
**Let’s Start Adding Leads to Markate!**  
Now that you understand the 7 stages of leads, it’s time to start adding new leads to Markate. In this module, you’ll learn how to create a new lead in Markate’s staging environment, which is the first step in filling up that “New” bucket. We’ll practice by adding 10 leads, using fake information.

**What is a New Lead (Again)?**  
- Anyone who shows interest but isn’t a customer yet.
- Could come from a call, website form, referral, or a repeat customer wanting a new service.

**Steps to Create a New Lead**  
1. Click “New Lead.”  
2. Fill out the form (name, phone, email). Use “555-XXXXXXX” for phone.  
3. Set the Lead Label to Hot, Warm, or Cold.  
4. Click “Save.”  
5. The lead appears in “New” stage.

You’ll create 10 new leads to practice.
""",
        "task_type": "miniquiz",
        "miniquiz_questions": [
            {
                "question": "How many new leads should you create in this module?",
                "options": [
                    "5",
                    "10",
                    "15"
                ],
                "correct_answer": 1
            },
            {
                "question": "Which field should you set to 'Hot,' 'Warm,' or 'Cold' when creating a new lead in Markate?",
                "options": [
                    "Customer Type",
                    "Lead Label",
                    "Lead Source",
                    "Comments"
                ],
                "correct_answer": 1
            },
            {
                "question": "Why do we use phone numbers in the format '555-XXXXXXX' when adding a lead in Markate’s staging environment?",
                "options": [
                    "It’s a requirement for real phone numbers in Markate.",
                    "It’s the format Markate uses for all live leads.",
                    "It’s a fake format used specifically for practice in the staging environment.",
                    "It’s required by state regulations for data entry."
                ],
                "correct_answer": 2
            },
            {
                "question": "Which field in the 'New Lead' form is ideal for adding important details like 'Test lead—created for training' or 'Big dog on property'?",
                "options": [
                    "Lead Source",
                    "Comments",
                    "Lead Title",
                    "Contact Name"
                ],
                "correct_answer": 1
            },
            {
                "question": "After you click 'Save' to create a new lead, which stage does it appear in by default?",
                "options": [
                    "Assigned",
                    "Scheduled",
                    "New",
                    "First Follow-Up"
                ],
                "correct_answer": 2
            }
        ]
    },
    {
        "title": "Chapter 2, Module 5: Creating New Opportunities (10 Entries)",
        "content": """
**Let’s Learn About Opportunities in Markate!**  
You’ve done a great job adding new leads to Markate—now it’s time to learn about *opportunities*. A new opportunity is for an existing customer who wants a new service we haven’t priced before. For example, if John Doe already had house washing but now wants pest control, you’d create a new opportunity.

**Steps**:  
1. Click “New Opportunity.”  
2. Link it to the existing customer (John Doe).  
3. Add the new service as the requested item.  
4. Save.  
5. The opportunity appears in the “New” stage, just like a lead.

We’ll practice adding 10 opportunities in the staging environment, each for a different existing customer.
""",
        "task_type": "scenario",
        "task": """
**Scenario**: A customer named Bob had pest control last year. Now he calls and says he wants holiday lights, which we’ve never priced for him before. What should you do?

A) Create a brand-new lead for Bob, since he’s asking for a new service.  
B) Create a new opportunity for Bob, since he’s an existing customer asking for an additional service.  

Select the correct answer and explain why.
""",
        "options": [
            "A) Create a brand-new lead for Bob, since he’s asking for a new service.",
            "B) Create a new opportunity for Bob, since he’s an existing customer asking for an additional service."
        ],
        "correct_answer": 1
    },
    {
        "title": "Chapter 2, Module 6: Assigning Employees & Final Notes",
        "content": """
**Let’s Learn About Assigning Leads & Opportunities!**  
When you create or edit a lead/opportunity, you’ll see a field called “Assign to Employee.” That’s how you decide who is responsible. However, assigning it does *not* automatically move it to the “Assigned” stage in the pipeline—you have to drag it there if it needs immediate attention.

**Final Tips**:
- Don’t let leads get stuck in any stage too long.  
- Always add notes when you call or email a lead.  
- Verify the assigned employee so everyone knows who’s responsible.

Following these tips ensures no lead slips through the cracks.
""",
        "task_type": "reflection",
        "task": "Reflection: Why do you think it’s important to keep leads even if they say ‘No’ after the second follow-up? How do you think this will help CC Inc. in the future?"
    },
    {
        "title": "Chapter 2, Module 7: Final Task – Create Your Own Test Opportunity",
        "content": """
**Let’s Put It All Together!**  
Now that you know how to manage leads and opportunities, let’s do a final practice. Use your test account from Chapter 1 (the one you created for yourself as a customer). Pretend you’re an existing customer who wants a new service. Create a new opportunity for yourself and move it to “Assigned” if it needs immediate action. 

That way, you’ll see the whole process from both sides.
""",
        "task_type": "scenario",
        "task": """
**Scenario**: Bob is an existing customer who wants a new service we haven’t priced for him before. What should you create?

A) A brand-new lead, since it’s a new service.  
B) A new opportunity, since he’s an existing customer.  
C) Nothing—he’s already a customer.

Select the correct answer and explain why in the box below.
""",
        "options": [
            "A) A brand-new lead, since it’s a new service.",
            "B) A new opportunity, since he’s an existing customer.",
            "C) Nothing—he’s already a customer."
        ],
        "correct_answer": 1
    }
]

CH2_FINAL_QUIZ = [
    {
        "question": "Which view in Markate lets you drag leads from stage to stage?",
        "options": [
            "Pipeline View",
            "Table View",
            "Calendar View"
        ],
        "answer": 0
    },
    {
        "question": "After the second follow-up attempt, if a lead says 'No', what do we do with their information?",
        "options": [
            "Delete the lead from Markate.",
            "Keep them in the 'Second Follow-Up' stage and convert them to a customer for future marketing.",
            "Move them back to the 'New' stage to start over."
        ],
        "answer": 1
    },
    {
        "question": "A brand-new potential client calls asking for a quote. What should you create?",
        "options": [
            "A new opportunity, since they’re asking for a quote.",
            "A brand-new lead in the 'New' stage, since they’re not a customer yet.",
            "A customer account, since they’re ready to buy."
        ],
        "answer": 1
    },
    {
        "question": "Bob is an existing customer who wants a new service we haven’t priced for him before. What should you create?",
        "options": [
            "A brand-new lead, since it’s a new service.",
            "A new opportunity, since he’s an existing customer.",
            "Nothing—he’s already a customer, so we don’t need to create anything."
        ],
        "answer": 1
    },
    {
        "question": "Why must we manually move leads to the 'Assigned' stage after assigning an employee?",
        "options": [
            "Markate does it automatically, so we don’t need to.",
            "To keep the Pipeline View accurate and show which leads need immediate action.",
            "We only do that if the lead is older than 30 days."
        ],
        "answer": 1
    }
]
