#!/usr/bin/env python3
"""
Chapter 4: Advanced Sales Process & Pipeline Optimization
This script guides you through advanced sales processes,
focusing on optimizing your pipeline, strategic communication,
and continuous improvement. It includes instructional content for
each module along with multiple-choice quizzes to assess your learning.
"""

import sys

def pause():
    input("\nPress Enter to continue...\n")

def ask_quiz(questions):
    score = 0
    for q in questions:
        print("\n" + q["question"])
        for option in q["options"]:
            print(option)
        # Get user input and enforce valid answer
        user_answer = input("Your answer (A, B, C, or D): ").strip().upper()
        while user_answer not in ['A', 'B', 'C', 'D']:
            user_answer = input("Invalid input. Please enter A, B, C, or D: ").strip().upper()
        if user_answer == q["answer"]:
            print("Correct!")
            score += 1
        else:
            print(f"Incorrect. The correct answer is {q['answer']}.")
    print(f"\nYou scored {score} out of {len(questions)} on this quiz.\n")
    pause()

def display_introduction():
    print("="*80)
    print("Chapter 4: Advanced Sales Process & Pipeline Optimization")
    print("="*80)
    print("""
Welcome to Chapter 4!
-----------------------------
In the previous chapters, you learned how to create customers, manage leads, and send estimates in Markate. 
Now, we are taking it one step further to optimize your sales process and pipeline. This chapter is designed
to help you move beyond the basics. We’ll focus on advanced strategies and techniques including:

  • Analyzing pipeline metrics to identify bottlenecks and opportunities.
  • Enhancing your daily workflow for improved efficiency.
  • Mastering proactive follow-up and effective communication with your leads.
  • Leveraging advanced CRM features to boost your sales performance.
  • Engaging in hands-on exercises that simulate real-life scenarios.

By the end of this chapter, you’ll have a deeper understanding of your pipeline and practical strategies to close deals faster.

Let's get started!
    """)
    pause()

def display_section1():
    print("="*80)
    print("Section 1: Advanced Pipeline Understanding & Analysis")
    print("="*80)
    print("""
In this section, we will revisit the sales pipeline you already know:
  • New → Assigned → Attempted to Contact → Scheduled → Estimate Sent → Follow-Up One → Follow-Up Two

Now, let’s dive deeper into analyzing and optimizing the pipeline:

1. Review the Basics:
   - You already know how to move leads between buckets.
   - The key is to monitor how long leads stay in each bucket and how effectively you’re moving them forward.

2. Advanced Metrics & Analysis:
   - **Lead Aging:** Track how long leads remain in each stage. If a lead is stuck too long, it may need extra follow-up.
   - **Conversion Ratios:** Examine the percentage of leads that progress from one stage to the next. This tells you where you might be losing potential deals.
   - **Pipeline Velocity:** Measure the average time from initial contact (New) to an accepted estimate. A faster pipeline means you’re closing deals quicker.

3. Using CRM Analytics:
   - Take advantage of Markate’s custom reports and dashboard widgets.
   - Create filters that show high-value or “hot” leads.
   - Set automated alerts to notify you when leads remain in one stage for too long.

By understanding these advanced metrics, you can tailor your follow-up strategy to ensure that no lead falls through the cracks.
    """)
    pause()

def quiz_section1():
    questions = [
        {
            "question": "1. In Markate, which metric helps you identify how long a lead stays in a specific stage?",
            "options": [
                "A. Lead Aging",
                "B. Customer Satisfaction Score",
                "C. Invoice Turnover",
                "D. Dashboard Theme"
            ],
            "answer": "A"
        },
        {
            "question": "2. What does a high conversion ratio between pipeline stages indicate?",
            "options": [
                "A. Leads are losing interest immediately",
                "B. A strong performance at moving leads forward",
                "C. Too many leads are being duplicated",
                "D. The CRM dashboard is not configured correctly"
            ],
            "answer": "B"
        },
        {
            "question": "3. Pipeline Velocity is best defined as:",
            "options": [
                "A. The number of new leads per day",
                "B. The speed at which leads progress from new to accepted estimate",
                "C. The total revenue generated from leads",
                "D. How quickly you respond to customer emails"
            ],
            "answer": "B"
        }
    ]
    print("\n-- Quiz: Advanced Pipeline Understanding & Analysis --")
    ask_quiz(questions)

def display_section2():
    print("="*80)
    print("Section 2: Optimizing Your Daily Workflow")
    print("="*80)
    print("""
A consistent daily routine can significantly improve your sales performance. In this section, you will learn how to optimize your everyday workflow.

1. Personal Daily Checklists:
   - Start each day by logging into Markate and reviewing your pipeline, especially the New and Assigned buckets.
   - Identify high-potential leads based on conversion data.
   - Set a personal checklist: follow-ups, new lead calls, and daily CRM review.

2. Time Management Techniques:
   - Allocate specific blocks of time for tasks. For example, mornings for fresh lead calls and afternoons for follow-ups.
   - Use your CRM calendar to schedule these tasks, and set reminders to ensure nothing is overlooked.

3. Maintaining a Clean Pipeline:
   - Regularly merge duplicate leads and update outdated information.
   - Archive leads that no longer respond, ensuring that your focus remains on the most promising opportunities.

By incorporating these techniques into your daily routine, you can ensure a steady flow of organized, high-quality leads.
    """)
    pause()

