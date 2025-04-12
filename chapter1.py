#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
chapter1.py

This module contains the Chapter 1 training content for the CRM Training App, a 
Streamlit-based training platform for CC Inc. employees learning to use the Markate CRM.
It includes the CH1_MODULES list with modules and tasks, as well as the CH1_FINAL_QUIZ 
list for the final quiz questions. 
"""

################################################################
#            CHAPTER 1 MODULES & FINAL QUIZ (DETAILED)         #
################################################################
CH1_MODULES = [
    {
        "title": "Chapter 1, Module 1: What is a CRM and Why Do We Use Markate?",
        "content": """
**Welcome to Your First Day of Training at CC Inc.!**  
Hi there, and welcome to Chapter 1 of your training! You’re about to learn how to use Markate, a tool that will help you manage customers at CC Inc. Don’t worry if you’ve never used a CRM before—I’ll explain everything step-by-step, as if you’re starting from scratch. Let’s dive in!

**What is a CRM?**  
A CRM stands for *Customer Relationship Management*. Think of it like a super-organized digital notebook that helps businesses keep track of their customers. Imagine you’re running a lemonade stand, and you have a notebook where you write down:  
- Who your customers are (their names, phone numbers, emails).  
- Where they live (so you can deliver lemonade to their house).  
- What they’ve bought before (e.g., “John likes extra sugar”).  
- When you last talked to them (e.g., “Called Sarah last week to ask if she wants more lemonade”).

A CRM does all of that, but on a computer, and it’s much smarter! It can:  
- Store customer information (like names, emails, and addresses).  
- Send automatic messages (like reminders for a lemonade delivery).  
- Help you schedule jobs (like delivering lemonade to 10 houses on Monday).  
- Keep a history of everything (so you don’t forget what John ordered last time).

At CC Inc., we provide services like house washing, pest control, window washing, painting, and holiday lights. A CRM helps us keep track of all our customers so we can provide great service without losing track of anyone.

**Why Do We Use Markate at CC Inc.?**  
Markate is the CRM we use at CC Inc. It’s like a digital assistant that helps us manage our customers and make sure we’re providing the best service possible. Here’s why we chose Markate:  
- **It Keeps Everything Organized**: Markate stores all our customer information in one place. For example, if a customer calls and says, “I need my windows washed,” we can quickly look up their address and schedule the job.  
- **It Helps Us Communicate**: Markate can send emails and text messages to customers automatically. For example, if we schedule a house washing job, Markate can send the customer a message saying, “We’ll be at your house on Tuesday at 10 AM!”  
- **It Makes Scheduling Easy**: Many of our customers have more than one house—like a primary home and a vacation home. Markate lets us keep track of all their addresses, so we know exactly where to send our service teams.  
- **It Saves Time**: Instead of writing everything down on paper, Markate does the hard work for us. It’s like having a super-smart assistant who never forgets anything!

**What is a Staging Environment?**  
Before we start working with real customers, we’re going to practice in a special version of Markate called the *staging environment*. Think of it like a practice playground:  
- It’s a safe space where you can try things without affecting real customers.  
- If you make a mistake (like accidentally deleting a customer), it won’t cause any problems because it’s not real data.  
- It’s like practicing a video game in “training mode” before playing the real game—you can learn the controls without any pressure.

At CC Inc., we use the staging environment to help you get comfortable with Markate. For example, you’ll practice creating fake customers, so when you start working with real customers, you’ll know exactly what to do. The staging environment is at a special website: https://stg.markate.com/. We’ll learn how to log in during the next module.

**How Does This Fit into Your Role at CC Inc.?**  
As a sales rep at CC Inc., your job is to talk to customers, understand their needs, and set them up in Markate so our service teams can do their jobs (like washing houses or setting up holiday lights). Markate helps you:  
- Keep track of customer information, so you don’t lose important details.  
- Communicate with customers, so they know when we’re coming to their house.  
- Schedule services at the right address, even if they have multiple homes.

