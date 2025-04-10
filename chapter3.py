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
- **What It Is**: A Standard Estimate is a simple document that lists the services you’re quoting for a customer. It can include any number of services, but the customer can’t pick and choose—they have to accept the whole estimate as it is.  
- **How It Works**: Think of a Standard Estimate like a fixed menu at a restaurant. For example, if you create a Standard Estimate with one service like “House Washing for $200,” the customer can either say yes to the whole thing or say no—they can’t change it. If you list multiple services (like “House Washing for $200” and “Pest Control for $150”), they still have to accept both or none.  
- **When We Use It**: We only use a Standard Estimate when the customer needs just *one* service. For example, if a customer calls and says, “I only want window washing,” you can create a Standard Estimate with one line item: “Window Washing for $100.”  
- **Why We Don’t Use It Often**: If the customer wants to pick and choose services (like “I want house washing but not pest control”), a Standard Estimate creates extra work for you. You’d have to go back, edit the estimate, and send it again. Because of this, we only use Standard Estimates about 10% of the time—usually for very simple jobs with just one service.  

**2. Options Estimate (Our Favorite!)**  
- **What It Is**: An Options Estimate is a document that lets customers choose which services they want. It’s like a customizable menu where they can pick what they like.  
- **How It Works**: When you create an Options Estimate, you list the services as separate line items, and each one has a checkbox next to it. For example, you might list “House Washing for $200” and “Pest Control for $150.” When the customer gets the estimate, they’ll see both services with checkboxes, and by default, all boxes are checked. They can uncheck any services they don’t want. So, if they only want house washing, they can uncheck pest control, and the total price will update to $200.  
- **When We Use It**: We use Options Estimates 90% of the time at CC Inc. because they’re perfect for most customers. Many customers want more than one service, and they like being able to choose. For example, a customer might say, “I want a quote for house washing and window washing, but I’m not sure about both.” You can create an Options Estimate with both services, and they can decide what they want.  
- **Why We Love It**:  
  - **It Eliminates Confusion**: The customer can see all the services and their prices, and they can pick exactly what they want without asking you to change the estimate.  
  - **It Saves Time**: If the customer only wants some of the services, you don’t have to edit the estimate—they can just uncheck what they don’t want, and Markate updates the total automatically.  
- **Important Rule**: An Options Estimate needs at least 2 services (line items) to work. If you only have 1 service, use a Standard Estimate instead. For example, if a customer only wants pest control, use a Standard Estimate. But if they want pest control and window washing, use an Options Estimate.  

**3. Package Estimate (We Don’t Use This)**  
- **What It Is**: A Package Estimate is a more complex way to bundle services together into a single “package” with one price. For example, you might create a package called “Spring Cleaning Special” that includes house washing, window washing, and pest control for a single price of $400.  
- **Why We Don’t Use It**: At CC Inc., we’ve never needed Package Estimates because our customers prefer to see the price for each service separately. Options Estimates work better for us because they give customers more flexibility to choose what they want. We also don’t want to confuse customers with bundled pricing—keeping things simple is better for our workflow. So, you won’t need to use Package Estimates in this training or in your role at CC Inc.

**Why This Matters for You**  
- **Pick the Right Type**: Knowing which estimate type to use helps you give customers the best experience. For example, using an Options Estimate for a customer who wants multiple services saves you time and makes them happy because they can choose what they want.  
- **Avoid Extra Work**: If you use the wrong type (like a Standard Estimate for multiple services), you might have to edit the estimate later, which takes more time. Understanding the types now means you’ll work more efficiently later.  
- **Build Confidence**: The more you understand about estimates, the more confident you’ll feel when talking to customers. For example, you’ll know exactly which type to use when a customer says, “I want a quote for house washing and maybe pest control.”

