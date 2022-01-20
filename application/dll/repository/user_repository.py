from application.dll.db.models import User


def create_parent(parent):
    User.save(parent)


def create_child(child):
    User.save(child)


def get_user_by_username(username):
    return User.find(username=username).first_or_none()