By learning Markate, you’re making sure CC Inc. can provide great service to every customer. In the next modules, we’ll learn how to log into Markate, create customer accounts, and even set up your own test account to see what it’s like to be a customer. Let’s get started!
        """,
        "task_type": "reflection",
        "task": "Reflection: In your own words, why do you think a staging environment is important for learning Markate? How do you think it will help you as a sales rep at CC Inc.?"
    },
    {
        "title": "Chapter 1, Module 2: Logging into Markate’s Staging Environment",
        "content": """
**Let’s Get Started with Markate!**  
Now that you know what a CRM is and why we use Markate at CC Inc., it’s time to log into the system and start practicing. In this module, we’ll learn how to access Markate’s staging environment—a safe place to practice without affecting real customers. I’ll walk you through every step, so don’t worry if you’ve never done this before!

**What You’ll Do in This Module**  
You’ll log into Markate’s staging environment using special test credentials. This will let you see the Markate dashboard, which is like the “home base” where you’ll do most of your work as a sales rep. The staging environment is a practice version of Markate, so you can try things without worrying about making mistakes.

**Steps to Log Into Markate’s Staging Environment**  
Follow these steps exactly as I describe them. If you get stuck, don’t worry—I’ll explain what to do!  
1. **Open Your Web Browser**: Use any browser you like (Google Chrome, Firefox, Safari, etc.). Think of a web browser as a window to the internet—it’s how you’ll visit the Markate website.  
2. **Go to the Staging Website**: In the address bar at the top of your browser (where you usually type things like “google.com”), type this exact address:  
   **https://stg.markate.com/**  
   Then press Enter on your keyboard. This will take you to Markate’s staging environment.  
   - **What’s That Address Again?** The “https://” part means it’s a secure website. The “stg” part means it’s the staging (practice) version of Markate. If you accidentally go to “https://app.markate.com/,” that’s the real system, and we don’t want to practice there!  
3. **Enter the First Login (Pre-Prompt)**: When you get to the website, a small window will pop up in the top middle of your screen asking for a username and password. This is called the “pre-prompt login.” Enter these details:  
   - **Username**: Markate  
   - **Password**: crm4you  
   Type them exactly as shown—they’re case-sensitive, so “Markate” needs a capital “M,” and “crm4you” is all lowercase. Then click the “Login” button in the top right corner of the screen.  
   - **What If It Doesn’t Work?** If the login doesn’t work, double-check that you typed the username and password correctly. Make sure there are no extra spaces, and that “Markate” has a capital “M.” If it still doesn’t work, let me know, and I’ll help you!  
4. **Enter the Second Login (Dashboard)**: After the first login, you’ll see a new page asking for another set of credentials. This is the “dashboard login,” which takes you to the main Markate system. Enter these details:  
   - **Email**: support@xecutetech.com  
   - **Password**: Windows4  
   Again, type them exactly as shown—“support@xecutetech.com” is all lowercase, and “Windows4” has a capital “W.” Then click the “Login” button.  
   - **Why Two Logins?** The first login (pre-prompt) is like a “front door” to make sure you’re allowed into the staging environment. The second login (dashboard) is like a “key” to the main system, where you’ll do your work. It’s a little extra security to keep things safe.  
5. **Welcome to the Markate Dashboard!**: If you entered everything correctly, you’ll see the Markate dashboard. This is the main screen where you’ll do most of your work as a sales rep. It’s like the control center of Markate—you’ll see menus at the top (like “Sales” and “Leads”), and you’ll use these to manage customers and leads.

**Why This Matters for You**  
- **Access is the First Step**: You can’t do your job as a sales rep if you can’t get into Markate. Learning to log in is the first step to managing customers and leads.  
- **Practice Makes Perfect**: The staging environment lets you practice without risking real customer data. For example, if you accidentally mess up a customer’s information, it won’t cause any problems because it’s not real.  
- **Builds Confidence**: Logging in might feel tricky at first, but the more you do it, the easier it gets. By the time you start working with real customers, you’ll be a pro at getting into Markate!

