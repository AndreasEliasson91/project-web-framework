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
