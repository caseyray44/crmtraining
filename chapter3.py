#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
chapter3.py

This module contains the Chapter 3 training content for the CRM Training App, a 
Streamlit-based training platform for CC Inc. employees learning to use the Markate CRM.
It includes the CH3_MODULES list with modules and tasks, as well as the CH3_FINAL_QUIZ 
list for the final quiz questions. The content, wording, and structure of the training 
material remain unchanged as per the app's requirements.
"""

# -------------------------------------------------------------------
# CHAPTER 3 MODULES & FINAL QUIZ (DETAILED)
# -------------------------------------------------------------------

CH3_MODULES = [
    {
        "title": "Chapter 3, Module 1: Introduction to Estimates in Markate",
        "content": """**Welcome to Chapter 3: Estimates Training!**  
Great job completing Chapters 1 and 2—you’ve learned how to create customers and manage leads in Markate, which are key skills for your role at CC Inc. Now, we’re moving on to Chapter 3, where you’ll learn how to create, send, and manage *estimates* in Markate. Estimates are a big part of how we give customers quotes for our services, and doing this well ensures we can provide great service without confusion or extra work. Don’t worry if you’ve never created an estimate before—I’ll explain everything step-by-step, just like in the previous chapters. Let’s get started!

**What is an Estimate?**  
An estimate is a document you create in Markate to tell a customer how much a service will cost. Think of it like a price tag you show the customer before they decide to buy. For example:  
- If a customer calls and says, “How much will it cost to wash my house?” you’ll create an estimate in Markate that says, “House washing will cost $200.”  
- The customer can then look at the estimate, decide if they want to go ahead, and let you know.

At CC Inc., we use estimates to give customers clear prices for services like house washing, pest control, window washing, painting, or holiday lights. Markate makes this easy by letting you create professional-looking estimates, send them to customers, and keep track of what they decide.

**Why Are Estimates Important at CC Inc.?**  
Estimates are like a promise to the customer—they show them exactly what they’ll pay, so there are no surprises. Here’s why they matter:  
- **They Help Customers Decide**: An estimate gives the customer a clear price, so they can decide if they want to hire CC Inc. For example, if a customer sees that house washing costs $200, they can say yes or no based on their budget.  
- **They Keep Things Organized**: Markate saves all your estimates in one place, so you can look them up later. For example, if a customer calls back and says, “What was that price you quoted me?” you can find their estimate in Markate and tell them.  
- **They Save Time**: Instead of writing prices on paper or guessing, Markate lets you create estimates quickly and send them to the customer with just a few clicks. This means you can focus on helping more customers instead of doing extra paperwork.

**How Do Estimates Fit into Your Role at CC Inc.?**  
As a sales rep at CC Inc., your job is to talk to customers, understand what services they need, and give them a price they can trust. Creating estimates in Markate is a big part of that. You’ll use estimates to:  
- **Give Accurate Quotes**: You’ll create estimates to tell customers how much their services will cost, so they know what to expect. For example, if a customer wants pest control, you’ll make an estimate that says, “Pest control will cost $150.”  
- **Make Customers Happy**: A clear estimate helps the customer feel confident in their decision. If they know the price upfront, they’re more likely to say yes and trust CC Inc. to do a great job.  
- **Turn Leads into Jobs**: In Chapter 2, you learned how to manage leads. When a lead says, “I’m ready for a quote,” you’ll create an estimate in Markate and send it to them. If they accept the estimate, you can turn it into a job for our service teams to handle.

**What’s a Staging Environment (Again)?**  
Just like in Chapters 1 and 2, we’ll practice creating estimates in Markate’s *staging environment*. This is a safe space where you can try things without affecting real customers. For example, if you make a mistake on an estimate (like typing the wrong price), it won’t cause any problems because it’s not real data. You’ll use the same login details as before:  
- Website: https://stg.markate.com/  
- First Login: Username: Markate, Password: crm4you  
- Second Login: Email: support@xecutetech.com, Password: Windows4  

