# phishing_awareness_simulator.py

emails = [
    {
        "subject": "Your Bank Account Has Been Suspended",
        "sender": "support@secure-bank-login.com",
        "link": "http://secure-bank-login.com/verify",
        "phishing": True
    },
    {
        "subject": "Meeting Reminder",
        "sender": "hr@company.com",
        "link": "https://company.com/calendar",
        "phishing": False
    },
    {
        "subject": "Congratulations! You Won a Prize",
        "sender": "winner@freegift.xyz",
        "link": "http://freegift.xyz/claim",
        "phishing": True
    }
]

score = 0

print("=" * 50)
print("PHISHING AWARENESS SIMULATOR")
print("=" * 50)

for i, email in enumerate(emails, start=1):
    print(f"\nEmail {i}")
    print("-" * 30)
    print("Subject :", email["subject"])
    print("Sender  :", email["sender"])
    print("Link    :", email["link"])

    answer = input("\nIs this a phishing email? (yes/no): ").strip().lower()

    if (answer == "yes" and email["phishing"]) or \
       (answer == "no" and not email["phishing"]):
        print("Correct!")
        score += 1
    else:
        print("Incorrect.")

        if email["phishing"]:
            print("Reason: Suspicious sender, insecure link, or social engineering.")
        else:
            print("Reason: This is a legitimate email.")

print("\n" + "=" * 50)
print("RESULT")
print("=" * 50)
print(f"Score: {score}/{len(emails)}")

if score == len(emails):
    print("Excellent! You identified all emails correctly.")
elif score >= 2:
    print("Good job! Continue checking senders, URLs, and unexpected requests.")
else:
    print("Review phishing indicators such as suspicious domains, urgent language, and HTTP links.")