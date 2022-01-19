import datetime

from application.dll.db.models import User
from typing import Optional
from werkzeug.security import generate_password_hash

from application.dll.repository import user_repository


def create_parent(email, password, birth_date):
    birth_date = birth_date.split('-')
    birth_date = datetime.datetime(int(birth_date[0]), int(birth_date[1]), int(birth_date[2]))

    parent = User(
        {
            'email': email,
            'password': generate_password_hash(password),
            'birth_date': birth_date,
            'admin': False,
            'parent': True,
            'children': [],
            'date_created': datetime.datetime.now(),
        }
    )
    user_repository.create_parent(parent)


def create_child(username, password, birth_date: Optional):
    child = User(
        {
            'username': username,
            'password': generate_password_hash(password),
            'parent': False,
            'personal_high_score': [],
            'date_created': datetime.datetime.now()
        }
    )

    if birth_date:
        birth_date = birth_date.split('-')
        child['birth_date'] = datetime.datetime(int(birth_date[0]), int(birth_date[1]), int(birth_date[2]))

    user_repository.create_child(child)
