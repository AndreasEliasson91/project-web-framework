import datetime
import random

from application.dll.db.models import User
from application.dll.repository import user_repository, image_repository
from typing import Optional
from werkzeug.security import generate_password_hash


def register_adult(email, password, birth_date):
    birth_date = birth_date.split('-')
    birth_date = datetime.datetime(int(birth_date[0]), int(birth_date[1]), int(birth_date[2]))

    parent = User(
        {
            'email': email,
            'password': generate_password_hash(password),
            'birth_date': birth_date,
            'admin': False,
            'parent': True,
            #'children': [],
            'date_created': datetime.datetime.now(),
           # 'avatar': random.choice(image_repository.get_all_image_ids())
        }
    )
    user_repository.register_adult(parent)


def register_child(username, password, birth_date: Optional):
    child = User(
        {
            'username': username,
            'password': generate_password_hash(password),
            'parent': False,
            'personal_high_score': [],
            'date_created': datetime.datetime.now(),
            'avatar': random.choice(image_repository.get_all_image_ids())
        }
    )

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

