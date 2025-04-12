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
- **They Bring in New Business**: Every new customer starts as a lead. For example, if someone calls and says, “I need my windows washed,” that’s a lead, and if you turn them into a customer, CC Inc. gets a new job!  
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
  - **Finding New Leads**: It’s everyone’s job at CC Inc. to bring in new leads, whether it’s through phone calls, website inquiries, referrals, or repeat customers asking for new services. For example, if you meet someone at a community event who says, “I might need my house washed,” you’ll add them as a new lead in Markate.  
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
- **Use Pipeline View When**: You want to see the big picture and move leads between stages. For example, if you’re planning your day and want to see how many leads are in each stage, Pipeline View is perfect. It’s also great for dragging leads to a new stage after you take action, like moving a lead from “New” to “Scheduled” after setting up a meeting.  
- **Use Table View When**: You need to find specific leads or sort them in a certain way. For example, if you want to see all the leads that are “Waiting for Response,” Table View makes it easy to filter and find them. It’s also helpful for seeing detailed info, like a lead’s phone number or notes, without having to click into each lead.

As you get more comfortable with Markate, you’ll figure out which view you prefer for different tasks. Some sales reps like Pipeline View for planning their day, while others prefer Table View for digging into details. You can switch between them anytime, so feel free to experiment!

**Why This Matters for You**  
- **Stay Organized**: Both Pipeline View and Table View help you keep track of your leads, so you always know what to do next. For example, Pipeline View shows you how many leads are waiting for you to contact them, while Table View lets you filter for leads that need a follow-up.  
- **Work Efficiently**: Knowing how to use both views lets you work faster and smarter. For example, if you need to call all the leads in the “New” stage, you can use Table View to sort them and get their phone numbers quickly.  
- **Understand the Process**: Seeing leads in different stages (like “New” or “Scheduled”) helps you understand the process of turning a lead into a customer. This will make you better at managing leads and closing deals.

**How This Fits into Your Role at CC Inc.**  
As a sales rep, you’ll spend a lot of time in the Leads section of Markate, and knowing how to view your leads is the first step to managing them. Pipeline View and Table View are tools to help you:  
- **See What’s Happening**: You’ll use these views to see where each lead is in the process, so you know what to do next. For example, if you see a lead in “New,” you’ll know to contact them. If you see a lead in “Waiting for Response,” you’ll know to follow up.  
- **Prioritize Your Work**: With Pipeline View, you can quickly see which stages have the most leads, so you can focus on what’s most important. For example, if the “New” stage is full, you’ll know to spend your day contacting those leads.  
- **Find Information Fast**: With Table View, you can sort and filter to find specific leads, which saves you time. For example, if you need to call all the leads who are waiting for a response, you can filter the list and get their phone numbers in seconds.

**What’s Next?**  
In the next module, we’ll dive deeper into the 7 stages of managing leads at CC Inc. You’ll learn what each stage means and how to move leads through them, so you can turn them into customers. To make sure you understand the difference between Pipeline View and Table View, I’ve prepared a reflection task for you. Let’s do this!
""",
        "task_type": "reflection",
        "task": "Reflection: Which view do you think you’ll use more as a sales rep—Pipeline View or Table View—and why? How do you think these views will help you manage your leads at CC Inc.?"
    },
    {
        "title": "Chapter 2, Module 3: The 7 Stages of Leads at CC Inc.",
        "content": """
**Let’s Learn the 7 Stages of Managing Leads!**  
Now that you know how to view leads in Markate using Pipeline View and Table View, it’s time to learn the process we use to manage them at CC Inc. We move leads through 7 stages in Markate, from the moment they show interest to the moment they become a customer (or decide not to). I’ll explain each stage in detail, what you need to do, and why it’s important. Let’s dive in!

**What You’ll Do in This Module**  
You’ll learn about the 7 stages of managing leads at CC Inc., which you’ll see in Markate’s Pipeline View. You’ll understand what each stage means, what actions you need to take, and how to move leads from one stage to the next. This will help you turn leads into customers and keep CC Inc.’s business growing.

**The 7 Stages of Leads at CC Inc.**  
At CC Inc., we use a specific process to manage leads in Markate, moving them through 7 stages. Each stage represents a step in the journey from “interested” to “customer.” Here’s what each stage means, what you do, and why it matters:

