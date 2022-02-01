import datetime
import time

from bson import ObjectId

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
    start_time = start_time.replace(":", "")
    end_time = end_time.replace(":", "")

    hour = datetime.datetime.now().hour
    minute = datetime.datetime.now().minute
    timed = f"{hour}{minute}"

    if int(start_time) < int(timed) or int(timed) > int(end_time):
        return True
    else:
        return False

