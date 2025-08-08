import smtplib

def send_alert(email, message):
    print(f"Email sent to {email}: {message}")

# Test
send_alert("test@example.com", "Test threat alert!")