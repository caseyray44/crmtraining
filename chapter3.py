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

**What You’ll Do in This Module**  
You’ll learn about the three types of estimates in Markate and understand which ones we use at CC Inc. You’ll also think about why we choose certain types over others, so you can make smart decisions when creating estimates for customers. This will help you get ready to create your own estimates in the next module.

**How to Find the Estimates Section in Markate**  
Before we talk about the types, let’s make sure you know how to find the Estimates section in Markate. Follow these steps carefully:  
1. **Make Sure You’re on the Markate Dashboard**: You should already be logged into Markate’s staging environment (https://stg.markate.com/, Username: Markate, Password: crm4you, then Email: support@xecutetech.com, Password: Windows4). If you’re not, go back to Chapter 1, Module 2, and follow the login steps. You’ll know you’re on the dashboard because you’ll see a menu bar at the top with options like “Sales,” “Leads,” and “Customers.”  
2. **Find the “Sales” Tab**: Look at the top of the screen. You’ll see a menu with options like “Sales,” “Leads,” “Schedule,” and more. Find the one that says “Sales.” You’ve used this before to find the Customers and Leads pages—it’s usually one of the first options on the left.  
3. **Hover Over the “Sales” Tab**: Move your mouse cursor over the word “Sales” (don’t click yet!). A dropdown menu will appear with more options, just like when you found the Customers or Leads pages.  
4. **Click on “Estimates”**: In the dropdown menu, find the option that says “Estimates” and click on it.  
   - **What If I Don’t See “Estimates”?** If you don’t see “Estimates” in the dropdown menu, make sure you’re hovering over “Sales” and not another tab like “Leads.” If you still don’t see it, try refreshing the page by pressing F5 on your keyboard, or log out and log back in.  
5. **Welcome to the Estimates Section!**: After clicking “Estimates,” you’ll be taken to the Estimates section in Markate. This is where you’ll see a list of all the estimates you’ve created (in the staging environment, these will be fake estimates for practice). It’s like a big list of price quotes you’ve made for customers, and you’ll use this section to create new estimates.  
6. **Click “+ New Estimate”**: In the top right corner of the Estimates page, you’ll see a green button that says “+ New Estimate.” Click on it to start creating a new estimate.  
   - **What Happens Next?** When you click “+ New Estimate,” Markate will show you three options: Standard Estimate, Options Estimate, and Package Estimate. These are the three types of estimates we’ll talk about in this module.

**The 3 Types of Estimates in Markate**  
Markate gives you three different ways to create an estimate, and each one works a little differently. Let’s go through them one by one, so you know which type to use for each customer.  

**1. Standard Estimate**  
A Standard Estimate is a simple document that lists the services you’re quoting for a customer. It can include any number of services, but the customer has to accept the entire estimate as-is. We typically only use it when the customer wants just one service.

**2. Options Estimate (Our Favorite!)**  
An Options Estimate lets customers pick and choose the services they want by unchecking any they don’t. We use this 90% of the time because it’s more flexible for customers with multiple needs.

**3. Package Estimate (We Don’t Use This)**  
Package Estimates bundle services into one price, which can be confusing, so CC Inc. avoids them.

**Why This Matters for You**  
- **Pick the Right Type**: You’ll save time and give customers the best experience by choosing Standard vs. Options correctly.  
- **Avoid Mistakes**: Using Options for a multi-service quote prevents redoing estimates if they only want some services.

**How This Fits into Your Role at CC Inc.**  
As a sales rep, you’ll create these estimates daily. Understanding them helps you close deals faster and keeps customers happy.

**What’s Next?**  
In the next module, we’ll learn how to create a Standard Estimate, and then in Module 4, an Options Estimate. Now let’s confirm your understanding with a quick miniquiz!
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
Now that you know the different types of estimates, it’s time to create your first one! In this module, we’ll learn how to create a *Standard Estimate* in Markate’s staging environment. A Standard Estimate is the simplest type, and it’s perfect for when a customer wants just one service. I’ll walk you through every step, and we’ll practice by creating 5 Standard Estimates, so you feel confident doing it on your own. Let’s get started!

**What You’ll Do in This Module**  
You’ll learn how to create a Standard Estimate in Markate, step-by-step. You’ll practice by creating 5 Standard Estimates using fake customers from Chapter 1, each with just one service. This will help you get comfortable with the process, so you’re ready to create Standard Estimates for real customers later. At the end, I’ll have a mini-quiz to make sure you understand the key steps.

**What is a Standard Estimate (Again)?**  
Just to recap from Module 2: A Standard Estimate is a simple document that lists the services you’re quoting for a customer, but the customer can’t pick and choose—they have to accept the whole estimate as it is. We use Standard Estimates when a customer wants just *one* service. For example:  
- If a customer says, “I only want pest control,” you’ll create a Standard Estimate with one service: “Pest Control for $150.”  
- The customer can then say yes or no to the whole estimate—they can’t change it.

**Why Do We Create Standard Estimates?**  
Creating a Standard Estimate in Markate is like writing a price tag for a single service. Here’s why it’s important:  
- **It Gives a Clear Price**: The customer knows exactly how much the service will cost, so they can decide if they want to hire CC Inc.  
- **It Keeps Things Simple**: Since there’s only one service, a Standard Estimate is quick to create and easy for the customer to understand.  
- **It Starts the Process**: Once the customer accepts the estimate, you can turn it into a job for our service teams to handle (we’ll learn more about that later).

**Steps to Create a Standard Estimate in Markate**  
Let’s create your first Standard Estimate together. We’ll use one of the fake customers you created in Chapter 1 (like John Doe). Follow these steps carefully, and I’ll explain why each step matters:  
1. **Go to the Estimates Section**: Make sure you’re logged into Markate’s staging environment (https://stg.markate.com/, Username: Markate, Password: crm4you, then Email: support@xecutetech.com, Password: Windows4). Go to the Estimates section (Sales → Estimates), like you learned in Module 2. You should see a list of any estimates you’ve created (it might be empty since we’re just starting).  
2. **Click the “+ New Estimate” Button**: In the top right corner of the Estimates page, click the green “+ New Estimate” button to start creating a new estimate.  
   - **What Happens Next?** Markate will show you the three estimate types: Standard Estimate, Options Estimate, and Package Estimate.  
3. **Select “Standard Estimate”**: Click on “Standard Estimate” to start creating a simple estimate with just one service.  
   - **Why Standard?** We’re practicing with a Standard Estimate because it’s the simplest type, and it’s perfect for a customer who only wants one service.  
4. **Fill in the Estimate Form**: Now you’ll see a form where you’ll enter the details of the estimate. Let’s go through each part:  
   - **Select Customer**: At the top of the form, there’s a field labeled “Customer.” Click on it and search for a fake customer you created in Chapter 1, like “John Doe.” Double-check that you’ve picked the right person.  
     - **Why This Field?** This tells Markate who the estimate is for. For example, if you pick John Doe, the estimate will be linked to his account, and he’ll get the email or text with the quote.  
     - **What If I Don’t See My Customer?** If you don’t see John Doe in the list, make sure you created him in Chapter 1. If not, go back to Chapter 1, Module 4, and create a few fake customers, then come back here.  
   - **Job Location**: Pick the customer’s address where the service will happen. For John Doe, this might be “123 Test Street” (his Billing Address from Chapter 1). If he has multiple addresses (like a vacation home named “Lakehouse”), choose the right one. For now, let’s use “123 Test Street.”  
     - **Why This Field?** This ensures our service teams know where to go if the customer accepts the estimate. For example, if John wants pest control at his main house, we need to know that’s at 123 Test Street.  
     - **What If There’s No Address?** If no address appears, you can add one by clicking “Add Address,” just like when you created a customer in Chapter 1.  
   - **Job Name**: This is like the “title” of your estimate. Use a simple name that describes the job, like “Pest Control for John Doe.” If you’re not sure, you can just use the customer’s name, like “John Doe.”  
     - **Why This Field?** The Job Name helps you and the customer know what the estimate is for. For example, “Pest Control for John Doe” tells you exactly what this estimate is about when you look at it later.  
   - **Estimate Number / Date / Expiration**: These fields usually fill in automatically. The Estimate Number is a unique ID for the estimate, the Date is today’s date, and the Expiration is set to 30 days by default (meaning the customer has 30 days to accept the estimate before it expires). You don’t need to change these.  
     - **Why 30 Days?** This gives the customer enough time to decide, but it also makes sure the price doesn’t stay valid forever (prices might change after 30 days).  
   - **Purchase Order Number**: We don’t use this field at CC Inc. Leave it blank.  
     - **Why Not?** Some businesses use purchase order numbers for their own tracking, but we don’t need this for our workflow.  
5. **Add a Line Item (The Service)**: A line item is the service you’re quoting for. Since this is a Standard Estimate with just one service, you’ll add one line item. Scroll down to the “Line Items” section and fill in these details:  
   - **Item Name**: Select the service from the preset list or type it in. For example, let’s pick “Pest Control.” You might see options like “House Washing,” “Window Washing,” or “Pest Control” in the dropdown—choose “Pest Control.”  
     - **Why This Field?** This tells the customer what service you’re quoting for. For example, “Pest Control” means you’re giving a price for pest control at John’s house.  
   - **Service / Material / Product**: Select “Service” from the dropdown.  
     - **Why Service?** At CC Inc., we mostly provide services (like pest control or house washing), not physical products. Only use “Material” or “Product” if you’re billing for something tangible, like “Bug Spray Can” (but we don’t do that in this training).  
   - **Quantity**: Set this to 1.  
     - **Why 1?** Since we’re quoting for one service (pest control at John’s house), the quantity is 1. If you were quoting for pest control at two houses, you’d set the quantity to 2, but for now, keep it simple.  
   - **Price**: Enter the dollar amount you’re quoting. Let’s say pest control costs $150, so type “150” in the Price field.  
     - **Why This Field?** This is the price the customer will see. For example, “$150” tells John how much pest control will cost.  
   - **Discount**: Keep this at 0 unless your manager approves a discount.  
     - **Why 0?** We don’t give discounts unless there’s a special reason, and for practice, we’ll keep it simple with no discounts.  
   - **Tax**: This is automatically set based on the customer’s location. You don’t need to change it.  
     - **Why Automatic?** Markate calculates the tax for you, so you don’t have to worry about it. For example, if the tax rate is 5%, Markate will add $7.50 to the $150 price (making the total $157.50).  
   - **Description (Super Important!)**: Always fill in a quick description of the service. For example, type “Pest control for main house—includes ants and spiders.”  
     - **Why This Field?** The description makes the estimate clear for both you and the customer. For example, “Pest control for main house—includes ants and spiders” tells John exactly what he’s getting, so there’s no confusion later. It also helps our service teams know what to do if the estimate turns into a job.  
6. **Preview the Estimate**: Scroll down to the bottom of the form. You’ll see two buttons: “Save as Draft” and “Preview.” Click “Preview” to see what the estimate will look like to the customer.  
   - **What Does Preview Do?** Preview shows you the estimate from the customer’s point of view. For example, John will see a document that says “Pest Control: $150, Description: Pest control for main house—includes ants and spiders, Total: $157.50 (with tax).”  
   - **Why Preview?** This lets you double-check everything before sending it to the customer. If something looks wrong (like the price or description), you can click “Edit” to fix it.  
7. **Submit the Estimate**: While in Preview mode, look at the top of the screen. You’ll see a button that says “Submit Estimate.” Click it to send the estimate to the customer.  
   - **What Happens Next?** Markate will open a small window showing the customer’s email (e.g., john@example.com). You can add or remove emails if needed. Since John’s notification method is set to “Both Email & Text” (from Chapter 1), he’ll get an email and a text with the estimate. Click “Send” (or “OK”) to confirm.  
   - **Why Check Notifications?** If the customer doesn’t have “Both Email & Text” set, they might not get the estimate. You can check or update this in their customer profile (go to Sales → Customers, find John Doe, and make sure it’s set to “Both Email & Text”).  
8. **Check the Status**: Go back to the Estimates section (Sales → Estimates). You’ll see your new estimate in the list with a status of “Submitted.”  
   - **What Does Submitted Mean?** It means the estimate has been sent to the customer, and now you’re waiting for them to accept or reject it.

**Practice: Create 5 Standard Estimates**  
To get comfortable with creating Standard Estimates, you’ll create 5 of them. Each time, use a different fake customer from Chapter 1 and a different service, but follow the same steps (Standard Estimate, single service, preview, submit). That’s it!

**Why This Matters for You**  
- **Start Simple**: Creating Standard Estimates is a great way to get comfortable with the process, since they’re the simplest type. Once you master this, you’ll be ready to create Options Estimates in the next module.  
- **Practice Makes Perfect**: Doing 5 Standard Estimates helps you learn quickly without risking real data.  
- **Accuracy is Key**: A clear line item description prevents confusion later.

**How This Fits into Your Role at CC Inc.**  
As a sales rep, you’ll create estimates like this for customers who want a single service. For instance, if someone calls asking for “just window washing,” you’ll do a Standard Estimate.

**What’s Next?**  
In the next module, we’ll tackle Options Estimates, which are even more common at CC Inc. First, let’s confirm you understand Standard Estimates with a mini-quiz!""",
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
        "content": """**Let’s Create an Options Estimate in Markate!**  
Great job creating Standard Estimates in the last module! Now, let’s learn how to create an *Options Estimate*, which is the type we use most often at CC Inc. An Options Estimate lets customers choose which services they want, making it perfect for most of our customers. I’ll walk you through every step, and we’ll practice by creating 10 Options Estimates, so you feel confident doing it on your own. Let’s get started!

**What You’ll Do in This Module**  
You’ll learn how to create an Options Estimate in Markate, step-by-step. You’ll practice by creating 10 Options Estimates using fake customers from Chapter 1, each with at least 2 services. This will help you get comfortable with the process, so you’re ready to create Options Estimates for real customers later. At the end, I’ll have a scenario task to make sure you understand when to use an Options Estimate.

**What is an Options Estimate (Again)?**  
Just to recap from Module 2: An Options Estimate is a document that lets customers choose which services they want by checking or unchecking boxes. We use Options Estimates 90% of the time at CC Inc. because they’re perfect for customers who want more than one service. For example:  
- If a customer says, “I want a quote for house washing and pest control, but I’m not sure about both,” you’ll create an Options Estimate with two services: “House Washing for $200” and “Pest Control for $150.”  
- The customer can then check the services they want (or uncheck the ones they don’t), and Markate will update the total price automatically.

**Why Do We Create Options Estimates?**  
Creating an Options Estimate in Markate is like giving the customer a menu they can customize. Here’s why it’s important:  
- **It Gives Customers Control**: They can pick exactly what they want.  
- **It Saves You Time**: No need to revise the estimate if they don’t want all services.  
- **It Reduces Confusion**: Clear prices for each service.

**Steps to Create an Options Estimate**  
Similar to Standard, but you add multiple line items. Each item has a checkbox.

**Practice: 10 Options Estimates**  
Use at least 2 services each time. This is the most common approach at CC Inc.

**Why This Matters for You**  
- **Master the Main Type**: Options is used 90% of the time.  
- **Make Customers Happy**: They get to choose exactly what they want.

**What’s Next?**  
We’ll learn to manage these estimates in the next module. First, let’s do a quick scenario check!""",
        "task_type": "scenario",
        "task": """**Scenario**: A customer named Emily Johnson calls and says she only wants a quote for gutter cleaning. What type of estimate should you create for her?  
A) Options Estimate, because it’s the type we use most often.  
B) Standard Estimate, because she only wants one service.  
C) Package Estimate, because it’s a single service.  
Select the correct answer and explain why in the box below, thinking about the rules for each estimate type.""",
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
You’re doing great! You’ve learned how to create Standard and Options Estimates in Markate, which covers most of what you’ll do as a sales rep at CC Inc. Now, let’s learn what to do *after* you send an estimate to a customer. In this module, we’ll cover how to check the status of your estimates and manage them—like turning them into jobs or invoices. I’ll walk you through every step, so you know exactly what to do when a customer responds to your quote. Let’s get started!

**What You’ll Do in This Module**  
You’ll learn how to check the status of your estimates in Markate and use the “Manage” options to take action, like marking an estimate as accepted or turning it into a job. You’ll also think about why these steps are important for your role at CC Inc. This will help you complete the process of working with estimates, from creating them to turning them into jobs for our service teams.

**Why Do We Need to Manage Estimates?**  
Sending an estimate to a customer is just the first step. After that, you need to keep track of what happens—does the customer accept the estimate? Do they have questions? Managing estimates in Markate helps you:  
- **Know What’s Happening**: You can see if they viewed or accepted it.  
- **Turn Quotes into Jobs**: Convert to a work order if they say yes.  
- **Keep Things Organized**: All estimates are stored in one place.

**Steps to Manage Estimates in Markate**  
Check the status, see if it’s “Submitted,” “Viewed,” “Accepted,” or “Rejected.” Use “Manage” to Mark as Accepted, Convert to Work Order, Convert to Invoice, Clone, Archive, or Delete.

**Why This Matters**  
- **Close the Loop**: From quote to actual job.  
- **Stay Organized**: Don’t lose track of quotes.  
- **Grow CC Inc.**: More accepted estimates means more business.

**How This Fits into Your Role**  
You’ll be the one checking on these estimates and following up.

**What’s Next?**  
In the final module, you’ll create two estimates for yourself as a final practice. Let’s reflect first!""",
        "task_type": "reflection",
        "task": """Reflection: Why do you think it’s important to follow up with a customer if they haven’t responded to an estimate? How do you think managing estimates in Markate will help you keep your work organized as a sales rep?"""
    },
    {
        "title": "Chapter 3, Module 6: Final Task – Create Estimates for Yourself",
        "content": """**Let’s Put It All Together: Create Estimates for Yourself!**  
You’ve made it to the final module of Chapter 3—amazing work! You’ve learned how to create Standard and Options Estimates in Markate and how to manage them after sending them to customers. Now, let’s bring it all together with a final task: you’re going to create two estimates for *yourself* in Markate, using the test account you made in Chapter 1. This will help you see the whole process from both the sales rep’s side and the customer’s side. I’ll guide you through every step, as always!

**What You’ll Do in This Module**  
You’ll create two estimates for your test account in Markate’s staging environment: one Options Estimate with 2 or more services, and one Standard Estimate with 1 service. You’ll submit them and imagine what it’s like to receive them as a customer. This will give you a complete picture of how estimates work, from start to finish. At the end, I’ll have a reflection task to help you think about what you’ve learned.

**Why Create Estimates for Yourself?**  
Creating estimates for yourself is like playing both roles in a play—you’ll be the sales rep creating the estimates, and the customer receiving them. Here’s why this is so helpful:  
- **See the Whole Process**: You’ll experience the entire process of creating, sending, and managing estimates.  
- **Understand the Customer’s Side**: Building empathy for what a customer sees.  
- **Practice Makes Perfect**: You’re fully prepared to handle real customers later.  
- **Build Confidence**: You’ll know exactly how your actions affect them.

**How to Create Your Estimates in Markate**  
1. Create an Options Estimate (2+ services) for yourself.  
2. Create a Standard Estimate (1 service) for yourself.  
3. Check them in the “Submitted” stage.  
4. Imagine viewing them as a customer.

**Why This Matters**  
- **Tie It All Together**: This completes the journey from lead to quote.  
- **Empathy**: Seeing it from both sides helps you do a better job for real customers.

**What’s Next?**  
You’ve now completed all modules for Chapter 3! After your reflection below, you’ll take a final quiz with 5 questions. You need 4 correct to pass (80%). If you don’t pass, review and try again. Good luck!""",
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
