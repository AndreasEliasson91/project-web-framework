from application.bll.controllers import user_controller
from application.dll.db.models import User
from flask_login import current_user


def get_all_children_from_db():
    user = current_user.children

    children_list1 = []

    for child in user:
        children = user_controller.get_user_by_user_id(child)
        children_list1.append(
            children.username
        )

    return children_list1

    #  return list_child  # render_template('parent_admin.html', listan=listan)