**How This Fits into Your Role at CC Inc.**  
As a sales rep, you’ll create estimates every day to give customers quotes for our services. Knowing the difference between Standard and Options Estimates helps you:  
- **Make Customers Happy**: Using the right estimate type (usually Options) lets customers choose what they want, which makes them feel in control and more likely to say yes.  
- **Work Faster**: Picking the right type from the start means less back-and-forth with the customer. For example, an Options Estimate lets them uncheck services they don’t want, so you don’t have to revise the estimate manually.  
- **Close More Deals**: A clear, easy-to-understand estimate makes customers more likely to accept your quote and hire CC Inc. for the job.

**What’s Next?**  
In the next module, we’ll learn how to create a Standard Estimate and an Options Estimate in Markate, step-by-step. You’ll practice creating a few estimates to get comfortable with the process. To make sure you understand the difference between Standard and Options Estimates, I’ve prepared a scenario task for you. Let’s do this!""",
        "task_type": "scenario",
        "task": """**Scenario**: A customer named Sarah Smith calls and says she wants a quote for house washing and window washing, but she’s not sure if she wants both services. What type of estimate should you create for her?  
A) Standard Estimate, because it’s simpler to create.  
B) Options Estimate, because it lets Sarah choose which services she wants.  
C) Package Estimate, because it bundles the services together.  
Select the correct answer and explain why in the box below, thinking about how this choice helps Sarah and saves you time.""",
        "options": [
            "A) Standard Estimate, because it’s simpler to create.",
            "B) Options Estimate, because it lets Sarah choose which services she wants.",
            "C) Package Estimate, because it bundles the services together."
        ],
        "correct_answer": 1
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
To get comfortable with creating Standard Estimates, you’ll create 5 of them. Each time, use a different fake customer from Chapter 1 and a different service, but follow the same steps:  
- Use a Standard Estimate (since we’re only quoting one service).  
- Pick a customer (like John Doe, Sarah Smith, etc.).  
- Add one line item with a service, price, and description.  
- Preview and submit the estimate.  
For example:  
- Estimate 1: John Doe, Pest Control, $150, “Pest control for main house—includes ants and spiders.”  
- Estimate 2: Sarah Smith, Window Washing, $100, “Exterior windows only—main house.”  
- Estimate 3: Mike Johnson, House Washing, $200, “House washing for main house—includes front porch.”  
- And so on, until you’ve created 5 Standard Estimates.  
- **Why 5 Times?** Doing this 5 times helps you practice the process so it becomes second nature. By the time you’re done, you’ll be able to create a Standard Estimate quickly and confidently, which is a key part of your job as a sales rep.

**Why This Matters for You**  
- **Start Simple**: Creating Standard Estimates is a great way to get comfortable with the process, since they’re the simplest type. Once you master this, you’ll be ready to create Options Estimates in the next module.  
- **Practice Makes Perfect**: Making 5 Standard Estimates in the staging environment helps you learn the steps without risking real customer data.  
- **Accuracy is Key**: Entering the right details (like the price and description) ensures the customer gets a clear quote. For example, a good description like “Pest control for main house—includes ants and spiders” prevents confusion later.

**How This Fits into Your Role at CC Inc.**  
As a sales rep, you’ll create estimates like this for customers who want a single service. For example, if a customer calls and says, “I only want window washing,” you’ll create a Standard Estimate to give them a clear price. This helps you:  
- **Give Quick Quotes**: A Standard Estimate is fast to create, so you can give the customer a price right away.  
- **Build Trust**: A clear estimate with a good description makes the customer feel confident in CC Inc., which makes them more likely to say yes.

**What’s Next?**  
In the next module, we’ll learn how to create an Options Estimate, which is the type we use most often at CC Inc. You’ll practice creating a few Options Estimates to get comfortable with the process. To make sure you understand how to create a Standard Estimate, I’ve prepared a mini-quiz for you. Let’s do this!""",
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
- **It Gives Customers Control**: The customer can pick exactly what they want, which makes them more likely to say yes.  
- **It Saves You Time**: If the customer only wants some of the services, they can uncheck the ones they don’t want, and you don’t have to edit the estimate yourself.  
- **It Reduces Confusion**: The customer sees all the services and their prices clearly, so there’s no misunderstanding about what they’re paying for.

