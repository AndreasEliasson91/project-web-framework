from application.dll.repository import admin_suspend_email_user_repository


def suspend_email_user(email, is_selected_user_active):
    return admin_suspend_email_user_repository.suspend_email_user(email, is_selected_user_active)
