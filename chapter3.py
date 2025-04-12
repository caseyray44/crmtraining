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
        "content": """
**Welcome to Chapter 3: Estimates Training!**  
Great job completing Chapters 1 and 2—you’ve learned how to create customer accounts and manage leads in Markate, which are key skills for your role at CC Inc. Now, we’re moving on to Chapter 3, where you’ll learn how to create, send, and manage *estimates* in Markate. Estimates are a big part of how we give customers quotes for our services, and doing this well ensures we can provide great service without confusion or extra work. Don’t worry if you’ve never created an estimate before—I’ll explain everything step-by-step, just like in the previous chapters. Let’s get started!

**What is an Estimate?**  
An estimate is a document you create in Markate to tell a customer how much a service will cost. Think of it like a price tag you show the customer before they decide to buy.

At CC Inc., we use estimates to give customers clear prices for services like house washing, pest control, window washing, painting, or holiday lights. Markate makes this easy by letting you create professional-looking estimates, send them to customers, and keep track of what they decide.

**Why Are Estimates Important at CC Inc.?**  
- They help customers decide.  
- They keep things organized in Markate.  
- They save time by letting you quickly send quotes.

**How Do Estimates Fit into Your Role?**  
You’ll create estimates for customers who ask, “How much does this cost?” or for leads who say, “I’m ready for a quote.” Once they accept, you convert it into a job. That’s how you bring revenue to CC Inc. Let’s dive in!
        """,
        "task_type": "reflection",
        "task": "Reflection: Why do you think it’s important to give customers a clear estimate before starting a job? How do you think creating estimates in Markate will help you as a sales rep at CC Inc.?"
    },
    {
        "title": "Chapter 3, Module 2: Understanding Estimate Types in Markate",
        "content": """
**What Types of Estimates Does Markate Offer?**  
Markate provides three types: Standard Estimate, Options Estimate, and Package Estimate. CC Inc. mostly uses Standard and Options.

- **Standard Estimate**: For quoting a single service. Customer can only accept or reject as a whole.  
- **Options Estimate**: For quoting multiple services. Each service can be checked or unchecked.  
- **Package Estimate**: Bundles services into one price (CC Inc. does not use this).

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
        "content": """
**Let’s Create Your First Standard Estimate in Markate!**  
A Standard Estimate is used when the customer wants just one service.

**Steps**:
1. Go to Sales → Estimates.
2. Click “+ New Estimate” and choose Standard Estimate.
3. Select the customer, set job name/location.
4. Add one line item (the service), including price and description.
5. Preview and submit to send it to the customer.
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
        "content": """
**Let’s Create an Options Estimate!**  
An Options Estimate is used when the customer might want multiple services. Each service is listed with a checkbox, so the customer can uncheck what they don’t want.

**Steps**:
1. Go to Sales → Estimates.
2. Click “+ New Estimate” → Options Estimate.
3. Add 2+ services as line items (each with price, description).
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
        "content": """
**Let’s Learn How to Manage Estimates in Markate!**  
After you send an estimate, you can check if the customer has viewed it (look for the “eye” icon). If they accept, you can convert it to a work order or invoice. If they haven’t responded in a few days, follow up. Don’t let it sit too long!

**Manage Button Options**:
- Mark as Accepted
- Convert to Work Order
- Convert to Invoice
- Clone
- Archive
- Delete

These actions help you finalize or reuse your estimates.
        """,
        "task_type": "reflection",
        "task": """Reflection: Why do you think it’s important to follow up with a customer if they haven’t responded to an estimate? How do you think managing estimates in Markate will help you keep your work organized as a sales rep?"""
    },
    {
        "title": "Chapter 3, Module 6: Final Task – Create Estimates for Yourself",
        "content": """
**Let’s Put It All Together: Create Estimates for Yourself!**  
You’ve made it to the final module of Chapter 3—amazing work! You’ve learned how to create Standard and Options Estimates in Markate, how to send them, and how to check their status. Now, let’s bring it all together by creating two estimates for *yourself* (using the test account you made in Chapter 1).

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
