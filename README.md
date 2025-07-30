📘 College Sync – User Authentication with OTP Verification


---

📝 Project Overview

College Sync is a Flask-based web application that allows users to register, verify via OTP sent to their email, and log in to access a protected dashboard.


---

🚀 Features

✅ User Registration with Email

✅ OTP Verification for Account Activation

✅ Secure Password Hashing (bcrypt)

✅ User Login/Logout

✅ Session Management

✅ Email Sending using Gmail SMTP

✅ Environment Variable Support using .env



---

🛠 Tech Stack

Component	Tool

Backend	Python with Flask
Password Hash	bcrypt
Email Service	smtplib (Gmail SMTP)
OTP Generator	Python random module
Database	SQLite
Config Storage	.env file with dotenv
Templating	Jinja2 (HTML Templates)



---

📁 Folder Structure

college_sync/
├── app.py                 # Main Flask application
├── otp_utils.py           # Handles OTP generation and email sending
├── database.py            # Database setup and user operations
├── templates/             # HTML templates
│   ├── register.html
│   ├── otp_verify.html
│   ├── login.html
│   └── dashboard.html
├── .env                   # Environment variables (secret key, email)
├── requirements.txt       # Required Python packages
└── users.db               # SQLite database (auto-created)


---

🔐 Why We Use Each Component

Component	Purpose

Flask	Lightweight Python web framework to create routes and views.
bcrypt	Securely hashes passwords so they aren't stored in plain text.
random	Generates 6-digit OTPs for verification.
smtplib	Sends emails via Gmail SMTP server.
dotenv	Loads sensitive data (email password, secret key) from .env file.
sqlite3	Stores user details persistently in a lightweight DB.
session	Tracks logged-in users during browsing sessions.



---

⚙ How It Works

1. User Registers

Fills name, email, and password

App hashes password using bcrypt

An OTP is generated and emailed using Gmail SMTP


2. User Verifies OTP

User enters OTP and email

If OTP matches, data is saved into the database


3. User Logs In

Enters email and password

Password is verified against hashed one in DB

On success, session is created and dashboard is shown


4. Logout

Session is cleared, user is redirected to login



---

🧪 Environment Setup

✅ Install Requirements

pip install flask bcrypt python-dotenv

✅ Create .env File

In our project root:

EMAIL=your_gmail@gmail.com
APP_PASSWORD=your_gmail_app_password
SECRET_KEY=random_generated_string

> ⚠ Get APP_PASSWORD from Google App Passwords (2-step verification must be on)

---

✅ Future Improvements

OTP expiration time

Password reset via email

Admin panel

Frontend design using Bootstrap
