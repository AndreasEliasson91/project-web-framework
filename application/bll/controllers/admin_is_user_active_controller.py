from application.dll.repository import admin_is_user_active_repository


def is_user_activate(username, selected_val):
    return admin_is_user_active_repository.is_user_active(username, selected_val)