1. **New**  
   - **What It Means**: This is where all leads start. A lead goes into the “New” stage as soon as they show interest in our services. They could come from a phone call (“I need a quote for house washing”), a website inquiry (“I filled out a form online”), a referral (“My friend told me about CC Inc.”), or a repeat customer asking for a new service (“I want pest control this time”).  
   - **What You Do**: Your job is to keep this bucket full—it’s everyone’s responsibility at CC Inc. to bring in new leads. For example, if you meet someone who says, “I might need my windows washed,” you’ll add them as a new lead in Markate (we’ll learn how in the next module). For now, just know that “New” is the starting point for every lead.  
   - **Why It Matters**: The “New” stage is like the fuel for our business—if we don’t have new leads coming in, we won’t have new customers. Keeping this bucket full ensures CC Inc. always has potential business to work on.

2. **Assigned**  
   - **What It Means**: This stage is for leads that need immediate attention from a sales rep (like you!). A lead moves to “Assigned” when someone at CC Inc. decides a sales rep needs to follow up.  
   - **What You Do**: As a sales rep, you’ll be assigned leads to contact. Your goal is to act quickly—within 24 hours. For example, if a lead says, “I need a quote for house washing,” you’ll call them to set up a meeting or send them a quote. Once you take action, you’ll move the lead to the next stage (like “Scheduled” or “Attempted to Contact”). This bucket should stay empty—assigned leads need to be handled fast!  
     - **Note**: If a lead is meant for someone else at CC Inc. (like Casey or another staff member, not a sales rep), it won’t be assigned to you. For example, if a lead needs an admin to handle paperwork, they’ll be assigned to the admin instead.  
   - **Why It Matters**: Acting quickly on assigned leads shows the customer we’re serious about helping them. If we wait too long, they might go to a competitor, and we’ll lose the business. Keeping this bucket empty ensures leads don’t sit around waiting.

3. **Attempted to Contact**  
   - **What It Means**: This stage is for leads you’ve tried to contact but couldn’t reach. For example, if you called a lead but they didn’t answer, or if there’s an issue (like a wrong number or they’re unavailable), you move them here.  
   - **What You Do**: When you move a lead to this stage, you *must* add notes in Markate to explain what happened. For example, you might write, “Called and left voicemail at 1:30 PM on 5/12/25.” This helps everyone at CC Inc. know what’s going on with the lead. You’ll also decide what to do next—maybe try calling again at a different time or send an email.  
   - **Why It Matters**: This stage helps you track leads that need extra effort to reach. For example, if you called at 1:30 PM and they didn’t answer, your note might remind you to try again in the evening when they’re more likely to be free. It keeps us organized and ensures no lead gets forgotten.

4. **Scheduled**  
   - **What It Means**: This stage is for leads you’ve successfully scheduled for a meeting or appointment. For example, if a lead says, “I’d like to meet to discuss pest control,” and you set up a meeting for next Tuesday, they move to “Scheduled.”  
   - **What You Do**: Once you schedule the meeting, Markate will automatically move the lead to this stage (you’ll learn how to do this in a later module). Your job is to prepare for the meeting—get ready to talk about CC Inc.’s services, answer their questions, and make a great impression. As we like to say at CC Inc., “Show up, shake hands, kiss babies, and do your thing!” This means being friendly, professional, and ready to help the customer.  
   - **Why It Matters**: Scheduling a meeting is a big step toward turning a lead into a customer—it means they’re serious enough to talk to you. A good meeting can convince them to choose CC Inc., so this stage is your chance to shine as a sales rep.

5. **Estimation / Waiting for Response**  
   - **What It Means**: This stage is for leads you’ve sent a quote (also called an estimate) to. For example, if a lead says, “I need a quote for house washing,” you’ll meet with them, figure out the cost, and send them the quote. Once you send the quote, Markate automatically moves the lead to this stage.  
   - **What You Do**: Your job is to wait for the customer to respond—they might say yes, no, or need more time to decide. Many leads will sit in this stage for a while as they think it over. You should check this bucket often (using Pipeline View or Table View) and follow up on quotes that haven’t been accepted yet. For example, if a lead hasn’t responded after a week, you might call them to see if they have any questions.  
   - **Why It Matters**: This stage is where leads decide whether to become customers. Following up shows the customer you care about their decision, which can make them more likely to say yes. If you don’t follow up, they might forget about the quote or choose a competitor.

