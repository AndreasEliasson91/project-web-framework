from application.dll.repository import admin_suspend_email_user_repository


def suspend_email_user(email):
    return admin_suspend_email_user_repository.suspend_email_user(email)
