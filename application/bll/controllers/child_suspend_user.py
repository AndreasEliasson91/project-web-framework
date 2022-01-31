from application.dll.repository import child_suspend_user


def suspend_child(username):
    return child_suspend_user.suspend_child(username)

