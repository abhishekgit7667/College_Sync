from flask import Flask, render_template, request, redirect, session, flash
from otp_utils import generate_otp, send_otp_email
from database import init_db, create_user, verify_user
import bcrypt

app = Flask(__name__)
app.secret_key = "your_secret_key_here"  # Change it in production

# Initialize database
init_db()

# Store OTPs temporarily
user_otps = {}

@app.route("/")
def home():
    return redirect("/login")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        password = request.form["password"]

        hashed_pw = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

        otp = generate_otp()
        user_otps[email] = {"otp": otp, "name": name, "password": hashed_pw}

        send_otp_email(email, otp)
        flash("OTP sent to your email.")
        return redirect("/verify")
    
    return render_template("register.html")

@app.route("/verify", methods=["GET", "POST"])
def verify():
    if request.method == "POST":
        email = request.form["email"]
        otp_input = request.form["otp"]

        if email in user_otps and user_otps[email]["otp"] == otp_input:
            user = user_otps.pop(email)
            create_user(user["name"], email, user["password"])
            flash("Account created. Please login.")
            return redirect("/login")
        else:
            flash("Invalid OTP.")
    
    return render_template("otp_verify.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]

        user = verify_user(email)
        if user and bcrypt.checkpw(password.encode('utf-8'), user["password"]):
            session["user"] = user["name"]
            return redirect("/dashboard")
        else:
            flash("Invalid login details.")
    
    return render_template("login.html")

@app.route("/dashboard")
def dashboard():
    if "user" not in session:
        return redirect("/login")
    return render_template("dashboard.html", name=session["user"])

@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect("/login")

if __name__== "__main__":
    print("starting the server....")
    app.run(debug=True)