import datetime
import time
from flask import Flask, request, url_for
from flask_mail import Mail, Message
from itsdangerous import URLSafeTimedSerializer, SignatureExpired

from bson import ObjectId
from passlib.handlers.argon2 import argon2


from application.dll.db.models import User


def register_adult(adult):
    User(adult).save()


def register_child(child):
    User(child).save()


def update_user_information(user):
    User.save(user)


def get_user_by_email(email):
    return User.find(email=email).first_or_none()


def get_user_by_username(username):
    return User.find(username=username).first_or_none()


def get_user_by_user_id(user_id):
    return User.find(_id=ObjectId(user_id)).first_or_none()


def get_user(**kwargs):
    if '_id' in kwargs:
        kwargs.value = ObjectId(kwargs.value)
    return User.find(**kwargs).first_or_none()


def get_parent_from_child_id(_id):
    users = User.all()
    for user in users:
        if user.parent:
            for child in user.children:
                if child == _id:
                    return user
    return None


def get_all_users():
    return User.all()

def time_is_right(user_id):

    child = get_user_by_username(user_id)
    start_time = child.time_start
    end_time = child.time_end
    if start_time and end_time is not None:
        start_time = start_time.replace(":", "")
        end_time = end_time.replace(":", "")

        hour = datetime.datetime.now().hour
        minute = datetime.datetime.now().minute
        timed = f"{hour}{minute}"

        if int(start_time) < int(timed) or int(timed) > int(end_time):
            return True
        else:
            return False
    else:
        return False


def send_email_registration(email):
    from application.settings import SECRET_KEY

    mail = Mail()
    s = URLSafeTimedSerializer([SECRET_KEY])
    token = s.dumps(email, salt='email-confirm')
    link = url_for('bp_open.verified_get_link', token=token, _external=True)
    msg = Message('confirm_email', sender='learnbygamesnow@gmail.com', recipients=[email])
    msg.body = f'Your  activation link is {link}'
    mail.send(msg)


def verify_user_email(email):
    user = get_user_by_email(email)
    user.verified = True
    user.save()

def change_user_password(email, password):
    user = get_user_by_email(email)
    user.password = argon2.using(rounds=12).hash(password)
    user.save()


def is_user_verified(user_id):
    user = get_user_by_email(user_id)
    if user.verified:
        return True
    else:
        return False


def send_email_password(email):
    from application.settings import SECRET_KEY

    mail = Mail()
    s = URLSafeTimedSerializer([SECRET_KEY])
    token = s.dumps(email, salt='password')
    link = url_for('bp_open.forgot_password_get', token=token, _external=True)
    msg = Message('Forgot Password', sender='learnbygamesnow@gmail.com', recipients=[email])
    msg.body = f'Your  link to reset your password is {link}, if you did not ask for this link your account may be' \
               f'compromised, log in and change your password on our website.'
    mail.send(msg)