**Pro Tip**: Always double-check the website address (https://stg.markate.com/) to make sure you’re in the staging environment. If you see “https://app.markate.com/,” that’s the real system, and we don’t want to practice there. Also, write down the login credentials (Markate/crm4you and support@xecutetech.com/Windows4) somewhere safe—you’ll use them every time you log in to practice.

**What’s Next?**  
Now that you know how to log into Markate, the next module will teach you how to find the “Customers” page, where you’ll start creating customer accounts. Let’s keep going!
        """,
        "task_type": "scenario",
        "task": """
**Scenario**: You’re trying to log into Markate’s staging environment, but you typed the wrong password for the pre-prompt login. What should you do?  
A) Keep trying random passwords until something works.  
B) Double-check the instructions and use the correct credentials (Username: Markate, Password: crm4you).  

Select the correct answer and explain why in the box below.
        """,
        "options": [
            "A) Keep trying random passwords until something works.",
            "B) Double-check the instructions and use the correct credentials (Username: Markate, Password: crm4you)."
        ],
        "correct_answer": 1
    },
    {
        "title": "Chapter 1, Module 3: Navigating to the Customers Page in Markate",
        "content": """
**Let’s Explore Markate Together!**  
Great job logging into Markate’s staging environment! Now that you’re on the Markate dashboard, it’s time to learn how to find the “Customers” page, where you’ll create and manage customer accounts. I’ll guide you through every step, and I’ll explain why this page is so important for your role at CC Inc.

**What You’ll Do in This Module**  
You’ll learn how to navigate to the “Customers” page in Markate, which is where you’ll create new customer accounts. This page is like a big list of all the customers CC Inc. works with (or in our case, fake customers, since we’re in the staging environment). You’ll also learn some key concepts, like the difference between a “Billing Address” and a “Service Address,” so you’re ready to start creating customers in the next module.

