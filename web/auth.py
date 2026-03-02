from flask import Blueprint, render_template

auth = Blueprint('auth',__name__)

@auth.route('/login')
def login():
    return render_template("login.html", boolean=True)

@auth.route('/sign-up')
def signup():
    return render_template("sign_up.html")


@auth.route('/logout')
def logout():
    return "<h1>Logout</h1>"

@auth.route('/profile')
def profile():
    return "<h1>Profile</h1>"
    
@auth.route('/home')
def home():
    return render_template("home.html")