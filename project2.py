import math
import string

def password_analysis(password):
    charset = 0

    if any(c.islower() for c in password):
        charset += 26
    if any(c.isupper() for c in password):
        charset += 26
    if any(c.isdigit() for c in password):
        charset += 10
    if any(c in string.punctuation for c in password):
        charset += len(string.punctuation)

    length = len(password)

    if charset == 0:
        entropy = 0
    else:
        entropy = length * math.log2(charset)

    print("\nPASSWORD SECURITY REPORT")
    print("-" * 35)
    print("Password Length :", length)
    print("Character Set   :", charset)
    print("Estimated Entropy: {:.2f} bits".format(entropy))

    score = 0

    if length >= 12:
        score += 2
    elif length >= 8:
        score += 1

    if any(c.islower() for c in password):
        score += 1

    if any(c.isupper() for c in password):
        score += 1

    if any(c.isdigit() for c in password):
        score += 1

    if any(c in string.punctuation for c in password):
        score += 1

    if score <= 2:
        strength = "Weak"
    elif score <= 4:
        strength = "Moderate"
    else:
        strength = "Strong"

    print("Strength        :", strength)

    print("\nRecommendations")

    if length < 12:
        print("- Use at least 12 characters.")

    if not any(c.isupper() for c in password):
        print("- Add uppercase letters.")

    if not any(c.islower() for c in password):
        print("- Add lowercase letters.")

    if not any(c.isdigit() for c in password):
        print("- Include numbers.")

    if not any(c in string.punctuation for c in password):
        print("- Include special characters.")

    if (length >= 12 and
        any(c.isupper() for c in password) and
        any(c.islower() for c in password) and
        any(c.isdigit() for c in password) and
        any(c in string.punctuation for c in password)):
        print("- Excellent password. No major improvements suggested.")

password = input("Enter password: ")
password_analysis(password)