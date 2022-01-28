from application.dll.db.models import User


def is_user_active(username, selected_val):
    global act
    if selected_val == 1:
        user1 = User.find(email=username)

    else:
        user1 = User.find(username=username)

    for selected_user in user1:
        user_dict = selected_user.__dict__

        # Here we loop through everything and take out the key and value from the dict.
        for key, value in user_dict.items():

            if key == 'activated':
                act = value

    return act