**Steps to Create an Options Estimate in Markate**  
Let’s create your first Options Estimate together. We’ll use one of the fake customers you created in Chapter 1 (like Sarah Smith). Follow these steps carefully—they’re very similar to creating a Standard Estimate, but with a few differences:  
1. **Go to the Estimates Section**: Make sure you’re logged into Markate’s staging environment (https://stg.markate.com/, Username: Markate, Password: crm4you, then Email: support@xecutetech.com, Password: Windows4). Go to the Estimates section (Sales → Estimates).  
2. **Click the “+ New Estimate” Button**: In the top right corner, click the green “+ New Estimate” button.  
3. **Select “Options Estimate”**: Click on “Options Estimate” to start creating an estimate that lets the customer choose their services.  
   - **Why Options?** We’re using an Options Estimate because we’ll include at least 2 services, and we want the customer to be able to pick what they want.  
4. **Fill in the Estimate Form**: The form looks almost the same as the one for a Standard Estimate. Let’s fill it in:  
   - **Select Customer**: Search for a fake customer, like “Sarah Smith.” Double-check that you’ve picked the right person.  
   - **Job Location**: Pick Sarah’s address, like “456 Fake Avenue.” If she has multiple addresses (like a vacation home), choose the right one.  
   - **Job Name**: Use a simple name, like “House Services for Sarah Smith.”  
   - **Estimate Number / Date / Expiration**: These will auto-fill (leave them as is).  
   - **Purchase Order Number**: Leave this blank—we don’t use it.  
5. **Add Line Items (At Least 2 Services)**: Since this is an Options Estimate, you need at least 2 services (line items) so the customer has something to choose between. Scroll down to the “Line Items” section and add the first service:  
   - **Item Name**: Select “House Washing.”  
   - **Service / Material / Product**: Select “Service.”  
   - **Quantity**: Set to 1.  
   - **Price**: Enter $200.  
   - **Discount**: Keep at 0.  
   - **Tax**: Leave as auto-set.  
   - **Description**: Type “House washing for main house—includes front porch.”  
   - **Add Another Option**: Click the “Add Another Option” button to add a second service. Fill in the second line item:  
     - **Item Name**: Select “Pest Control.”  
     - **Service / Material / Product**: Select “Service.”  
     - **Quantity**: Set to 1.  
     - **Price**: Enter $150.  
     - **Discount**: Keep at 0.  
     - **Tax**: Leave as auto-set.  
     - **Description**: Type “Pest control for main house—includes ants and spiders.”  
   - **Why At Least 2?** An Options Estimate needs at least 2 line items so the customer has something to choose between. For example, Sarah can decide if she wants both house washing and pest control, or just one of them.  
6. **Adjustments, Markups, and Other Settings**: Below the line items, you’ll see some extra settings. For now, we’ll leave most of these as they are:  
   - **Adjustments**: This lets you add an extra discount or fee. We rarely use this, so leave it blank.  
   - **Markup**: This applies a percentage to all line items (e.g., a 10% markup would increase the total price). The customer won’t see a “markup” line—it just raises the total. We don’t use this at CC Inc., so leave it at 0.  
   - **Deposit Request / Payment Schedule**: This lets you ask for a deposit or set up a payment plan. We rarely use this, so leave it blank.  
   - **Message to Customer & Terms & Conditions**: These are pre-set by CC Inc. and don’t need to be edited. They might say something like, “Thank you for choosing CC Inc.! Payment is due upon completion.”  
   - **Attachments**: You can attach photos (like a picture of the customer’s house). If you do, note it in the line item description (e.g., “See attached photo of front porch”). For practice, we’ll skip attachments.  
7. **Preview the Estimate**: Scroll down and click “Preview” to see what the estimate will look like to the customer.  
   - **What Will Sarah See?** Sarah will see a document with two services: “House Washing: $200, Description: House washing for main house—includes front porch” and “Pest Control: $150, Description: Pest control for main house—includes ants and spiders.” Each service will have a checkbox next to it, and both will be checked by default. The total will be $350 (plus tax, e.g., $367.50 if the tax rate is 5%). Sarah can uncheck any service she doesn’t want, and the total will update automatically.  
8. **Submit the Estimate**: In Preview mode, click “Submit Estimate” at the top. Markate will show Sarah’s email (e.g., sarah@example.com). Since her notification method is “Both Email & Text,” she’ll get an email and a text. Click “Send” to submit.  
9. **Check the Status**: Go back to Sales → Estimates. You’ll see your Options Estimate in the list with a “Submitted” status.

**Practice: Create 10 Options Estimates**  
To get comfortable with creating Options Estimates, you’ll create 10 of them. Each time, use a different fake customer from Chapter 1 and include at least 2 services:  
- Use an Options Estimate (since we’re quoting multiple services).  
- Pick a customer (like Sarah Smith, Mike Johnson, etc.).  
- Add at least 2 line items with services, prices, and descriptions.  
- Preview and submit the estimate.  
For example:  
- Estimate 1: Sarah Smith, House Washing ($200, “House washing for main house—includes front porch”), Pest Control ($150, “Pest control for main house—includes ants and spiders”).  
- Estimate 2: Mike Johnson, Window Washing ($100, “Exterior windows only—main house”), Gutter Cleaning ($120, “Gutter cleaning for main house—includes downspouts”).  
- And so on, until you’ve created 10 Options Estimates.  
- **Why 10 Times?** Doing this 10 times helps you practice the process, since Options Estimates are the type we use most often. By the time you’re done, you’ll be ready to create Options Estimates for real customers.

**Why This Matters for You**  
- **Master the Main Type**: Options Estimates are the type we use 90% of the time, so getting good at creating them is a key skill for your role.  
- **Practice Makes Perfect**: Creating 10 Options Estimates in the staging environment helps you learn the steps without risking real customer data.  
- **Make Customers Happy**: An Options Estimate lets customers choose what they want, which makes them more likely to accept your quote and hire CC Inc.

**How This Fits into Your Role at CC Inc.**  
As a sales rep, you’ll create Options Estimates for most customers, since they often want more than one service. For example, if a customer calls and says, “I want a quote for house washing and window washing,” you’ll create an Options Estimate so they can pick what they want. This helps you:  
- **Save Time**: The customer can uncheck services they don’t want, so you don’t have to revise the estimate.  
- **Close More Deals**: Giving customers control makes them more likely to accept your quote and hire CC Inc.

**What’s Next?**  
In the next module, we’ll learn how to manage estimates after you’ve sent them—like checking their status and turning them into jobs. To make sure you understand when to use an Options Estimate, I’ve prepared a scenario task for you. Let’s do this!""",
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
- **Know What’s Happening**: You can see if the customer has viewed your estimate or accepted it, so you know what to do next.  
- **Turn Quotes into Jobs**: If the customer says yes, you can turn the estimate into a job for our service teams to handle.  
- **Keep Things Organized**: Markate keeps all your estimates in one place, so you can find them easily and take action when needed.

**Steps to Manage Estimates in Markate**  
Let’s go through the process of managing an estimate after you’ve sent it. We’ll use one of the Options Estimates you created in Module 4 (like the one for Sarah Smith). Follow these steps:  
1. **Go to the Estimates Section**: Go to Sales → Estimates in Markate’s staging environment. You’ll see a list of all the estimates you’ve created, including the ones from Modules 3 and 4.  
2. **Check the Status of Your Estimate**: Look for the estimate you sent to Sarah Smith (e.g., “House Services for Sarah Smith”). You’ll see a status next to it, like “Submitted.” Here’s what the statuses mean:  
   - **Draft**: You saved the estimate but didn’t send it to the customer.  
   - **Submitted**: You sent the estimate, and you’re waiting for the customer to respond.  
   - **Viewed**: The customer has opened the estimate (you’ll see a small eye icon next to it).  
   - **Accepted**: The customer has agreed to the estimate (either by clicking “Accept” in the email/text or by telling you verbally).  
   - **Rejected**: The customer has declined the estimate.  
   - **What If I Can’t Find It?** You can search for the customer’s name (e.g., “Sarah Smith”) or filter by status (e.g., “Submitted”) to find the estimate.  
3. **Check If the Customer Has Viewed It**: If you see a small eye icon next to Sarah’s estimate, it means she has viewed it. This is a good sign—it means she’s looking at your quote!  
   - **Why This Matters**: If the customer hasn’t viewed the estimate, you might need to follow up (e.g., call her and say, “Hi Sarah, I sent you a quote—did you get it?”). If she has viewed it, you can wait a little longer for her to decide.  
4. **Use the “Manage” Button**: On the right side of the estimate, you’ll see a “Manage” button. Click on it to see a list of options for what to do next. Here’s what each option does:  
   - **Mark as Accepted**: Use this if the customer tells you they agree to the estimate (e.g., Sarah calls and says, “I want both house washing and pest control”). This changes the status to “Accepted.”  
     - **Why Do This?** Marking it as accepted lets everyone at CC Inc. know the customer said yes, so you can move forward with the job.  
   - **Convert to Work Order**: This turns the estimate into a job for our service teams to handle. For example, if Sarah accepts the estimate, you can convert it to a work order, and our team will go to her house to do the house washing and pest control.  
     - **What Happens Next?** A work order is like a to-do list for our service teams—it tells them where to go (456 Fake Avenue), what to do (house washing and pest control), and any details (like “includes front porch”).  
   - **Convert to Invoice**: This creates a bill for the customer right away. For example, if Sarah has already had the services done, you can convert the estimate to an invoice to bill her for $350 (plus tax).  
     - **Why Do This?** We usually create an invoice after the job is done, but you can do it earlier if the customer prefers to pay upfront.  
   - **Clone**: This copies the estimate, so you can use it as a starting point for a new one. For example, if another customer wants a similar quote, you can clone Sarah’s estimate and edit it.  
     - **Why Clone?** This saves time if you’re creating similar estimates for different customers.  
   - **Archive**: This hides the estimate from the main list (but doesn’t delete it). Use this for old estimates you don’t need to see anymore.  
     - **Why Archive?** It keeps your Estimates list clean, so you can focus on active estimates.  
   - **Delete**: This removes the estimate completely. We rarely use this, so don’t delete anything for now.  
     - **Why Not Delete?** Even if an estimate is old, it’s good to keep it in case you need to look it up later (e.g., to see what you quoted a customer last year).  
5. **Follow Up with the Customer**: If Sarah hasn’t responded after a few days, you can call or email her to check in. For example, you might say, “Hi Sarah, I sent you a quote for house washing and pest control—do you have any questions?”  
   - **Why Follow Up?** Sometimes customers need a little nudge to make a decision. Following up shows you care, which can make them more likely to say yes.

**Why This Matters for You**  
- **Close the Loop**: Managing estimates helps you turn quotes into jobs, which is the whole point of creating estimates in the first place. For example, if Sarah accepts your quote, you can convert it to a work order and get the job done.  
- **Stay Organized**: Checking the status of your estimates keeps you on top of your work. For example, if you see that Sarah hasn’t viewed her estimate, you’ll know to follow up with her.  
- **Help CC Inc. Grow**: Every estimate you manage and turn into a job means more business for CC Inc. By mastering this process, you’re helping our company succeed.

**How This Fits into Your Role at CC Inc.**  
As a sales rep, managing estimates is a key part of your job. You’ll use this process to:  
- **Turn Quotes into Jobs**: When a customer accepts an estimate, you’ll convert it to a work order, so our service teams can get to work.  
- **Keep Customers Happy**: Following up on estimates shows the customer you care, which makes them more likely to choose CC Inc.  
- **Stay on Top of Your Work**: Checking the status of your estimates ensures you don’t miss any opportunities to close a deal.

**What’s Next?**  
In the next module, you’ll do a final task: creating estimates for yourself using the test account you made in Chapter 1. This will help you see the whole process from both the sales rep’s side and the customer’s side. To make sure you understand how to manage estimates, I’ve prepared a reflection task for you. Let’s do this!""",
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
- **See the Whole Process**: You’ll experience the entire process of creating, sending, and managing estimates, which ties together everything you’ve learned in Chapter 3.  
- **Understand the Customer’s Side**: By using your own test account, you’ll see what it’s like to be a customer receiving an estimate. This builds on what you did in Chapters 1 and 2, where you created your test account and an opportunity to see the customer’s perspective.  
- **Practice Makes Perfect**: This final task gives you one more chance to practice creating estimates, so you’re fully prepared to do this with real customers.  
- **Build Confidence**: Seeing the whole process from start to finish makes you more confident as a sales rep. You’ll know exactly what to do when a real customer asks for a quote, and you’ll understand how your actions affect them.

**How to Create Your Estimates in Markate**  
Let’s create your two estimates together. We’ll use your test account from Chapter 1 (e.g., “Damon Smith” or “Jake Smith”). Follow these steps carefully:  

**Task 1: Create an Options Estimate for Yourself**  
1. **Go to the Estimates Section**: Go to Sales → Estimates in Markate’s staging environment.  
2. **Click the “+ New Estimate” Button**: Click the green “+ New Estimate” button.  
3. **Select “Options Estimate”**: Choose “Options Estimate” since we’ll include 2 or more services.  
4. **Fill in the Estimate Form**:  
   - **Select Customer**: Search for your test account (e.g., “Damon Smith”).  
   - **Job Location**: Use the address from your test account, like “123 Test Street, Springfield, IL, 62704.”  
   - **Job Name**: Use “Test Options Estimate for [Your Name].” For example, “Test Options Estimate for Damon.”  
   - **Estimate Number / Date / Expiration**: Leave as auto-filled.  
   - **Purchase Order Number**: Leave blank.  
5. **Add Line Items (At Least 2 Services)**: Add two services:  
   - **First Line Item**:  
     - Item Name: House Washing  
     - Service / Material / Product: Service  
     - Quantity: 1  
     - Price: $200  
     - Discount: 0  
     - Tax: Auto-set  
     - Description: “House washing for main house—includes front porch.”  
   - **Second Line Item**: Click “Add Another Option” and add:  
     - Item Name: Window Washing  
     - Service / Material / Product: Service  
     - Quantity: 1  
     - Price: $100  
     - Discount: 0  
     - Tax: Auto-set  
     - Description: “Exterior windows only—main house.”  
6. **Preview and Submit**: Click “Preview” to see the estimate, then click “Submit Estimate.” Markate will show your email (e.g., damon@example.com). Since your notification method is “Both Email & Text,” you’d get an email and text (but in the staging environment, no real messages are sent). Click “Send” to submit.  
7. **Check the Status**: Go back to Sales → Estimates and confirm your estimate has a “Submitted” status.

**Task 2: Create a Standard Estimate for Yourself**  
1. **Click the “+ New Estimate” Button**: Go back to Sales → Estimates and click “+ New Estimate” again.  
2. **Select “Standard Estimate”**: Choose “Standard Estimate” since we’ll include just 1 service.  
3. **Fill in the Estimate Form**:  
   - **Select Customer**: Pick your test account again (e.g., “Damon Smith”).  
   - **Job Location**: Use “123 Test Street.”  
   - **Job Name**: Use “Test Standard Estimate for [Your Name].” For example, “Test Standard Estimate for Damon.”  
   - **Estimate Number / Date / Expiration**: Leave as auto-filled.  
   - **Purchase Order Number**: Leave blank.  
4. **Add One Line Item**: Add one service:  
   - **Item Name**: Pest Control  
   - **Service / Material / Product**: Service  
   - **Quantity**: 1  
   - **Price**: $150  
   - **Discount**: 0  
   - **Tax**: Auto-set  
   - **Description**: “Pest control for main house—includes ants and spiders.”  
5. **Preview and Submit**: Click “Preview” to see the estimate, then click “Submit Estimate.” Click “Send” to submit.  
6. **Check the Status**: Go back to Sales → Estimates and confirm your Standard Estimate has a “Submitted” status.

**What Happens Next?**  
Now that you’ve created your two estimates, let’s see what it looks like from both sides:  
- **As a Sales Rep**: You’ve created two estimates for “Damon Smith”: an Options Estimate with house washing and window washing, and a Standard Estimate with pest control. You’ve submitted them and can see them in the Estimates section with a “Submitted” status. In a real scenario, you’d now wait for the customer (you!) to respond, and you could use the “Manage” button to take action (like marking them as accepted).  
- **As a Customer**: You’re now the customer in this scenario. In a real scenario, you’d get emails and texts with the estimates. For the Options Estimate, you’d see two services with checkboxes: “House Washing: $200” and “Window Washing: $100.” You could uncheck one if you didn’t want it. For the Standard Estimate, you’d see just “Pest Control: $150” with no checkboxes—you’d have to accept or reject the whole thing. In the staging environment, no real messages are sent, but you can imagine what it would be like to receive them.

Why This Matters for You

See Both Sides: Creating estimates for yourself lets you see the process from both the sales rep’s side (creating and sending the estimates) and the customer’s side (receiving and reviewing them). This helps you understand how your actions affect the customer, making you better at your job.
Tie It All Together: This task brings together everything you’ve learned in Chapter 3: creating Standard and Options Estimates, submitting them, and understanding how they look to the customer. It’s like a final practice run before you start working with real customers.
Build Empathy: Seeing the estimates from the customer’s perspective helps you empathize with them. For example, you’ll understand why a clear description (like “House washing for main house—includes front porch”) is important, because it would help you as a customer know exactly what you’re getting.
How This Fits into Your Role at CC Inc.

As a sales rep, you’ll create and send estimates for customers every day, and this task shows you how the whole process works. By creating estimates for yourself, you’re practicing:

Creating Professional Estimates: You’ve made both a Standard and an Options Estimate, which are the two types you’ll use most often at CC Inc. For example, if a real customer calls and says, “I want a quote for house washing and maybe window washing,” you’ll know how to create an Options Estimate for them.
Understanding the Customer’s Experience: Seeing the estimates from the customer’s side helps you make better estimates for real customers. For example, you’ll know why it’s important to include a good description, because you’d want that clarity as a customer.
Closing the Loop: This task completes the journey from creating an estimate to sending it, which is a core part of your job. It prepares you to give real customers accurate quotes, helping CC Inc. grow our business.
What’s Next?

You’ve now completed all the modules for Chapter 3! You’ve learned how to create Standard and Options Estimates in Markate, send them to customers, manage their status, and even see what it’s like to receive them. To finish Chapter 3, you’ll take a final quiz to test your understanding of everything we’ve covered. The quiz has 5 questions, and you need to get at least 4 correct (80%) to pass. If you don’t pass, you’ll need to review the modules and try again. I’ve prepared a reflection task to help you think about what you’ve learned in this module. Let’s do this!""",
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
