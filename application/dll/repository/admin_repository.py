from application.dll.repository import user_repository


def suspend_user(user):
    if user is not None:
        user.activated = not user.activated
        user_repository.update_user_information(user)
        return 'aktiverad' if user.activated else 'avstängd'


def child_control_clock(child_id, start, end):
    child = user_repository.get_user(username=child_id)
    child.time_start = start
    child.time_end = end
    user_repository.update_user_information(child)