6. **First Follow-Up**  
   - **What It Means**: This stage is for leads you’ve followed up with for the first time after sending a quote. For example, if a lead hasn’t responded to your quote after a week, you’ll call or email them to check in, and then move them to this stage.  
   - **What You Do**: When you follow up, you’ll ask if they’re ready to proceed with the service. For example, you might say, “Hi John, I wanted to check if you had any questions about the house washing quote I sent you. Are you ready to schedule the service?” Some customers might say yes, some might say no, and others might need more time. Add notes in Markate to keep track of what they say (e.g., “John said he needs another week to decide”). Your goal is to keep the conversation going.  
   - **Why It Matters**: Following up shows the customer you’re interested in helping them, which can make them more likely to choose CC Inc. Many customers need a little nudge to make a decision, and this stage ensures we don’t let leads slip away.

7. **Second Follow-Up**  
   - **What It Means**: This stage is for leads you’ve followed up with a second time after the first follow-up. If a lead is still undecided after your first follow-up, you’ll follow up again and move them here. This is the final follow-up before the lead either becomes a customer or decides not to buy.  
   - **What You Do**: Follow up one more time to see if the customer is ready to proceed. For example, you might say, “Hi John, I just wanted to check in one last time about the house washing quote. Are you ready to move forward, or do you have any other questions?” Add notes in Markate about their response (e.g., “John said he’s not interested right now but might need services later”).  
   - **Why It Matters**: This stage gives the customer one last chance to say yes, which can help us close more deals. It also ensures we don’t give up on leads too early—sometimes a second follow-up is all it takes to turn a lead into a customer.

**What Happens After the Second Follow-Up?**  
After the second follow-up, a lead will either become a customer or decide not to buy. Here’s what happens:  
- **If They Say Yes**: Great! You’ll create a customer account for them in Markate (like you learned in Chapter 1) and schedule the service. They’re no longer a lead—they’re now a customer.  
- **If They Say No**: We don’t delete leads, even if they say no. Instead, they stay in the “Second Follow-Up” stage, and we convert them into a customer account in Markate. This way, we have their information for future reference and can use it for marketing other services later. For example, if John says, “I don’t need house washing right now,” we’ll keep his info and might contact him later about pest control or holiday lights.  
  - **Note**: If a customer doesn’t want to receive marketing emails, they can opt out themselves. We don’t remove their info unless they specifically ask us to.  
- **Why Keep Their Info?** Even if a lead says no, they might change their mind later or need a different service. Keeping their info lets us reach out in the future, which can lead to more business for CC Inc.

**Final Notes on the 7 Stages**  
Here are some key things to remember as you manage leads through these stages:  
- **Every Lead Goes Through This Process**: Whether it’s a new customer or an existing one, every lead moves through these 7 stages. It’s a consistent process that helps us stay organized.  
- **Don’t Let Leads Get Stuck**: Your job is to keep leads moving through the stages—don’t let them sit in one stage for too long. For example, if a lead is in “Waiting for Response” for weeks, follow up to see if they’re ready to decide. If they’re in “Attempted to Contact,” try again at a different time. Keeping leads moving ensures we don’t miss out on potential business.  
- **Always Add Notes**: Whenever you move a lead to a new stage, add notes in Markate to explain what happened. For example, “Moved to Attempted to Contact—called and left voicemail at 1:30 PM on 5/12/25.” This keeps everyone at CC Inc. on the same page.  
- **Follow-Ups Are Key**: Many leads don’t say yes right away, but persistence can close deals. Following up shows the customer you care, which can make them more likely to choose CC Inc.  
- **Verify Who the Lead is Assigned To**: Make sure you know who’s responsible for each lead. For example, if a lead is assigned to you, act on it within 24 hours. If it’s assigned to someone else, make sure they know about it.

**Why This Matters for You**  
- **Turn Leads into Customers**: Understanding the 7 stages helps you know exactly what to do at each step, so you can turn more leads into customers. For example, following up at the right time can make the difference between a “yes” and a “no.”  
- **Stay Organized**: The stages keep your work structured, so you always know what’s next. For example, if a lead is in “Scheduled,” you know to prepare for a meeting. If they’re in “First Follow-Up,” you know to check in.  
- **Help CC Inc. Grow**: Every lead you turn into a customer means more business for CC Inc. By mastering this process, you’re helping our company succeed, which makes you a valuable part of the team.

