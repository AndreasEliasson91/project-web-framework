from application.settings import SECRET_KEY
from flask import url_for
from flask_mail import Mail, Message
from itsdangerous import URLSafeTimedSerializer


def send_email_registration(email):
    mail = Mail()
    s = URLSafeTimedSerializer([SECRET_KEY])
    token = s.dumps(email, salt='email-confirm')
    link = url_for('bp_open.verified_get_link', token=token, _external=True)
    msg = Message('confirm_email', sender='learnbygamesnow@gmail.com', recipients=[email])
    msg.body = f'Your  activation link is {link}'
    mail.send(msg)


def send_email_password(email):
    mail = Mail()
    s = URLSafeTimedSerializer([SECRET_KEY])
    token = s.dumps(email, salt='password')
    link = url_for('bp_open.forgot_password_get', token=token, _external=True)
    msg = Message('Forgot Password', sender='learnbygamesnow@gmail.com', recipients=[email])
    msg.body = f'Your  link to reset your password is {link}, if you did not ask for this link your account may be' \
               f'compromised, log in and change your password on our website.'
    mail.send(msg)