**Steps to Navigate to the Customers Page**  
Let’s walk through this together, step-by-step:  
1. **Make Sure You’re on the Markate Dashboard**: You should already be logged into the staging environment from the last module. If you’re not, go back to Module 2 and follow the login steps (https://stg.markate.com/, Username: Markate, Password: crm4you, then Email: support@xecutetech.com, Password: Windows4). You’ll know you’re on the dashboard because you’ll see a menu bar at the top with options like “Sales,” “Leads,” and “Customers.”  
2. **Find the “Sales” Tab**: Look at the top of the screen. You’ll see a menu with several options, like “Sales,” “Leads,” “Schedule,” and more. Find the one that says “Sales.” It’s usually one of the first options on the left.  
   - **What Does “Sales” Mean?** In Markate, the “Sales” tab is where you manage everything related to customers and leads (people who might become customers). It’s called “Sales” because your job as a sales rep is to help turn leads into customers and manage their accounts.  
3. **Hover Over the “Sales” Tab**: Move your mouse cursor over the word “Sales” (don’t click yet!). When you hover over it, a dropdown menu will appear with more options. A dropdown menu is like a little list that pops up—it’s a way to show more choices without taking up too much space on the screen.  
4. **Click on “Customers”**: In the dropdown menu, you’ll see several options, like “Customers,” “Leads,” “Estimates,” and more. Find the one that says “Customers” and click on it.  
   - **What If I Don’t See “Customers”?** If you don’t see “Customers” in the dropdown menu, make sure you’re hovering over “Sales” and not another tab like “Leads.” If you still don’t see it, try refreshing the page by pressing F5 on your keyboard, or log out and log back in.  
5. **Welcome to the Customers Page!**: After clicking “Customers,” you’ll be taken to the Customers page. This page shows a list of all the customers in Markate (in the staging environment, these are fake customers created for practice). It’s like a big address book, but with extra features to help you manage customer information. You’ll see columns like “Name,” “Email,” “Phone,” and more, showing details for each customer.

**Understanding the Customers Page**  
Now that you’re on the Customers page, let’s talk about what you’re seeing and why it’s important:  
- **List of Fake Customers**: Since we’re in the staging environment, the customers you see here aren’t real—they’re test accounts created for practice. For example, you might see names like “John Doe” or “Jane Smith” with fake emails and phone numbers. This lets you practice without affecting real customer data.  
- **Customer Details**: Each customer in the list has details like their name, email, phone number, and address. These details help you know who they are and where they need services. For example, if a customer calls and says, “I need pest control,” you can look them up on this page to see their address and schedule the job.  
- **Why This Page Matters**: The Customers page is where you’ll do a lot of your work as a sales rep. You’ll use it to:  
  - Create new customer accounts (which we’ll learn in the next module).  
  - Look up existing customers to see their information.  
  - Update customer details if something changes (like a new phone number).

**Key Concept: Billing Address vs. Service Address**  
Before we start creating customers, there’s an important concept you need to understand: the difference between a “Billing Address” and a “Service Address.” This will come up a lot when you create customer accounts, so let’s break it down:  
- **Billing Address**: This is the address where a customer would get their bill (like an invoice for services). But at CC Inc., we don’t send paper bills through the mail—we send everything by email or text. Because of this, we use the “Billing Address” field in Markate to mean the same thing as the “Service Address.”  
- **Service Address**: This is the address where we’ll actually provide services (like washing a house or setting up holiday lights). For most customers, their Billing Address and Service Address are the same—it’s the house where they live. But some customers have more than one house, like a primary home and a vacation home. In those cases, we’ll add extra Service Addresses to keep track of all their properties.  
- **Why This Matters**: When you create a customer in Markate, you’ll enter their Billing Address, which we treat as their main Service Address. If they have more houses (like a vacation home), you’ll add those as extra Service Addresses later. This ensures our service teams know exactly where to go for each job. For example, if a customer says, “I need my vacation home cleaned,” you’ll look in Markate to find the right address for that house.

**How This Fits into Your Role at CC Inc.**  
As a sales rep, you’ll spend a lot of time on the Customers page in Markate. It’s where you’ll create new customer accounts, look up existing customers, and make sure their information is correct. Getting comfortable with this page is a big step toward doing your job well. In the next module, we’ll learn how to create a new customer account, so you’ll get to practice using this page!

**Pro Tip**: When you’re on the Customers page, take a moment to look around. You’ll see a green “+ New Customer” button in the top right corner—that’s what we’ll use in the next module to create a new customer. For now, just get familiar with the layout of the page, so you know where to find things when we start creating customers.
        """,
        "task_type": "reflection",
        "task": "Reflection: Why do you think it’s important to understand the difference between a Billing Address and a Service Address? How do you think this will help you when working with customers at CC Inc.?"
    },
    {
        "title": "Chapter 1, Module 4: Creating Basic Residential Customers (25 Entries)",
        "content": """
**Let’s Create Your First Customer in Markate!**  
Now that you know how to log into Markate and find the Customers page, it’s time to start creating customer accounts! In this module, we’ll learn how to create a *basic residential customer* in Markate’s staging environment. A residential customer is an individual person (not a business) who needs services at their home, like house washing or pest control. We’ll create 25 of these customers to practice, and I’ll explain every step in detail so you feel confident doing it.

**What You’ll Do in This Module**  
You’ll create 25 basic residential customers in Markate’s staging environment. “Basic” means these customers will have just one address (their main home) and no extra contacts (like a spouse). We’ll use fake information since we’re practicing, and I’ll teach you some important rules about how to fill in the customer details. By the end of this module, you’ll be ready to create more complex customers in the next module.

**What is a Residential Customer?**  
A residential customer is a person who needs services at their home. At CC Inc., most of our customers are residential—they might need house washing, pest control, window washing, painting, or holiday lights. For example:  
- John Doe might need his house washed at 123 Test Street.  
- Sarah Smith might want holiday lights at her home in City, State.  
As a sales rep, your job is to create a customer account for them in Markate, so our service teams know where to go and how to contact them.

**Why Do We Create Customer Accounts in Markate?**  
Creating a customer account in Markate is like adding a new person to your address book, but with extra details to help CC Inc. provide great service. Here’s why it’s important:  
- **We Need Their Information**: We need to know their name, email, phone number, and address so we can contact them and send our service teams to the right place.  
- **We Need to Communicate**: Markate can send emails and text messages to customers, like “Your house washing is scheduled for Tuesday!” We need their contact info to do this.  
- **We Need to Schedule Services**: The address we enter in Markate tells our service teams where to go. If we don’t have the right address, they might show up at the wrong house!  
- **We Need to Keep Track**: Markate keeps a history of every customer, so we can see what services they’ve had before. For example, if John Doe had pest control last year, we can look it up and ask if he wants it again.

**Steps to Create a Basic Residential Customer in Markate**  
Let’s create your first customer account together. Follow these steps exactly, and I’ll explain why each step matters:  
1. **Make Sure You’re on the Customers Page**: You should already be logged into Markate’s staging environment (https://stg.markate.com/, Username: Markate, Password: crm4you, then Email: support@xecutetech.com, Password: Windows4). If you’re not on the Customers page, go back to Module 3 and follow the steps to get there (Sales → Customers).  
2. **Click the “+ New Customer” Button**: On the Customers page, look in the top right corner of the screen. You’ll see a green button that says “+ New Customer.” Click on it to start creating a new customer.  
   - **What Does This Button Do?** Clicking “+ New Customer” opens a form where you’ll enter the customer’s information. It’s like opening a blank page in your address book to add a new person.  
3. **Set the Customer Type to “Residential”**: At the top of the form, you’ll see a dropdown menu labeled “Customer Type.” Click on it and select “Residential.”  
   - **Why Residential?** This tells Markate that we’re creating an account for an individual person, not a business. We’ll learn about business (commercial) customers later in Module 6.  
4. **Fill in the Required Information**: Now you’ll enter the customer’s details. Since we’re in the staging environment, we’ll use fake information to practice. Here’s what to enter:  
   - **First Name & Last Name**: Use any fake name you want. For example, “John Doe” or “Sarah Smith.” This is the customer’s name, so we know who they are.  
     - **Example**: First Name: John, Last Name: Doe.  
   - **Email**: Use the format firstname@example.com. For example, if the customer’s name is John Doe, their email should be john@example.com.  
     - **Why This Format?** We use firstname@example.com for all fake customers in the staging environment to keep things consistent. It’s like giving every practice customer a pretend email address that follows the same pattern. In the real system, you’d use the customer’s actual email, like john.doe@gmail.com.  
   - **Mobile Phone**: Use the format 555-XXXXXXX, where XXXXXXX is any 7 digits. For example, 555-123-4567.  
     - **Why This Format?** We use 555-XXXXXXX for all fake phone numbers in the staging environment to keep things consistent. The “555” part is a pretend area code often used in movies and TV shows for fake numbers. In the real system, you’d use the customer’s actual phone number, like 123-456-7890.  
   - **Preferred Notification Method**: Select “Both Email & Text” from the dropdown menu.  
     - **Why Both Email & Text?** This ensures the customer gets all important updates from CC Inc., like scheduling confirmations (“We’ll be at your house on Tuesday!”), estimates (“Here’s the cost for your house washing”), and overdue invoices (“You have a payment due”). Some customers prefer email, others prefer text, but we choose both to make sure they don’t miss anything. This is really important for keeping customers happy—if they miss a message, they might not know when we’re coming, and that could cause problems!  
   - **Billing Address**: Use a fake address, like “123 Test Street, City, State, ZIP.” For example, 123 Test Street, Springfield, IL, 62704.  
     - **Why Do We Need This?** At CC Inc., we don’t send paper bills through the mail—we send everything by email or text. Because of this, we use the “Billing Address” field in Markate to mean the same thing as the “Service Address.” This is the address where we’ll provide services, like washing their house or setting up holiday lights. For a basic residential customer, this is their main home address.  
     - **Why Is This Important?** Getting the address right ensures our service teams go to the correct place. For example, if John Doe lives at 123 Test Street, that’s where we’ll send our house washing team. If the address is wrong, they might go to the wrong house, and that would be a big problem!  
   - **Comments**: Add a note like “Test customer - created for training purposes.”  
     - **Why Add a Comment?** This helps us keep track of which customers are fake (for practice) and which are real. In the staging environment, all customers are fake, so we add this note to remind ourselves. In the real system, you might use the Comments field to add extra information, like “Customer prefers morning appointments” or “Has a big dog in the yard.”  
5. **Ignore These Sections for Now**: You’ll see other sections in the form, like “Additional Contacts” and “Additional Service Addresses.” Ignore these for now—we’ll learn about them in the next module when we create advanced residential customers.  
6. **Click “Save” to Create the Customer**: At the bottom of the form, you’ll see a “Save” button. Click it to add the customer to Markate.  
   - **What Happens When You Click Save?** The customer will be added to the list on the Customers page. You’ll see their name (e.g., John Doe) in the list, along with their email, phone number, and address. This means they’re now in Markate, and you can schedule services for them!  
7. **Repeat This Process 25 Times**: To get comfortable with creating customers, you’ll create 25 basic residential customers. Each time, use a different fake name, email, and address, but follow the same rules (firstname@example.com, 555-XXXXXXX, Both Email & Text). For example:  
   - Customer 1: John Doe, john@example.com, 555-123-4567, 123 Test Street, Springfield, IL, 62704.  
   - Customer 2: Sarah Smith, sarah@example.com, 555-234-5678, 456 Fake Avenue, Chicago, IL, 60601.  
   - Customer 3: Mike Johnson, mike@example.com, 555-345-6789, 789 Practice Road, Miami, FL, 33101.  
   And so on, until you’ve created 25 customers.  
   - **Why 25 Times?** Doing this 25 times helps you practice the process so it becomes second nature. By the time you’re done, you’ll be able to create a customer account quickly and confidently, which is a big part of your job as a sales rep.
        """,
        "task_type": "miniquiz", 
        "miniquiz_questions": [
            {
                "question": "What should you set the Preferred Notification Method to when creating a customer?",
                "options": [
                    "Email only",
                    "Text only",
                    "Both Email & Text"
                ],
                "correct_answer": 2
            },
            {
                "question": "Why do we use the Billing Address as the Service Address at CC Inc.?",
                "options": [
                    "Because we send paper bills to that address.",
                    "Because we don’t send paper bills, so we use it as the service location.",
                    "Because it’s required by Markate."
                ],
                "correct_answer": 1
            }
        ]
    },
    {
        "title": "Chapter 1, Module 5: Creating Advanced Residential Customers (10 Entries)",
        "content": """
**Let’s Take It Up a Notch: Advanced Residential Customers!**  
Great job creating 25 basic residential customers in Markate! You’re getting the hang of this. Now, let’s learn how to create *advanced* residential customers. These are customers who need a bit more setup because they have extra contacts (like a spouse or property manager) or multiple houses (like a vacation home). At CC Inc., only about 3% of our residential customers need this setup, but it’s important to know how to handle these cases because they can be more complicated. I’ll walk you through every step, just like before!

**What You’ll Do in This Module**  
You’ll create 10 advanced residential customers in Markate’s staging environment. “Advanced” means these customers will have:  
- An additional contact (like a spouse, property manager, or assistant).  
- An additional service address (like a vacation home or rental property).  
We’ll use fake information again, and I’ll explain some new concepts, like why we name service addresses and why additional contacts don’t get notifications. By the end of this module, you’ll be ready to create commercial customers (businesses) in the next module.

**What is an Advanced Residential Customer?**  
An advanced residential customer is still an individual person (not a business), but they have more complex needs. Here are some examples:  
- **John and Jane Doe**: John is the main contact, but his spouse Jane also manages their house. We need to add Jane as an additional contact so we can reach her if John isn’t available.  
- **Sarah Smith with a Vacation Home**: Sarah lives at 123 Test Street, but she also has a vacation home at 456 Secondary Street. We need to add her vacation home as an extra service address so we can schedule services there if needed.  
At CC Inc., most customers are “basic” (just one address, no extra contacts), but about 3% are “advanced” because they have extra contacts or multiple properties. Knowing how to handle these customers ensures we can provide great service, no matter how complicated their needs are.

**How to Create an Advanced Residential Customer in Markate**  
Let’s create an advanced residential customer together. This builds on what you learned in Module 4, but with a few extra steps. Follow along carefully:  
1. **Start Like a Basic Customer**: Follow the same steps you learned in Module 4 to create a basic residential customer:  
   - Go to the Customers page (Sales → Customers).  
   - Click the green “+ New Customer” button.  
   - Set the Customer Type to “Residential.”  
   - Fill in the basic fields:  
     - First Name & Last Name: Any fake name (e.g., John Doe).  
     - Email: firstname@example.com (e.g., john@example.com).  
     - Mobile Phone: 555-XXXXXXX (e.g., 555-123-4567).  
     - Preferred Notification Method: Both Email & Text.  
     - Billing Address: 123 Test Street, City, State, ZIP.  
     - Comments: “Test customer - created for training purposes.”  
   So far, this is exactly the same as creating a basic customer. Now, let’s add the “advanced” parts.  
2. **Add an Additional Contact**: In the customer form, scroll down until you see a section called “Additional Contacts.” This is where you’ll add a secondary person who helps manage the customer’s property, like a spouse, property manager, or assistant.  
   - Click the button to add a new contact (it might say something like “+ Add Contact”).  
   - Fill in these details:  
     - **Name**: Use a fake name for the additional contact (e.g., Jane Doe).  
     - **Email**: Use firstname@example.com (e.g., jane@example.com).  
     - **Phone**: Use 555-XXXXXXX (e.g., 555-987-6543).  
     - **Notes**: Add a comment like “Spouse managing property.”  
   - **Important Note About Notifications**: Additional contacts do *not* get email or text notifications automatically. Only the main contact gets texts. However, when we send an invoice, we can manually choose to email the additional contact.  
3. **Add an Additional Service Address**: Now, scroll down to the “Service Addresses” section in the form. This is where you’ll add a second address if the customer has more than one property.  
   - Click the button to add a new service address (it might say “+ New Service Address”).  
   - Fill in these details:  
     - **Address**: Use a fake address for the second property (e.g., 456 Secondary Street, City, State, ZIP).  
     - **Suite/Unit**: Leave blank unless needed.  
     - **City, Zip, State**: Fill in as needed.  
     - **Access Code**: If the property has a gate or door code, add it or leave blank.  
     - **Contact Name (Most Important!)**: This is the name of the property in Markate. For example, “Lakehouse” or “Vacation Home.”  
   - **Why Name It?** Naming the service address is crucial so we know which location is which. If the customer says, “Clean my vacation home,” we’ll know which address to pick.  
4. **Click “Save” to Create the Customer**: Once you’ve added the additional contact and service address, click “Save.”  
5. **Repeat This Process 10 Times**: Create 10 advanced residential customers. For each one, add at least one additional contact and one additional service address.  

By the time you’re done, you’ll be ready for commercial customers next!
        """,
        "task_type": "scenario",
        "task": """
**Scenario**: A customer named Sarah Smith calls and says her spouse, Mike Smith, will manage their vacation home at 789 Pine Lane. Where should you add Mike’s information, and where should you add the vacation home?  
A) Add Mike in the Billing Address field, and put the vacation home in the Comments section.  
B) Add Mike as an Additional Contact, and create a new Service Address named “Vacation Home” for 789 Pine Lane.  
C) Add Mike in the Service Addresses section, and create a new Billing Address for 789 Pine Lane.  

