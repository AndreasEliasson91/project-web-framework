from application.dll.db.models import User


def suspend_email_user(email):
    global operation, _id, admin, parent, password, children, birth_date, date_created, act, date_end, settings, time_start, time_end, date_start
    test_lista = []

    user1 = User.find(email=email)

    for selected_user in user1:
        user_dict = selected_user.__dict__

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
            test_lista.append(value)
            if key == 'activated':
                value = 'false'

                update_user_dict = User(
                    {'_id': _id, 'email': email, 'password': password, 'birth_date': birth_date
                        , 'admin': admin, 'parent': parent, 'children': children, 'date_created': date_created
                        , 'activated': act, 'time_start': time_start, 'time_end': time_end, 'date_start': date_start,
                     'date_end': date_end, 'avatar': avatar})

                User.save(update_user_dict)
                operation = "Suspended"
                # print(key, ' : ', value)
    return operation
