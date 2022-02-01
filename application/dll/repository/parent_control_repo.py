import username

from application.dll.db.models import User


def child_control_clock(username, start, end):
    child = User.find(username=username).first_or_none()

    child.time_start = start
    child.time_end = end
    child.save()

