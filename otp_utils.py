import random
import smtplib
from email.mime.text import MIMEText

EMAIL = "your_gmail@gmail.com"
APP_PASSWORD = "your_app_password"  # Use app password, not Gmail password

def generate_otp():
    return str(random.randint(100000, 999999))

def send_otp_email(to_email, otp):
    subject = "Your College Sync OTP"
    body = f"Your OTP is: {otp}"

    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = EMAIL
    msg["To"] = to_email

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(EMAIL, APP_PASSWORD)
        server.send_message(msg)