**How This Fits into Your Role at CC Inc.**  
As a sales rep, managing leads through these 7 stages is a core part of your job. You’ll use this process to:  
- **Build Relationships**: Each stage is a chance to connect with the lead and show them why CC Inc. is the best choice. For example, a friendly follow-up call can make a lead feel valued and more likely to say yes.  
- **Close More Deals**: By following the stages, you’ll know when to follow up and how to keep the conversation going, which helps you turn more leads into customers. For example, a lead who’s been sitting in “Waiting for Response” might say yes after a well-timed follow-up.  
- **Keep Things Moving**: The stages ensure leads don’t get stuck or forgotten. For example, if a lead is in “Attempted to Contact,” you’ll know to try again, which keeps the process moving forward.

**What’s Next?**  
In the next module, we’ll learn how to create new leads in Markate, so you can start filling up that “New” bucket. You’ll practice adding 10 leads to get comfortable with the process. Let’s do this!
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
Now that you understand the 7 stages of managing leads at CC Inc., it’s time to start adding leads to Markate. In this module, you’ll learn how to create a new lead in Markate’s staging environment, which is the first step in filling up that “New” bucket we talked about. We’ll practice by adding 10 leads, and I’ll walk you through every step to make sure you feel confident doing it.

**What You’ll Do in This Module**  
You’ll learn how to add a new lead to Markate by filling out a form with their details, like their name, contact info, and what they’re interested in. You’ll practice this by creating 10 leads in the staging environment, using fake information. This will help you get comfortable with the process, so you’re ready to add real leads later.

**What is a New Lead (Again)?**  
Just to recap from Module 1: a lead is anyone who has shown interest in CC Inc.’s services. A *new lead* is someone who has just shown that interest, and we’re adding them to Markate for the first time. For example:  
- **A Phone Call**: Someone calls and says, “I need a quote for window washing.”  
- **A Website Inquiry**: Someone fills out a form on our website saying, “I’m interested in pest control.”  
- **A Referral**: A friend of a customer says, “I heard you do great house washing—can you help me?”  
- **A Repeat Customer**: An existing customer (like John Doe from Chapter 1) says, “I want to add holiday lights.” That’s a new lead for a new service.

When you add a new lead to Markate, they automatically go into the “New” stage in the Pipeline View, ready for you to start working with them.

