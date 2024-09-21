import os
from flask import Flask, redirect, url_for, render_template, request, session, flash, json

from datetime import timedelta



app = Flask(__name__)



app.config['SECRET_KEY'] = os.urandom(24)
# csrf = CSRFProtect(app)
# oauth = OAuth(app)
# app.config['GOOGLE_CLIENT_ID'] = 'google_client_id'
# app.config['GOOGLE_CLIENT_SECRET'] = 'google_client_secret_key'


# reCAPTCHA configuration
# app.config['RECAPTCHA_PUBLIC_KEY'] = 'recaptcha_public_key'
# app.config['RECAPTCHA_PRIVATE_KEY'] = 'recaptcha_private_key'


# Set up the database URI
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///project.db'  # Using SQLite for simplicity
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.permanent_session_lifetime = timedelta(days=7)



# Home route
# @app.route('/')
# def home():
#     return 'This is Flask.'

@app.route('/')
@app.route('/login', methods=['GET', 'POST'])
def signup_login():
    return render_template('signup-login-form.html')


if __name__ == '__main__':
    app.run(debug=True)
