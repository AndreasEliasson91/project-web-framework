import datetime
import random

from application.dll.repository import user_repository, image_repository
from passlib.hash import argon2
from typing import Optional


def get_user(**kwargs):
    return user_repository.get_user(**kwargs)


def get_all_users():
    return user_repository.get_all_users()


def update_user_information(user):
    return user_repository.update_user_information(user)


def register_adult(email, password, birth_date):
    birth_date = birth_date.split('-')
    birth_date = datetime.datetime(int(birth_date[0]), int(birth_date[1]), int(birth_date[2]))

    adult = {
        'email': email,
        'display_name': email.split('@')[0],
        'password': argon2.using(rounds=12).hash(password),
        'birth_date': birth_date,
        'admin': False,
        'parent': True,
        'activated': True,
        'verified': False,
        'personal_high_score': [],
        'children': [],
        'friends': [],
        'date_created': datetime.datetime.now(),
        'avatar': random.choice(image_repository.get_all_image_ids()),
        'settings': {
            'rgb_title': (0, 0, 0),
            'rgb_subtitle': (128, 0, 128)
        }
    }

    user_repository.register_user(adult)


def register_child(username, password, birth_date: Optional):

    child = {
        'username': username,
        'password': argon2.using(rounds=12).hash(password),
        'parent': False,
        'activated': True,
        'verified': True,
        'time_start': None,
        'time_end': None,
        'personal_high_score': [],
        'friends': [],
        'date_created': datetime.datetime.now(),
        'avatar': random.choice(image_repository.get_all_image_ids()),
        'settings': {
            'rgb_title': (0, 0, 0),
            'rgb_subtitle': (128, 0, 128)
        }
    }

    if birth_date:
        birth_date = birth_date.split('-')
        child['birth_date'] = datetime.datetime(int(birth_date[0]), int(birth_date[1]), int(birth_date[2]))

    user_repository.register_user(child)


def verify_user(user_id, password):
    from werkzeug.security import check_password_hash

    if check_parent_status(user_id):
        user = get_user(email=user_id)
    else:
        user = get_user(username=user_id)

    if user is None:
        return False

    if user.password.startswith('pbkdf2:sha256'):
        verified = check_password_hash(user.password, password)
        if verified:
            user.password = argon2.using(rounds=12).hash(password)
            update_user_information(user)
        return verified
    return argon2.verify(password, user.password)


def signin_user(user_id):
    from flask_login import login_user

    if check_parent_status(user_id):
        user = get_user(eamil=user_id)
    else:
        user = get_user(username=user_id)

    if user is not None:
        login_user(user)
        user.last_signin = datetime.datetime.now()
        update_user_information(user)


def get_user_friends(current_user):
    return [user for user in get_all_users()  for friend in current_user.friends if user._id == friend]


def time_is_right(user_id):
    child = get_user(username=user_id)
    return user_repository.time_is_right(child)


def verify_user_email(email):
    user = get_user(email=email)
    user.verified = True
    update_user_information(user)


def is_user_verified(user_id):
    user = get_user(email=user_id)
    return user.verified


def change_user_password(email, password):
    user = get_user(email=email)
    user.password = argon2.using(rounds=12).hash(password)
    update_user_information(user)


def check_parent_status(user_id):
    if '@' in user_id:
        return True
    return False
