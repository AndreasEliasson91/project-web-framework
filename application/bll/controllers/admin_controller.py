from application.bll.controllers import user_controller
from application.dll.repository import admin_repository


def get_all_users_from_db():
    return [value for user in user_controller.get_all_users() for key, value in user.__dict__.items() if key == 'email']


def suspend_email_user(email):
    return admin_repository.suspend_email_user(email)


def is_user_active(user_id, selected_val):
    return admin_repository.is_user_active(user_id, selected_val)
