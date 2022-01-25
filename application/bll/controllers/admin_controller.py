from application.dll.repository import admin_repository


def get_all_users_from_db():
    return admin_repository.get_all_users_from_db()
