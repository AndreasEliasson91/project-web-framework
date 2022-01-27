from application.dll.db.models import User


def activate_email_user(email):
    global operation, _id, admin, parent, password, children, birth_date, date_created, act, date_end, settings, \
        time_start, time_end, date_start, rgb_title, rgb_subtitle
    test_lista = []

    # Here we are looking for the selected users email, and take out the
    # the user dict.
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
                act = 'true'

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

            # Take out the second dict called settings.
            if user_dict.values == 'settings':
                print("Hello")

            for ettan, tvåan in user_dict.items():
                if ettan == 'settings':
                    for k, v in tvåan.items():
                        if k == 'rgb_title':
                            rgb_title = v
                        if k == 'rgb_subtitle':
                            rgb_subtitle = v

                # Here we build up the dict as it was, and we changed the activate field to false.
                update_user_dict = User(
                    {'_id': _id, 'email': email, 'password': password, 'birth_date': birth_date
                        , 'admin': admin, 'parent': parent, 'children': children, 'date_created': date_created
                        , 'activated': act, 'time_start': time_start, 'time_end': time_end, 'date_start': date_start,
                     'date_end': date_end, 'avatar': avatar,
                     'settings': {'rgb_title': rgb_title, 'rgb_subtitle': rgb_subtitle}
                     })
                # update the dict to the database.
                User.save(update_user_dict)
                operation = "Active"
                # print(key, ' : ', value)
    return operation
