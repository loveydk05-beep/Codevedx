# vulnerability_assessment_demo.py

sample_system = {
    "OS": "Windows 10",
    "Firewall": False,
    "Antivirus": True,
    "HTTPS": False,
    "Strong Password": False,
    "Unused Open Ports": True
}

print("=" * 40)
print("VULNERABILITY ASSESSMENT REPORT")
print("=" * 40)

score = 0

checks = [
    ("Firewall", "Firewall Disabled", 3),
    ("Antivirus", "Antivirus Missing", 3),
    ("HTTPS", "HTTPS Not Enabled", 2),
    ("Strong Password", "Weak Password", 2),
    ("Unused Open Ports", "Unused Open Ports Found", 1)
]

for key, message, severity in checks:
    value = sample_system[key]

    if key in ["Firewall", "Antivirus", "HTTPS", "Strong Password"]:
        vulnerable = not value
    else:
        vulnerable = value

    if vulnerable:
        print("[VULNERABLE]", message)
        score += severity
    else:
        print("[OK]", key)

print("\nRisk Score:", score)

if score >= 8:
    level = "HIGH"
elif score >= 4:
    level = "MEDIUM"
else:
    level = "LOW"

print("Overall Risk:", level)