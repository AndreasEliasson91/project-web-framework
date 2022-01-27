from application.dll.db.models import User


def is_user_active(email):

    global act
    user1 = User.find(email=email)

    for selected_user in user1:
        user_dict = selected_user.__dict__

        # Here we loop through everything and take out the key and value from the dict.
        for key, value in user_dict.items():
            if key == '_id':
                _id = value

            if key == 'email':
                email = value

            if key == 'password':
                password = value

            if key == 'birth_date':
                birth_date = value

            if key == 'admin':
                admin = value

            if key == 'parent':
                parent = value

            if key == 'children':
                children = value

            if key == 'date_created':
                date_created = value

            if key == 'activated':
                act = value

            if key == 'time_start':
                time_start = value
            if key == 'time_end':
                time_end = value
            if key == 'date_start':
                date_start = value
            if key == 'date_end':
                date_end = value

            if key == 'avatar':
                avatar = value

    return act
