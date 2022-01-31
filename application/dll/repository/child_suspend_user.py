from application.dll.db.models import User


def suspend_child(username):
    # user_status = "Suspended"
    # Here we are looking for the selected users email, and take out the
    # the user dict.
    user1 = User.find(username=username).first_or_none()

    if user1 is not None:
        if user1.activated == True:
            user_status = "Suspended"
            user1.activated = not user1.activated
            user1.save()
        else:
            user_status ="Activated"
            user1.activated = not user1.activated
            user1.save()
    return user_status

    # if user1 is not None:
    #     user1.activated = not user1.activated
    #     user1.save()
    # return user_status