Select the correct answer and explain why in the box below, thinking about how this setup helps CC Inc. provide services.
        """,
        "options": [
            "A) Add Mike in the Billing Address field, and put the vacation home in the Comments section.",
            "B) Add Mike as an Additional Contact, and create a new Service Address named “Vacation Home” for 789 Pine Lane.",
            "C) Add Mike in the Service Addresses section, and create a new Billing Address for 789 Pine Lane."
        ],
        "correct_answer": 1
    },
    {
        "title": "Chapter 1, Module 6: Creating Commercial Customers (15 Entries)",
        "content": """
**Let’s Learn About Commercial Customers!**  
You’re doing great so far! You’ve learned how to create basic and advanced residential customers in Markate, which covers most of the people we work with at CC Inc. Now, let’s learn about a different type of customer: *commercial customers*. These are businesses (not individuals) that need our services, often at multiple locations. I’ll explain everything you need to know, and we’ll create 15 commercial customers in Markate’s staging environment to practice.

**What is a Commercial Customer?**  
A commercial customer is a business that needs services from CC Inc. Unlike residential customers (who are individual people), commercial customers are companies, and they often have more complex needs. Here are some examples:  
- **Johnson Corp**: A property management company that needs house washing at three apartment buildings.  
- **Sunny Resort**: A resort that wants holiday lights set up at their main office and two guest buildings.  
- **Green Lawn Co.**: A lawn care company that subcontracts CC Inc. to do pest control at a construction site.

