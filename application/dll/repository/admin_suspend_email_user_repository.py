from application.dll.db.models import User


def suspend_email_user(email, is_selected_user_active):
    # Here we are looking for the selected users email, and take out the
    # the user dict.
    user1 = User.find(email=email).first_or_none()
    if user1 is not None:
        user1.activated = not user1.activated
        user1.save()
