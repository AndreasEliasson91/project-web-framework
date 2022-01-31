from application.dll.db.models import User
from application.dll.repository import user_repository


def suspend_email_user(email):
    # Here we are looking for the selected users email, and take out the user dict.
    user = User.find(email=email).first_or_none()

    if user is not None:
        user.activated = not user.activated
        user_repository.update_user_information(user)

        return "Suspended" if user.activated else "Activated"


def is_user_active(user_id):
    if '@' in user_id:
        user = User.find(email=user_id).first_or_none()
    else:
        user = User.find(username=user_id).first_or_none()

    return user.activated

