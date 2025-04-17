"""
chapter5.py

This module contains the Chapter 5 training content for the CRM Training App, a 
Streamlit-based training platform for CC Inc. employees learning to use the Markate CRM.
It includes the CH5_MODULES list with modules and tasks, as well as the CH5_FINAL_QUIZ 
list for the final quiz questions.
"""

# -------------------------------------------------------------------
# CHAPTER 5 MODULES & FINAL QUIZ
# -------------------------------------------------------------------

CH5_MODULES = [
    {
        "title": "Chapter 5, Module 1: Introduction to Commissions at CC Inc.",
        "content": """
**Welcome to Chapter 5: Understanding Commissions in Markate!**  
Great job making it to Chapter 5! So far, you’ve learned how to create customers, manage leads, send estimates, and create work orders in Markate CRM. Now, let’s talk about something that directly impacts *you*—your commissions! As a sales rep at CC Inc., commissions are a big part of how you earn money, and understanding how they work is key to your success. Don’t worry if this feels new—I’ll break it down step-by-step, just like we’ve done in the other chapters, so you’ll know exactly how to get paid for your hard work. Let’s get started!

**What Are Commissions?**  
Commissions are the money you earn for booking jobs with CC Inc. They’re a percentage of the job’s total cost, and they reward you for bringing in new customers and growing business with existing ones. Think of commissions as a "thank you" for your sales efforts—the more jobs you book, the more you earn! At CC Inc., we have two types of commissions:  
- 10 percent commission on new sales - this is for new customers, people who have never worked with CC Inc. before. For example, if you bring in a new customer who books a $1,000 house washing job, you earn $100 (10 percent of $1,000 before taxes).  
- 5 percent commission on existing customers - this is for customers who have worked with us before, like someone who had window washing last year and now wants pest control. If they book a $500 job, you earn $25 (5 percent of $500 before taxes).  

**Why Are Commissions Important?**  
Commissions motivate you to find new customers and keep existing ones coming back for more services. They’re a big part of your income at CC Inc., and understanding how to track and earn them ensures you get paid for all your hard work. Here’s why this matters:  
- Earning potential - the more sales you make, the more you earn. For example, a big $10,000 job with a new customer could mean $1,000 in your pocket!  
- Motivation to grow - commissions encourage you to find new leads and upsell existing customers. For example, if a past customer books a new service, that 5 percent adds up over time.  
- Fairness - CC Inc. wants to reward you for your efforts, and commissions make sure you’re paid for every job you book.  

**How Does Markate Help with Commissions?**  
Markate CRM makes tracking commissions easier, especially for new sales, because it logs who sends the estimate and calculates your 10 percent commission automatically. For existing customers, you’ll use a manual process with work order sheets, which we’ll cover in later modules. By the end of this chapter, you’ll know exactly how to earn, track, and get paid your commissions using Markate and our payroll process.

**What’s Next?**  
We’ll start by diving into the 10 percent commission for new sales—how it works, how to track it in Markate, and what you need to do to make sure you get paid. Let’s make sure you understand the basics with a quick quiz!
""",
        "task_type": "miniquiz",
        "miniquiz_questions": [
            {
                "question": "What percentage commission do you earn on a new customer sale?",
                "options": ["A. 5%", "B. 10%", "C. 15%"],
                "correct_answer": 1
            },
            {
                "question": "What percentage commission do you earn on an existing customer sale?",
                "options": ["A. 5%", "B. 10%", "C. 15%"],
                "correct_answer": 0
            }
        ]
    },
    {
        "title": "Chapter 5, Module 2: Earning 10 Percent Commission on New Sales",
        "content": """
**Let’s Learn How to Earn Your 10 Percent Commission!**  
Now that you understand what commissions are, let’s dive into the first type: the 10 percent commission you earn on new sales. This is the easiest commission to track because Markate does most of the work for you, but there are a few key steps you need to follow to make sure you get paid. I’ll walk you through everything, step-by-step, with examples to make it crystal clear. Let’s get started!

**What Are New Sales?**  
A new sale is when you book a job for a new customer—someone who has never worked with CC Inc. before. This could be:  
- A new lead who calls and says, "I need house washing for my home."  
- Someone you meet at a community event who wants pest control and has never heard of CC Inc. before.  
For these new customers, you earn a 10 percent commission on the total job amount (before taxes). For example:  
- If a new customer books a $2,000 window washing job, your commission is $200 (10 percent of $2,000).  
- If they book a $500 pest control job, your commission is $50 (10 percent of $500).  

**How to Earn Your 10 Percent Commission in Markate**  
Markate tracks your 10 percent commission automatically, but there’s one very important rule you need to follow: you must send the estimate yourself, from your own Markate account. Here’s how it works, step-by-step:  
- Log into your Markate account - every sales rep at CC Inc. has their own login for Markate. This is not the staging environment you used in Chapter 1, Module 2—this is your personal account for real customer work. Make sure you’re logged in with your personal account—not someone else’s!  
  - Why? Markate tracks who sends the estimate based on your login. If you’re not logged in to your account, or if someone else sends the estimate (like Casey or an office admin), you won’t get the commission.  
- Create and send the estimate - when a new customer asks for a quote, create an estimate in Markate (you learned how in Chapter 3). For example, if a new customer named Sarah Jones wants house washing, you’ll:  
  - Go to Sales > Estimates.  
  - Click "+ New Estimate," select the type (Standard or Options), and fill in the details (e.g., "House Washing: $1,000").  
  - Send the estimate to Sarah from your account.  
- Customer accepts the estimate - if Sarah accepts the estimate (or part of it), Markate logs that you sent it and calculates your commission.  
  - Important note - you only earn commission on the accepted amount. For example, if you send a $10,000 estimate with multiple services (like house washing and pest control), but Sarah only accepts $1,000 worth of services, your commission is $100 (10 percent of $1,000, before taxes).  
- Markate tracks your commission - once the job is accepted by the customer, Markate automatically calculates your 10 percent commission and adds it to your payroll. You’ll see this on your biweekly pay statement (we’ll cover payroll in a later module).  

**Example in Action**  
Let’s say you meet a new customer, Mike Brown, at a local event. He’s never worked with CC Inc. before and wants window washing. Here’s what happens:  
- You log into your Markate account, create a new lead for Mike, and schedule and assign it to yourself since you’re talking with him in person.  
- You then create an estimate for "Window Washing: $800" and send the quote from your account.  
- Mike accepts it, and the job is booked.  
- Markate logs that you sent the estimate from your account and calculates your commission: $80 (10 percent of $800).  
- That $80 will show up in your next biweekly paycheck—nice work!  

**Key Tip: Always Use Your Account!**  
If someone else sends the estimate—like another sales rep such as Casey or an admin like Lisa—you won’t get the commission, even if you found the customer. Always double-check that you’re logged in and sending the estimate yourself. This is how Markate knows to give you credit for the sale.

**What’s Next?**  
In the next module, we’ll learn about the 5 percent commission for existing customers, which uses a different process since Markate doesn’t track it automatically. Let’s make sure you understand the 10 percent commission process with a quick quiz!
""",
        "task_type": "miniquiz",
        "miniquiz_questions": [
            {
                "question": "What must you do to earn the 10% commission on a new sale?",
                "options": ["A. Create a work order", "B. Send the estimate from your Markate account", "C. Call the customer"],
                "correct_answer": 1
            },
            {
                "question": "If a new customer accepts $2,000 of a $5,000 estimate, what is your commission?",
                "options": ["A. $500", "B. $200", "C. $50"],
                "correct_answer": 1
            }
        ]
    },
    {
        "title": "Chapter 5, Module 3: Earning 5 Percent Commission on Existing Customers",
        "content": """
**Let’s Learn How to Earn Your 5 Percent Commission!**  
Now that you know how to earn your 10 percent commission on new sales, let’s talk about the second type: the 5 percent commission you earn on sales to existing customers. This process is a bit different because Markate doesn’t track these commissions automatically—you’ll use a manual process with work order sheets. I’ll walk you through every step with examples, so you’ll know exactly what to do. Let’s dive in!

**What Are Existing Customer Sales?**  
An existing customer is someone who has worked with CC Inc. before—they already have a customer account in Markate, and they might have past invoices or estimates, which could be 3–4 years old. As long as they’re an existing customer, you earn a 5 percent commission on any new jobs you book with them. For example:  
- If an existing customer books a $1,000 house washing job, your commission is $50 (5 percent of $1,000 before taxes).  
- If they book a $500 pest control job, your commission is $25 (5 percent of $500 before taxes).  

**How to Find Opportunities with Existing Customers**  
To earn your 5 percent commission, you’ll need to reach out to existing customers and offer them new services. Markate makes this easy by letting you look up their past jobs or estimates. Here’s how:  
- Look up the customer in Markate - go to Sales > Customers, search for the customer (e.g., John Doe), and open their profile.  
- Check past invoices or estimates - in John’s profile, look at:  
  - Past invoices - these show jobs we’ve done for John before (e.g., "Window Washing: $500 last year").  
  - Past estimates - these show quotes we sent that John didn’t accept (e.g., "House Washing: $850, not accepted").  
  This information helps you start the conversation—John might want to repeat a past service or try something new.  
- Call the customer - reach out to John and offer services. For example:  
  - "Hi John, I see we did your windows last year for $500—would you like to do that again?"  
  - "I also noticed we quoted you $850 for house washing last year, but you didn’t move forward. Would you like to add that this time?"  
  Be friendly and helpful—your goal is to get John to book a new job!  
- Hover over Sales > Invoices - another way to find opportunities is to hover over "Sales" in the top menu, then click "Invoices." You can view all past invoices here, going back to 2020, to see who’s done work with us in the past. You can also click "Reports" on the top menu bar and open any report you’d like—these give you a variety of options to explore past data. We won’t go through all of them here since they’re self-explanatory, but feel free to click around—you won’t break anything! Just like with invoices, you can view the Estimates column to see past estimates, which might include thousands of records dating back years.  

**Example: Booking a Job with John Doe**  
Let’s say John’s the customer you call—he did window washing last year for $500, according to his past invoice. You also saw on his profile that he had an estimate for house washing at $850, but he didn’t move forward with it. During your call, you say, "Hi John, I see we did your windows last year for $500—would you like to do that again? Also, we quoted you $850 for house washing, which you didn’t book at the time. It’d be a great way to keep your home looking its best—would you like to add that this year?" John agrees to both services: window washing for $500 and house washing for $850. You’ve convinced John this is a good idea, and he signs up for both. Here’s what happens: John books a total of $1,350 in services ($500 + $850). You’ll earn a 5 percent commission on that amount: $67.50 (5 percent of $1,350, before taxes).  

**How to Track Your 5 Percent Commission**  
Since Markate doesn’t track this commission automatically, you’ll use a work order sheet to report the sale. Casey will provide you the work order sheet. Here’s the step-by-step process:  
- Create work orders in Markate - since John booked two services (window washing and house washing), you’ll create two work orders in Markate, just like you learned in Chapter 4:  
  - One for "John Doe - Window Washing" ($500).  
  - One for "John Doe - House Washing" ($850).  
  Make sure you’re logged into your Markate account when creating these work orders, so the jobs are linked to you.  
- Fill out a work order sheet - grab a work order sheet from the shop and write down:  
  - Customer name - John Doe.  
  - Services booked - House Washing $850, Window Washing $500.  
  - Total before taxes - $1,350.  
  You don’t need to calculate your commission—the payroll team will do that for you (5 percent of $1,350 = $67.50).  
- Submit the work order sheet - place the sheet in the work order bins in the shop. These bins are where all commission sheets go to be processed for payroll (we’ll cover the full payroll process in the next module).  

**Key Tip: Always Submit Your Work Order Sheet!**  
If you don’t submit the work order sheet, you won’t get your 5 percent commission, even if you booked the job—because how is the office supposed to know? Make it a habit to fill out and submit the sheet right after creating the work orders in Markate.

**What’s Next?**  
In the next module, we’ll learn about hourly rates for tasks outside the scope of sales, which use a similar tracking process. Let’s make sure you understand the 5 percent commission process with a quick quiz!
""",
        "task_type": "miniquiz",
        "miniquiz_questions": [
            {
                "question": "How can you find out what services an existing customer has had before?",
                "options": ["A. Check their past invoices or estimates in Markate", "B. Ask the payroll team", "C. Look in the work order bins"],
                "correct_answer": 0
            },
            {
                "question": "What must you do to get your 5% commission for an existing customer sale?",
                "options": ["A. Send an estimate in Markate", "B. Fill out and submit a work order sheet", "C. Call the customer twice"],
                "correct_answer": 1
            }
        ]
    },
    {
        "title": "Chapter 5, Module 4: Hourly Rates and Additional Earnings",
        "content": """
**Let’s Learn About Hourly Rates and Other Earnings!**  
Great work so far! You’ve learned how to earn your 10 percent and 5 percent commissions—now let’s talk about another way you might earn money at CC Inc.: hourly rates for field work. I’ll explain how this works, how to track it, and how it fits into the payroll process. Let’s get started!

**What Are Hourly Rates at CC Inc.?**  
At CC Inc., your main earnings come from commissions (10 percent for new sales, 5 percent for existing customers), but you might also do work in the field that’s paid at a flat hourly rate. This hourly rate is for tasks outside the scope of sales—things that aren’t related to booking jobs, since those are covered by your commissions. For example:  
- You might spend a day training with the pest control crew to learn more about their services.  
- You might do quality control, like checking a completed house washing job to ensure it meets standards.  
- You might run errands, such as picking up stain for the painting division or dropping off materials for a job site.  
- You might work with another division, like helping the holiday lights team set up a display.  
The exact hourly rate depends on your agreement with Casey—let’s say it’s $20 per hour for this example.

**How to Track Your Hourly Work**  
Tracking your hourly work uses the same work order sheet process you learned for 5 percent commissions. Here’s how it works:  
- Do the field work - let’s say you spend 3 hours working with the pest control crew to learn their processes.  
- Fill out a work order sheet - grab a work order sheet from the shop and fill it out. The sheet is self-explanatory—just write your name, the date, a brief description (e.g., "Worked with pest control crew"), and your total hours (3 hours). You don’t need to calculate your pay—the payroll team will do that based on your hourly rate.  
- Submit the work order sheet - place the sheet in the work order bins in the shop, just like you do for 5 percent commissions.  

**How Hourly Pay Gets Processed**  
Your hourly pay follows the same payroll process as your 5 percent commissions, which we’ll cover in more detail in the next module. For now, know that your sheet stays in the work order bins until the biweekly payroll period ends. The payroll team will collect it, process your pay, and move the sheet to the outbound files for you to review.

**Example: Combining Commissions and Hourly Pay**  
Let’s say in one pay period:  
- You earned $800 in 10 percent commissions from new sales.  
- You earned $450 in 5 percent commissions from an existing customer (John Doe).  
- You worked 3 hours in the field at $20/hour ($60).  
Your total earnings for that paycheck would be $1,310 ($800 + $450 + $60), all listed on your pay statement. Great work!

**Key Tip: Be Detailed on Your Work Order Sheet!**  
When filling out the sheet for hourly work, be specific about what you did (e.g., "Worked with pest control crew") and how many hours you worked. This helps the payroll team process your pay accurately and ensures there’s a clear record in case you need to double-check later.

**What’s Next?**  
In the next module, we’ll learn how all your earnings—commissions and hourly pay—get processed through payroll, so you know exactly how you’ll get paid. Let’s make sure you understand hourly rates with a quick quiz!
""",
        "task_type": "miniquiz",
        "miniquiz_questions": [
            {
                "question": "How do you track hourly work for field tasks?",
                "options": ["A. Send an estimate in Markate", "B. Fill out a work order sheet with hours worked", "C. Log it in the outbound files"],
                "correct_answer": 1
            },
            {
                "question": "Where do hourly work earnings appear?",
                "options": ["A. In your biweekly paycheck", "B. In Markate’s dashboard", "C. In the customer’s profile"],
                "correct_answer": 0
            }
        ]
    },
    {
        "title": "Chapter 5, Module 5: The Payroll Process for Commissions",
        "content": """
**Let’s Learn How Your Commissions Get Paid!**  
Now that you’ve learned how to earn your commissions and hourly pay, let’s bring it all together! At CC Inc., you can earn money in three ways:  
- 10 percent commission on new sales - tracked automatically in Markate when you send the estimate and the customer accepts it.  
- 5 percent commission on existing customers - tracked manually by submitting a work order sheet to the bins in the shop.  
- Hourly rates for field work - also tracked manually by submitting a work order sheet for tasks outside the scope of sales.  
In this module, we’ll learn how all these earnings get processed through payroll and paid to you, with everything documented in the outbound files for your records. Let’s get started!

**How Does Payroll Work at CC Inc.?**  
At CC Inc., we process payroll biweekly—that means you get paid every two weeks. Your commissions (both 10 percent for new sales and 5 percent for existing customers) are included in your biweekly paycheck, along with any other earnings (like hourly rates). The payroll process makes sure all your hard work is tracked and paid accurately.

**Step-by-Step: How Your Commissions Get Paid**  
Here’s how the payroll process works for your commissions:  
- New sales (10 percent commission)  
  - Markate automatically tracks your 10 percent commission for new sales (as you learned in Module 2).  
  - When the customer accepts the job, Markate logs your commission and sends it to the payroll team.  
  - For example, if you earned $800 on an $8,000 new sale, that $800 is automatically added to your next paycheck.  
  - You’ll see this amount on your biweekly pay statement—no extra work needed!  
- Existing customer sales (5 percent commission) and hourly rates  
  - For these sales and hourly work, you submit a work order sheet to the work order bins in the shop (as you learned in Modules 3 and 4). For example, if you booked a $1,350 job with John Doe, you’d submit a sheet listing the services and total. If you worked 3 hours in the field, you’d submit another sheet for that.  
  - Here’s what happens next:  
    - Step 1 - work order bins: your sheet stays in the work order bins in the shop until payroll is processed. These bins are where all commission sheets are collected.  
    - Step 2 - payroll processing: when the biweekly payroll period ends, the payroll team collects all sheets from the bins and moves them to the office. They calculate your 5 percent commission (e.g., $67.50 for John Doe’s $1,350 job) or your hourly pay (e.g., $60 for 3 hours at $20/hour) and add it to your paycheck.  
    - Step 3 - outbound files: after processing, your work order sheet is moved to the outbound files. These are records you can take home to review exactly what you earned. For example, your sheet for John Doe will show the $1,350 job and your $67.50 commission.  
- Get your paycheck - every two weeks, you’ll get a paycheck that includes:  
  - Your 10 percent commissions from new sales (tracked by Markate).  
  - Your 5 percent commissions from existing customer sales (from your work order sheets).  
  - Any hourly pay for field work (also from your work order sheets).  
  - A pay statement showing the breakdown of all your earnings, so you can see exactly what you earned from each job.  

**Example: Your Biweekly Pay**  
Let’s say you had a busy two weeks:  
- You booked $8,000 in new sales (10 percent commission = $800).  
- You booked $1,350 with an existing customer, John Doe (5 percent commission = $67.50).  
- You worked 3 hours in the field at $20/hour ($60).  
When payroll is processed:  
- Markate automatically sends your $800 for new sales to payroll.  
- The payroll team processes your work order sheets, adding $67.50 for John Doe’s job and $60 for your hourly work to your paycheck.  
- Your total earnings for the pay period are $927.50 ($800 + $67.50 + $60), which you’ll see on your pay statement. You can take the sheets from the outbound files to double-check everything matches up.  

**Key Tip: Always Check Your Pay Statement!**  
Your biweekly pay statement will list all your commissions and hourly pay, so you can confirm you were paid for every job. If something looks wrong (e.g., a work order sheet is missing), you can talk to the payroll team to sort it out. The outbound files are your backup—they show exactly what you submitted.

**What’s Next?**  
You’ve now learned everything you need to know about earning and getting paid at CC Inc.! Next, you’ll take a final quiz to wrap up Chapter 5. Let’s make sure you understand how commissions are paid with a quick quiz!
""",
        "task_type": "miniquiz",
        "miniquiz_questions": [
            {
                "question": "How often does CC Inc. process payroll?",
                "options": ["A. Weekly", "B. Biweekly", "C. Monthly"],
                "correct_answer": 1
            },
            {
                "question": "Where do you submit your work order sheets for 5% commissions?",
                "options": ["A. Outbound files", "B. Work order bins in the shop", "C. Markate dashboard"],
                "correct_answer": 1
            }
        ]
    }
]

CH5_FINAL_QUIZ = [
    {
        "question": "What percentage commission do you earn on a new customer sale?",
        "options": ["A. 5%", "B. 10%", "C. 15%"],
        "answer": 1
    },
    {
        "question": "How do you ensure you get your 10% commission for a new sale?",
        "options": ["A. Fill out a work order sheet", "B. Send the estimate from your Markate account", "C. Call the customer"],
        "answer": 1
    },
    {
        "question": "What percentage commission do you earn on an existing customer sale?",
        "options": ["A. 5%", "B. 10%", "C. 15%"],
        "answer": 0
    },
    {
        "question": "Where do you submit your work order sheet for 5% commissions or hourly work?",
        "options": ["A. Outbound files", "B. Work order bins in the shop", "C. Markate dashboard"],
        "answer": 1
    },
    {
        "question": "How often does CC Inc. process payroll?",
        "options": ["A. Weekly", "B. Biweekly", "C. Monthly"],
        "answer": 1
    },
    {
        "question": "You’re calling an existing customer, Jane Smith, to offer new services. Where can you find information about her past jobs to start the conversation?",
        "options": [],  # Written answer, no options
        "answer": None,  # Will check for non-empty response
        "is_written": True
    }
]
