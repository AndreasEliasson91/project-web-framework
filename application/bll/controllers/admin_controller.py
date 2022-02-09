from application.dll.repository import admin_repository
from application.bll.controllers.user_controller import check_parent_status


def suspend_user(user_id):
    from application.dll.repository.user_repository import get_user

    if check_parent_status(user_id):
        user = get_user(email=user_id)
    else:
        user = get_user(username=user_id)

    return admin_repository.suspend_user(user)


def is_user_active(user_id):
    from application.dll.repository.user_repository import get_user

    if check_parent_status(user_id):
        user = get_user(email=user_id)
    else:
        user = get_user(username=user_id)

    return user.activated


def child_control_clock(child_id, start, end):
    return admin_repository.child_control_clock(child_id, start, end)