**How to Add a New Lead in Markate**  
Let’s add your first lead together. Follow these steps carefully, and I’ll explain why each step matters:  
1. **Go to the Leads Section**: Make sure you’re logged into Markate’s staging environment (https://stg.markate.com/, Username: Markate, Password: crm4you, then Email: support@xecutetech.com, Password: Windows4). Go to the Leads section (Sales → Leads), like you learned in Module 2.  
2. **Click the “New Lead” Button**: On the Leads page, look in the top right corner for a button that says “New Lead” (it might have a “+” symbol). Click on it to start adding a new lead.  
3. **Fill in the Required Information**: Now you’ll enter the lead’s details. Since we’re in the staging environment, we’ll use fake information to practice.  
   - **Lead Title**: e.g., “John Doe - Window Washing.”  
   - **Customer Type**: e.g., “Residential.”  
   - **Contact Name**: e.g., John Doe.  
   - **Phone Number**: Use 555-XXXXXXX.  
   - **Email**: firstname@example.com.  
   - **Preferred Notification Method**: Both Email & Text.  
   - **Billing Address**: A fake address like 123 Test Street.  
   - **Lead Source (Optional)**: e.g., “Phone Call.”  
   - **Lead Label**: Hot, Warm, or Cold. (Default is Hot.)  
   - **Comments**: e.g., “Test lead - created for training.”  
   - **Assign to Employee**: Assign it to yourself.  

4. **Click “Save”**: This adds the new lead to Markate, and it appears in the “New” stage.  
5. **Repeat 10 Times**: Create 10 new leads to get comfortable. Each lead should have a unique name, email, and phone, etc.
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
                "question": "Which field should you set to “Hot,” “Warm,” or “Cold” when creating a new lead in Markate?",
                "options": [
                    "Customer Type",
                    "Lead Label",
                    "Lead Source",
                    "Comments"
                ],
                "correct_answer": 1
            },
            {
                "question": "Why do we use phone numbers in the format “555-XXXXXXX” when adding a lead in Markate’s staging environment?",
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
                "question": "After you click “Save” to create a new lead, which stage does it appear in by default?",
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
You’ve done a great job adding new leads to Markate—now it’s time to learn about a related concept: *opportunities*. In this module, you’ll learn how to create a new opportunity in Markate’s staging environment, which is something you’ll do for existing customers who want a quote for an additional service. We’ll practice by adding 10 opportunities, and I’ll walk you through every step to make sure you feel confident.

**What You’ll Do in This Module**  
You’ll learn how to create a new opportunity in Markate for an existing customer who wants a quote for a new service. You’ll practice this by adding 10 opportunities in the staging environment, using fake information. This will help you get comfortable with the process, so you’re ready to create real opportunities later. At the end, I’ll have a scenario task to make sure you understand the difference between a new lead and a new opportunity.

**What is a New Opportunity?**  
A *new opportunity* is a request from an existing customer for a quote on an additional service that we haven’t priced for them before. Let’s break that down:  
- **Existing Customer**: This is someone who already has a customer account in Markate, like the ones you created in Chapter 1 (e.g., John Doe).  
- **Additional Service**: This is a new service they want that we haven’t quoted for them before.  
- **Quote Needed**: We need to give them a price for the new service, but only if we don’t already have a price in their account.

**Why Create a New Opportunity?**  
- **Accurate Quotes**: We provide a new price for the additional service.  
- **Avoid Duplicates**: If we already have a price for a service, we don’t recreate it.  
- **Grow Business**: Opportunities let us expand services for existing customers.

**How to Create a New Opportunity**  
1. Go to Leads → “New Opportunity.”  
2. Link to an existing customer.  
3. Enter the service info, pick the address, etc.  
4. Save.  
5. The opportunity appears in “New” stage, just like a lead.

We’ll do this 10 times for practice.
""",
        "task_type": "scenario",
        "task": """
**Scenario**: Bob is an existing customer who had pest control last year. Now he calls and says he wants holiday lights, and we’ve never priced that for him before. What should you do?  
A) Create a brand-new lead for Bob, since he’s asking for a new service.  
B) Create a new opportunity for Bob, since he’s an existing customer asking for an additional service.  
Select the correct answer and explain why in the box below, thinking about how this helps CC Inc. manage Bob’s request.
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
**Let’s Learn About Assigning Leads and Opportunities!**  
You’re almost done with Chapter 2—great work! You’ve learned how to view leads, understand the 7 stages, and create new leads and opportunities in Markate. In this module, we’ll cover how to assign leads and opportunities to employees (like yourself or other staff members) and go over some final notes on managing leads. This will help you wrap up the process of working with leads at CC Inc.

**What You’ll Do in This Module**  
You’ll learn how to assign a lead or opportunity to a specific employee in Markate, and you’ll understand why this doesn’t automatically move the lead to the “Assigned” stage. You’ll also get some final tips on managing leads effectively. At the end, I’ll have a reflection task to help you think about what you’ve learned.

**How to Assign Employees to Leads & Opportunities**  
- When you create or edit a lead/opportunity, you see “Assign to Employee.”  
- This just notes who’s responsible; it doesn’t move the lead to “Assigned.”  
- To actually move it to “Assigned,” drag the card from “New” to “Assigned” in Pipeline View.

**Final Notes**  
- Keep leads moving.  
- Add notes for every call/email.  
- Verify assigned employee.

Following these steps ensures no lead slips through the cracks.
""",
        "task_type": "reflection",
        "task": "Reflection: Why do you think it’s important to keep leads even if they say ‘No’ after the second follow-up? How do you think this will help CC Inc. in the future?"
    },
    {
        "title": "Chapter 2, Module 7: Final Task – Create Your Own Test Opportunity",
        "content": """
**Let’s Put It All Together: Create Your Own Test Opportunity!**  
Now that you know how to manage leads and opportunities, let’s do a final practice. Use your test account from Chapter 1 (the one you created for yourself as a customer). Pretend you’re an existing customer who wants a new service. Create a new opportunity for yourself and move it to “Assigned” if it needs immediate action. This way, you’ll see the whole process from both sides.
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