**How Are Commercial Customers Different?**  
- They’re Businesses, Not People.  
- They Often Have Multiple Locations.  
- They Might Have Different Points of Contact.  
- Mistakes Are More Serious (affects larger accounts).

**How to Create a Commercial Customer in Markate**  
Follow the steps below, similar to residential, but choose “Commercial” for the Customer Type. Remember to add service addresses for each business location.

**Practice**: Create 15 commercial customers. For each one, add multiple service addresses if needed, and use a fake business name (e.g., “Johnson Corp”).  

By the time you’re done, you’ll be an expert at creating customers in Markate!
        """,
        "task_type": "scenario",
        "task": """
**Scenario**: A property management company called Johnson Corp needs house washing at three apartment buildings. What Customer Type should you select, and why is naming each service address important?  
A) Select Residential, to keep it simple, and put all addresses in the Comments section.  
B) Select Commercial, and create separate Service Addresses named “Building A,” “Building B,” and “Building C” for each location.  
C) Select Group, to organize by region, and use the same address for all locations.  

Select the correct answer and explain why in the box below, thinking about how this setup helps CC Inc. deliver services to a business.
        """,
        "options": [
            "A) Select Residential, to keep it simple, and put all addresses in the Comments section.",
            "B) Select Commercial, and create separate Service Addresses named “Building A,” “Building B,” and “Building C” for each location.",
            "C) Select Group, to organize by region, and use the same address for all locations."
        ],
        "correct_answer": 1
    },
    {
        "title": "Chapter 1, Module 7: Creating Your Own Test Account",
        "content": """
