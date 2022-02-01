from application.dll.repository import parent_control_repo


def child_control_clock(child, start, end):
    return parent_control_repo.child_control_clock(child, start, end)
