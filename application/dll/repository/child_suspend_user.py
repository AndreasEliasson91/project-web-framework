from application.dll.db.models import User
from application.dll.repository import user_repository


def suspend_child(username):
    user = User.find(username=username).first_or_none()
    if not user.parent:

        if user is not None:
            user.activated = not user.activated
            user_repository.update_user_information(user)
            return 'Activated' if user.activated else 'Suspended'