**Let’s See Markate from the Customer’s Side!**  
You’ve done an amazing job so far! You’ve learned how to log into Markate, create residential and commercial customers, and even add advanced details like extra contacts and service addresses. Now, let’s do something a little different: you’re going to create a test account for *yourself* in Markate. This will let you see what it’s like to be a customer, which will help you understand how Markate works from their perspective. Let’s go!

**Steps**:  
1. Go to Customers page.  
2. Click “+ New Customer” -> Choose Residential.  
3. Enter your own name (or a test version of it).  
4. Use a fake phone/email (or your actual if you want, but it won’t really send in staging).  
5. Save.  

Then you’ll see yourself in the Customers list! This helps you see how customers appear in Markate. 
        """,
        "task_type": "reflection",
        "task": "Reflection: Why do you think it’s useful to create a test account with your own details? How do you think seeing Markate from the customer’s side will help you as a sales rep at CC Inc.?"
    }
]

CH1_FINAL_QUIZ = [
    {
        "question": "Why do we always select 'Both Email & Text' for the Preferred Notification Method when creating a customer in Markate?",
        "options": [
            "Because it’s faster to send both.",
            "To ensure customers get all updates and don’t miss important messages.",
            "Because Markate requires it for all customers."
        ],
        "answer": 1
    },
    {
        "question": "What is the main difference between a Billing Address and a Service Address for a residential customer at CC Inc.?",
        "options": [
            "The Billing Address is where we send paper bills, and the Service Address is where we provide services.",
            "There is no difference—we use the Billing Address as the Service Address since we don’t send paper bills.",
            "The Billing Address is for commercial customers only, and the Service Address is for residential customers."
        ],
        "answer": 1
    },
    {
        "question": "A customer has a vacation home in addition to their primary home. Where should you record the vacation home in Markate?",
        "options": [
            "Put it in the Comments section.",
            "Create a new Service Address with a name like 'Vacation Home.'",
            "Use the same Billing Address for both homes."
        ],
        "answer": 1
    },
    {
        "question": "Why must every Service Address have a name (e.g., 'Lakehouse' or 'Johnson Warehouse') in Markate?",
        "options": [
            "To make it more fun for the customer.",
            "Because customers like to name their properties.",
            "To track work orders and invoices, so we know which location a job is for."
        ],
        "answer": 2
    },
    {
        "question": "What should you do if a commercial customer needs services at multiple locations?",
        "options": [
            "Put all locations in the Billing Address field.",
            "Create separate Service Addresses for each location, with unique names.",
            "Create a new customer account for each location."
        ],
        "answer": 1
    }
]