**What’s Next?**  
In this chapter, we’ll learn how to create, send, and manage estimates in Markate. We’ll start by exploring the different types of estimates and how to access the Estimates section. By the end of this chapter, you’ll be able to create professional estimates for customers and help them make decisions about our services. To make sure you understand what estimates are, I’ve prepared a reflection task for you. Let’s do this!""",
        "task_type": "reflection",
        "task": """Reflection: Why do you think it’s important to give customers a clear estimate before starting a job? How do you think creating estimates in Markate will help you as a sales rep at CC Inc.?"""
    },
    {
        "title": "Chapter 3, Module 2: Understanding Estimate Types in Markate",
        "content": """**Let’s Learn About Estimate Types in Markate!**  
Now that you know what estimates are and why they’re important, let’s learn about the different types of estimates you can create in Markate. Markate gives you three options for creating estimates: Standard Estimate, Options Estimate, and Package Estimate. We’ll focus on the first two because they’re the ones we use at CC Inc. I’ll explain each type, how it works, and when to use it, so you can pick the right one for each customer. Let’s get started!

**How to Find the Estimates Section in Markate**  
Before we talk about the types, let’s make sure you know how to find the Estimates section in Markate. Follow these steps carefully:  
1. **Make Sure You’re on the Markate Dashboard**.  
2. **Find the “Sales” Tab** and hover over it.  
3. **Click on “Estimates.”**  
4. **Welcome to the Estimates Section!**  
5. **Click “+ New Estimate.”**

You’ll see three types of estimates: Standard, Options, and Package. Here’s how they differ:
""",
        "task_type": "miniquiz",
        "miniquiz_questions": [
            {
                "question": "Which type of estimate in Markate allows the customer to remove services they don’t want by simply unchecking them?",
                "options": [
                    "Standard Estimate",
                    "Options Estimate",
                    "Package Estimate",
                    "None of the above"
                ],
                "correct_answer": 1
            },
            {
                "question": "Which type of estimate does CC Inc. not use because it bundles services in a single price and can be confusing for customers?",
                "options": [
                    "Standard Estimate",
                    "Options Estimate",
                    "Package Estimate",
                    "All of the above"
                ],
                "correct_answer": 2
            },
            {
                "question": "Scenario: A customer, Ian Johnson, asks for a quote on both pest control and holiday light installation. He’s not sure he wants both services and would like to see separate pricing. Which type of estimate should you create?",
                "options": [
                    "Standard Estimate, because it’s the simplest and forces the customer to accept both services or none.",
                    "Options Estimate, because it allows Ian to pick which services he wants and automatically updates the total.",
                    "Package Estimate, because it bundles the services together under one price."
                ],
                "correct_answer": 1
            }
        ]
    },
    {
        "title": "Chapter 3, Module 3: Creating a Standard Estimate in Markate",
        "content": """**Let’s Create Your First Standard Estimate in Markate!**  
A Standard Estimate is used when the customer wants just one service. This module shows you how to create one.

**Steps**:
1. Go to Sales → Estimates.  
2. Click “+ New Estimate,” choose Standard Estimate.  
3. Select the customer, set job name/location.  
4. Add one line item (the service), including price and description.  
5. Preview and submit.
""",
        "task_type": "miniquiz",
        "miniquiz_questions": [
            {
                "question": "When should you use a Standard Estimate?",
                "options": [
                    "When the customer wants multiple services and needs to choose.",
                    "When the customer wants just one service.",
                    "When the customer wants a bundled package of services."
                ],
                "correct_answer": 1
            },
            {
                "question": "Why is the Description field important in a Standard Estimate?",
                "options": [
                    "It automatically calculates the tax.",
                    "It ensures clarity for you and the customer about what the service includes.",
                    "It lets the customer pick and choose services."
                ],
                "correct_answer": 1
            }
        ]
    },
    {
        "title": "Chapter 3, Module 4: Creating an Options Estimate in Markate",
        "content": """**Let’s Create an Options Estimate!**  
An Options Estimate is used when the customer might want multiple services. Each service is listed with a checkbox, so they can uncheck what they don’t want.

**Steps**:
1. Go to Sales → Estimates.  
2. Click “+ New Estimate” → Options Estimate.  
3. Add 2+ services as line items.  
4. Preview and submit. The customer can pick which ones to accept.
""",
        "task_type": "scenario",
        "task": """
