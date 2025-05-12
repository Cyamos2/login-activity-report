# login-activity-report
Python script that scans login logs, detects suspicious activity, and generates a summary report.

# 🛡️ Login Activity Report Generator (Python)

This Python script simulates a basic log analysis tool that scans login activity, detects failed attempts, flags known suspicious IP addresses, and generates a simple security report.

---

## ✅ What It Does

- Counts total login attempts
- Separates successful vs. failed logins
- Checks for known suspicious IPs
- Triggers an alert if suspicious activity is detected
- Prints a clean, readable summary report

---

## 🧠 How It Works

### Input:
A list of fake log entries (could be adapted for real log files):
```python
logs = [
    "SUCCESS: user1 from 192.168.1.5",
    "FAILED: user2 from 10.0.0.99",
    ...
]

## Logic:
- Uses for loops to scan each log line
- Uses string checks ("SUCCESS" or "FAILED") to classify outcomes
- Cross-checks each log line against a list of know suspicious IPs

## Output:
LOGIN REPORT
----------------
Total attempts: 6
Successful logins: 2
Failed logins: 4
Suspicious IPs detected: 2
⚠️ ALERT TRIGGERED

---

## 🔧 Future Enhancements
	•	Load log data from an external file
	•	Save the report as a .txt or .csv
	•	Add timestamps or usernames
	•	Use regular expressions for deeper pattern matching
	•	Integrate into a larger incident response toolkit

---

## 🎯 Why This Project?

This tool was built as part of my CompTIA Security+ and Python practice. It demonstrates:
	•	Real-world log analysis thinking
	•	Secure coding and defensive scripting
	•	Automation of repetitive detection tasks
