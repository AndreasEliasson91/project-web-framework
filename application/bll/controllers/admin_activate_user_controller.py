from application.dll.repository import admin_activate_user_repository


def activate_email_user(email):
    return admin_activate_user_repository.activate_email_user(email)