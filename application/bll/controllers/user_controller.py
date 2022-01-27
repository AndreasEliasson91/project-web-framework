import datetime
import random

from application.dll.repository import user_repository, image_repository
from flask_login import login_user
from passlib.hash import argon2
from typing import Optional
from werkzeug.security import check_password_hash


def register_adult(email, password, birth_date):
    birth_date = birth_date.split('-')
    birth_date = datetime.datetime(int(birth_date[0]), int(birth_date[1]), int(birth_date[2]))

    adult = {
            'email': email,
            'password': argon2.using(rounds=12).hash(password),
            'birth_date': birth_date,
            'admin': False,
            'parent': True,
            'activated:': True,
            'time_management': None,
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
    user_repository.register_adult(adult)


def register_child(username, password, birth_date: Optional):
    child = {
            'username': username,
            'password': argon2.using(rounds=12).hash(password),
            'parent': False,
            'activated:': True,
            'time_management': None,
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
    user_repository.register_child(child)


def update_user_information(user):
    return user_repository.update_user_information(user)


def get_user_by_email(email):
    return user_repository.get_user_by_email(email)


def get_user_by_username(username):
    return user_repository.get_user_by_username(username)


def get_user_by_user_id(user_id):
    return user_repository.get_user_by_user_id(user_id)


def verify_user(user_id, password):
    if '@' in user_id:
        user = get_user_by_email(user_id)
    else:
        user = get_user_by_username(user_id)

    if user is None:
        return False

    if user.password.startswith('pbkdf2:sha256'):
        verified = check_password_hash(user.password, password)
        if verified:
            user.password = argon2.using(rounds=12).hash(password)
            user.save()
        return verified
    return argon2.verify(password, user.password)


def signin_user(user_id):
    if '@' in user_id:
        user = get_user_by_email(user_id)
    else:
        user = get_user_by_username(user_id)

    if user is not None:
        login_user(user)
        user.last_signin = datetime.datetime.now()
        user.save()
