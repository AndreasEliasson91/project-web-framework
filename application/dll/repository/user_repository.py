import datetime

from application.dll.db.models import User
from bson import ObjectId


def get_user(**kwargs):
    # if '_id' in kwargs:
    #     kwargs.value = ObjectId(kwargs.value)
    return User.find(**kwargs).first_or_none()


def register_user(user):
    User(user).save()


def get_all_users():
    return User.all()


def update_user_information(user):
    User.save(user)


def get_parent_from_child_id(_id):
    for user in get_all_users():
        if user.parent:
            for child in user.children:
                if child == _id:
                    return user
    return None


def time_is_right(child):
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
