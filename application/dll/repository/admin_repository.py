import application
from application.dll import db
from application.dll.db.models import User


def get_all_users_from_db():
    def get_all_user_emails():

        counter = 0
        get_users = User.find()
        e_listan = []
        for db_users in get_users:
            data_from_user = db_users.__dict__

            for key, value in data_from_user.items():
                if key == 'email':
                    e_listan.append(value)
                    # print(key, ' : ', value)
                else:
                    pass
            # e_listan.append(data_from_user)

        print(e_listan)

    get_all_user_emails()

    # # global val
    # user_list = []
    # # x = []
    # get_users = User.find()
    # user_list = []
    # counter = 0
    # for user in get_users:
    #     x = str(user)
    #     ch = []
    #     (_id, email, password, birth_date, admin, parent, ch, date_created) = x
    #     print(email)
    #
    #     look1 = "email = "
    #     look2 = "."
    #     found_string = x.find(look1)
    #     found2_string = x.find(look2)
    #
    #     complete_string = (x[found_string + 8:found2_string + 4])
    #     print(complete_string)
    #     print(x)
    # obj_id = (user['_id'])
    # email = (user['email'])
    # password = (user['password'])

    # xx = (user['email': 'email'])
    # val = x[1]
    # idel, email, password, birth_date, admin, parent, child, date_created = str(x.split)

    # user_list.append(val)
    # print()
    # print(type(x))
    # print()
# return user_list
