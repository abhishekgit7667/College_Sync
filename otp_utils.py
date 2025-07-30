import random
import smtplib
from email.mime.text import MIMEText

from dotenv import load_dotenv
import os
load_dotenv()
from flask import Flask, request, redirect, render_template, flash

EMAIL = os.getenv("EMAIL")
APP_PASSWORD = os.getenv("APP_PASSWORD")  # Use app password, not Gmail password

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