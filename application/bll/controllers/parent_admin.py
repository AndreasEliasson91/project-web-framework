from application.dll.repository import parent_admin


def get_all_children_from_db():
    return parent_admin.get_all_children_from_db()