def quiz_section2():
    questions = [
        {
            "question": "1. What is one of the first actions you should take each day in Markate?",
            "options": [
                "A. Send out estimates randomly",
                "B. Review your pipeline, especially the New and Assigned buckets",
                "C. Immediately call every contact in the system",
                "D. Change your dashboard settings"
            ],
            "answer": "B"
        },
        {
            "question": "2. Which technique helps ensure no lead is overlooked?",
            "options": [
                "A. Ignoring automated reminders",
                "B. Allocating specific time blocks for follow-ups",
                "C. Merging all leads into one bucket",
                "D. Only checking the pipeline once a week"
            ],
            "answer": "B"
        },
        {
            "question": "3. Why is regular pipeline cleanup important?",
            "options": [
                "A. It makes the system look busy",
                "B. It ensures you’re focused on the most promising leads",
                "C. It automatically closes deals",
                "D. It increases the total number of leads"
            ],
            "answer": "B"
        }
    ]
    print("\n-- Quiz: Optimizing Your Daily Workflow --")
    ask_quiz(questions)

def display_section3():
    print("="*80)
    print("Section 3: Strategic Communication & Advanced Follow-Up")
    print("="*80)
    print("""
Effective communication is at the heart of sales. In this section, we focus on how to reach out to leads with clear, personalized messaging and handle objections like a seasoned professional.

1. Crafting the Right Follow-Up Message:
   - Personalize your messages by using the customer’s name and referencing previous conversations.
   - Clearly state the next steps, whether it is scheduling a follow-up call or confirming service details.
   - Summarize the agreed services and pricing to reinforce the value of your offer.

2. Overcoming Objections:
   - Familiarize yourself with common customer objections such as concerns about pricing or scheduling.
   - Prepare your responses in advance; for example, explain how quality and reliability justify the cost.
   - Practice role-playing scenarios with a colleague to build your confidence and refine your approach.

By refining your communication and follow-up techniques, you not only improve your chances of closing deals, but you also build stronger, trust-based relationships with your customers.
    """)
    pause()

def quiz_section3():
    questions = [
        {
            "question": "1. When crafting a follow-up message, it’s important to:",
            "options": [
                "A. Use a generic template for all customers",
                "B. Personalize the message with the customer’s name and details",
                "C. Avoid referring to past interactions",
                "D. Keep the message as brief as possible without specifics"
            ],
            "answer": "B"
        },
        {
            "question": "2. What is a key reason for practicing role-playing scenarios?",
            "options": [
                "A. To memorize a script word-for-word",
                "B. To build confidence and refine objection-handling techniques",
                "C. To determine the customer’s favorite color",
                "D. To shorten the time needed for follow-up calls"
            ],
            "answer": "B"
        },
        {
            "question": "3. A clear follow-up message should include:",
            "options": [
                "A. A vague promise to call later",
                "B. Specific next steps and a summary of services offered",
                "C. Only pricing information",
                "D. A request for the customer to email you their feedback"
            ],
            "answer": "B"
        }
    ]
    print("\n-- Quiz: Strategic Communication & Advanced Follow-Up --")
    ask_quiz(questions)

def display_section4():
    print("="*80)
    print("Section 4: Leveraging Advanced CRM Tools to Enhance Your Sales Strategy")
    print("="*80)
    print("""
Markate offers powerful CRM tools that, when used well, can significantly enhance your sales strategy. In this section, you will learn how to customize and leverage these features:

1. Customizing Your Dashboard:
   - Learn to create custom filters that help you quickly identify high-potential leads.
   - Add widgets or charts to visualize key metrics such as lead aging and conversion rates.

2. Using CRM Tags and Filters:
   - Tag your leads based on priority (e.g., “hot” leads or specific campaigns).
   - Use filters to segment your leads, making it easier to target personalized follow-up efforts.

3. Integration & Notifications:
   - Integrate your email and calendar with Markate for real-time notifications.
   - Set up alerts to ensure you never miss important follow-ups or scheduling changes.

Harnessing these advanced CRM features helps you work smarter, not harder, by automating routine tasks and providing actionable insights.
    """)
    pause()

def quiz_section4():
    questions = [
        {
            "question": "1. What is one benefit of customizing your CRM dashboard?",
            "options": [
                "A. It forces you to call all leads at the same time",
                "B. It provides a visual representation of your key metrics",
                "C. It deletes old leads automatically",
                "D. It disables notifications"
            ],
            "answer": "B"
        },
        {
            "question": "2. How do tags help in managing your leads?",
            "options": [
                "A. They increase the total number of leads",
                "B. They help identify the priority or campaign of each lead",
                "C. They remove the need to make follow-up calls",
                "D. They hide unimportant customer details"
            ],
            "answer": "B"
        },
        {
            "question": "3. What is the purpose of integrating your calendar with Markate?",
            "options": [
                "A. To receive real-time notifications for appointments and follow-ups",
                "B. To prevent any modifications to your schedule",
                "C. To automate the merging of duplicate leads",
                "D. To hide the lead details from your dashboard"
            ],
            "answer": "A"
        }
    ]
    print("\n-- Quiz: Leveraging Advanced CRM Tools --")
    ask_quiz(questions)

