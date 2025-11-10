#!/usr/bin/env python3
"""
CodeAlpha Cyber Security Internship — Task 2
Phishing Awareness Training Program (Interactive Python Version)
Developer: Muheeb Bin Nadeem
"""

import time
import textwrap

# helper function to print formatted text
def slow_print(text, delay=0.03):
    for ch in text:
        print(ch, end='', flush=True)
        time.sleep(delay)
    print()

# introduction
def intro():
    print("=" * 70)
    slow_print("🛡️  Welcome to the Phishing Awareness Training Program!")
    print("=" * 70)
    slow_print("\nIn this training, you'll learn how to identify and avoid phishing attacks.")
    slow_print("Phishing is one of the most common forms of cybercrime —")
    slow_print("where attackers trick you into revealing sensitive information like passwords or card numbers.\n")
    input("Press ENTER to continue...")

# phishing examples
def examples():
    print("\n📧 Example 1: Suspicious Email\n")
    email_1 = """
    From: support@micr0soft-security.com
    Subject: Urgent! Verify your Microsoft account immediately.

    Dear user,
    We have detected unusual activity on your account. 
    Please verify your details immediately to avoid suspension:
    https://micr0soft-verify-login.com
    """
    print(textwrap.dedent(email_1))
    slow_print("\n⚠️  Red Flags:")
    slow_print("- Sender address looks suspicious (micr0soft-security.com).")
    slow_print("- Urgent tone creates pressure to act quickly.")
    slow_print("- Fake verification link (notice the '0' instead of 'o').")

    print("\n📧 Example 2: Fake Bank SMS\n")
    sms_1 = "Your account is locked. Click http://bit.ly/Bank-Unlock to restore access."
    slow_print(sms_1)
    slow_print("\n⚠️  Red Flags:")
    slow_print("- Shortened URL hides true destination.")
    slow_print("- Banks never ask you to click links in SMS messages.\n")
    input("Press ENTER to continue to quiz...")

# quiz section
def quiz():
    score = 0
    print("\n🧠 Let's test your knowledge! (Type a, b, or c)\n")

    qna = [
        {
            "q": "1. What is the main goal of a phishing attack?",
            "a": ["To improve system speed", "To steal sensitive data", "To protect your password"],
            "c": "b"
        },
        {
            "q": "2. Which of the following is a sign of a phishing email?",
            "a": ["Official domain name", "Urgent or threatening tone", "Personalized greeting"],
            "c": "b"
        },
        {
            "q": "3. What should you do if you receive a suspicious link?",
            "a": ["Click immediately", "Ignore and delete", "Forward to everyone"],
            "c": "b"
        },
        {
            "q": "4. What’s the safest way to verify a message’s authenticity?",
            "a": ["Reply to the same email", "Contact the company via official website", "Click all links"],
            "c": "b"
        },
        {
            "q": "5. Phishing mainly relies on which method?",
            "a": ["Social engineering and deception", "System hardware failure", "Strong encryption"],
            "c": "a"
        }
    ]

    for item in qna:
        print(item["q"])
        for i, opt in enumerate(item["a"]):
            print(f"  {chr(97+i)}. {opt}")
        ans = input("Your answer: ").lower()
        if ans == item["c"]:
            slow_print("✅ Correct!\n")
            score += 1
        else:
            slow_print("❌ Incorrect.\n")
        time.sleep(0.5)

    return score

# feedback
def feedback(score):
    print("=" * 70)
    slow_print(f"\n🎯 You scored {score}/5!")
    if score == 5:
        slow_print("Excellent! You’re highly aware of phishing tactics.")
    elif score >= 3:
        slow_print("Good job! Stay alert — you’re on the right track.")
    else:
        slow_print("You need more awareness. Review phishing examples again.")
    slow_print("\nRemember: Never click suspicious links or share personal info via email.\n")
    print("=" * 70)
    slow_print("✅ Training Complete — Developed by Muheeb Bin Nadeem (CodeAlpha 2025)")

# main
def main():
    intro()
    examples()
    score = quiz()
    feedback(score)

if __name__ == "__main__":
    main()