**Scenario**: A customer named Emily Johnson calls and says she only wants a quote for gutter cleaning. What type of estimate should you create for her?  
A) Options Estimate, because it’s the type we use most often.  
B) Standard Estimate, because she only wants one service.  
C) Package Estimate, because it’s a single service.

Select the correct answer and explain why in the box below, thinking about the rules for each estimate type.
""",
        "options": [
            "A) Options Estimate, because it’s the type we use most often.",
            "B) Standard Estimate, because she only wants one service.",
            "C) Package Estimate, because it’s a single service."
        ],
        "correct_answer": 1
    },
    {
        "title": "Chapter 3, Module 5: Managing Estimates in Markate",
        "content": """**Let’s Learn How to Manage Estimates in Markate!**  
After you send an estimate, you can check its status (Submitted, Viewed, Accepted, etc.). If the customer accepts, convert it to a work order or invoice. If they don’t respond, follow up. Don’t let it sit!

**Manage Button Options**:
- Mark as Accepted
- Convert to Work Order
- Convert to Invoice
- Clone
- Archive
- Delete

Check statuses often to stay organized and close more deals.
""",
        "task_type": "reflection",
        "task": """Reflection: Why do you think it’s important to follow up with a customer if they haven’t responded to an estimate? How do you think managing estimates in Markate will help you keep your work organized as a sales rep?"""
    },
    {
        "title": "Chapter 3, Module 6: Final Task – Create Estimates for Yourself",
        "content": """**Let’s Put It All Together: Create Estimates for Yourself!**  
You’ve made it to the final module of Chapter 3—amazing work! You’ve learned how to create Standard and Options Estimates in Markate and how to manage them after sending them to customers. Now, let’s bring it all together with a final task: you’re going to create two estimates for *yourself* in Markate, using the test account you made in Chapter 1. This will help you see the whole process from both the sales rep’s side and the customer’s side. I’ll guide you through every step, as always!

**Task**:
1. Create an Options Estimate (2+ services) for yourself.
2. Create a Standard Estimate (1 service) for yourself.
3. Submit both and imagine seeing them as a customer.

This helps you see the process from start to finish, so you’re fully prepared to do this for real customers.
""",
        "task_type": "reflection",
        "task": """Reflection: After creating your own estimates, what part of the estimate process do you feel most confident about now? How do you think seeing both the sales rep’s side and the customer’s side will help you in your role at CC Inc.?"""
    }
]

CH3_FINAL_QUIZ = [
    {
        "question": "What is the main difference between a Standard Estimate and an Options Estimate?",
        "options": [
            "A Standard Estimate lets customers choose services, while an Options Estimate does not.",
            "An Options Estimate lets customers choose services with checkboxes, while a Standard Estimate does not.",
            "A Standard Estimate is for commercial customers, while an Options Estimate is for residential customers."
        ],
        "answer": 1
    },
    {
        "question": "When should you use an Options Estimate?",
        "options": [
            "When the customer wants just one service.",
            "When the customer wants multiple services and needs to choose which ones they want.",
            "When the customer wants a bundled package with a single price."
        ],
        "answer": 1
    },
    {
        "question": "Why is the Description field important when adding a line item to an estimate?",
        "options": [
            "It automatically calculates the price for the service.",
            "It ensures clarity for both you and the customer about what the service includes.",
            "It lets the customer uncheck the service if they don’t want it."
        ],
        "answer": 1
    },
    {
        "question": "What does the 'Mark as Accepted' option do in the Manage menu?",
        "options": [
            "It deletes the estimate from Markate.",
            "It changes the estimate’s status to Accepted, showing the customer agreed to it.",
            "It sends the estimate to the customer again."
        ],
        "answer": 1
    },
    {
        "question": "What should you do if a customer hasn’t responded to an estimate after a few days?",
        "options": [
            "Delete the estimate and create a new one.",
            "Follow up with the customer to see if they have any questions.",
            "Convert the estimate to a work order right away."
        ],
        "answer": 1
    }
]