def display_section5():
    print("="*80)
    print("Section 5: Hands-On Exercises & Best Practices")
    print("="*80)
    print("""
In this final section, we put theory into practice. These hands-on exercises and best practices will help you apply what you have learned in real-world scenarios.

1. Simulation Exercises:
   - Practice moving a lead from the New bucket to Follow-Up Two, updating your notes, and scheduling follow-ups as needed.
   - Role-play a complete follow-up scenario with a colleague, from initial contact to securing an estimate.

2. Group Discussions & Peer Feedback:
   - Join or organize group sessions to share your successful techniques and discuss challenges.
   - Use manager Q&A sessions to clarify doubts and improve your overall process.

These exercises will reinforce your learning and help you identify ways to continuously improve your sales process.
    """)
    pause()

def final_quiz():
    questions = [
        {
            "question": "1. In a real-life scenario, if you notice that many leads are stalling in the 'Attempted to Contact' bucket, what is the most effective strategy?",
            "options": [
                "A. Immediately move all leads to 'Scheduled' without follow-up",
                "B. Review and update your follow-up strategy while setting personalized reminders",
                "C. Delete the leads to start fresh",
                "D. Wait for the leads to call you back"
            ],
            "answer": "B"
        },
        {
            "question": "2. During a role-play exercise, you practice handling a common objection regarding pricing. Which approach best addresses this objection?",
            "options": [
                "A. Apologize and offer a discount immediately",
                "B. Explain the value and quality of the service and share relevant success stories",
                "C. Ignore the objection and continue with the sales pitch",
                "D. End the conversation to avoid conflict"
            ],
            "answer": "B"
        },
        {
            "question": "3. When using advanced CRM features, which of the following practices helps you quickly identify high-potential leads?",
            "options": [
                "A. Creating custom filters and dashboards",
                "B. Deleting all low-priority leads",
                "C. Relying solely on default dashboard settings",
                "D. Ignoring lead tags and notes"
            ],
            "answer": "A"
        },
        {
            "question": "4. Which hands-on exercise is designed to help you simulate the complete follow-up process?",
            "options": [
                "A. Reviewing the CRM dashboard without interacting with leads",
                "B. Role-playing a lead follow-up scenario with a colleague",
                "C. Only reading through past customer emails",
                "D. Setting up a new CRM account to start over"
            ],
            "answer": "B"
        },
        {
            "question": "5. Group discussions in your team are most beneficial because they:",
            "options": [
                "A. Allow you to compete and rank each other's performance",
                "B. Provide a platform to share successful strategies and improve collectively",
                "C. Focus only on the mistakes made during calls",
                "D. Replace the need for one-on-one training sessions"
            ],
            "answer": "B"
        }
    ]
    print("\n-- Final Quiz: Real-World Scenarios & Comprehensive Review --")
    ask_quiz(questions)

def display_conclusion():
    print("="*80)
    print("Conclusion: Putting It All Together")
    print("="*80)
    print("""
Congratulations! You have completed Chapter 4: Advanced Sales Process & Pipeline Optimization.
By now, you should be able to:
  - Analyze and optimize your sales pipeline using advanced metrics.
  - Structure your daily workflow for maximum efficiency.
  - Communicate effectively with prospects and handle objections professionally.
  - Leverage advanced CRM tools to target high-value leads and set up effective reminders.
  - Apply these strategies in hands-on exercises and role-playing scenarios.

As you integrate these practices into your daily routine, you will notice an improvement in your lead conversion and overall sales performance. Remember, continuous improvement and proactive follow-up are the keys to achieving and exceeding your targets.

Get ready to move on to Chapter 5, where we’ll explore exactly how your commission is tracked – a crucial area that directly affects your earnings!
    """)
    pause()

def main():
    # Introduction to Chapter 4
    display_introduction()
    
    # Section 1: Advanced Pipeline Understanding & Analysis
    display_section1()
    quiz_section1()
    
    # Section 2: Optimizing Your Daily Workflow
    display_section2()
    quiz_section2()
    
    # Section 3: Strategic Communication & Advanced Follow-Up
    display_section3()
    quiz_section3()
    
    # Section 4: Leveraging Advanced CRM Tools to Enhance Your Sales Strategy
    display_section4()
    quiz_section4()
    
    # Section 5: Hands-On Exercises & Best Practices
    display_section5()
    print("Now, let's take the final comprehensive quiz, which includes real-world scenarios!")
    pause()
    final_quiz()
    
    # Conclusion and transition to next chapter
    display_conclusion()
    print("End of Chapter 4.")
    
if __name__ == '__main__':
    main()
