from application.dll.db.models import User


def suspend_email_user(email):
    global operation, _id, admin, parent, password, children, birth_date, date_created
    test_lista = []

    user1 = User.find(email=email)

    for selected_user in user1:
        user_dict = selected_user.__dict__

        for key, value in user_dict.items():
            if key == '_id':
                _id = value

                test_lista.append(value)
            if key == 'email':
                email = value

                test_lista.append(value)
            if key == 'password':
                password = value

                test_lista.append(value)
            if key == 'birth_date':
                birth_date = value

                test_lista.append(value)
            if key == 'admin':
                admin = value

                test_lista.append(value)
            if key == 'parent':
                parent = value

                test_lista.append(value)
            if key == 'children':
                children = value

                test_lista.append(value)
            if key == 'date_created':
                date_created = value
            test_lista.append(value)
            if key == 'activated':
                value = 'false'

                update_user_dict = User(
                    {'_id': _id, 'email': email, 'password': password, 'birth_date': birth_date
                        , 'admin': admin, 'parent': parent, 'children': children, 'date_created': date_created
                        , 'activated': value})

                User.save(update_user_dict)
                operation = "Suspended"
                # print(key, ' : ', value)
    return operation
