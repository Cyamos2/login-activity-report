logs = [
    "SUCCESS: user1 from 192.168.1.5",
    "FAILED: user2 from 10.0.0.99",
    "FAILED: admin from 172.16.0.3",
    "SUCCESS: user3 from 192.168.1.5",
    "FAILED: root from 66.66.66.66",
    "FAILED: guest from 123.123.123.123"
]

# Counters
total_attempts = 0
failed_attempts = 0
success_attempts = 0
suspicious_count = 0

# List of known suspicious IPs
suspicious_ips = ["66.66.66.66", "123.123.123.123"]

# Loop through each log entry
for log in logs:
    total_attempts += 1

    if "SUCCESS" in log:
        success_attempts += 1
        print(log)
        print("The user was successfully logged in.")
    else:
        failed_attempts += 1
        print(log)
        print("The user failed to log in.")

    # Check for suspicious IPs
    for ip in suspicious_ips:
        if ip in log:
            suspicious_count += 1
            print("⚠️ Suspicious IP detected:", ip)

# Final report
print("\nLOGIN REPORT")
print("----------------")
print(f"Total attempts: {total_attempts}")
print(f"Successful logins: {success_attempts}")
print(f"Failed logins: {failed_attempts}")
print(f"Suspicious IPs detected: {suspicious_count}")
print("⚠️ ALERT TRIGGERED") if suspicious_count > 0 else print("✅ No alerts.")