from application.dll.db import init_db
from flask import Flask
from flask_login import LoginManager


def create_app():
    _app = Flask(__name__)
    _app.config.from_pyfile('settings.py')
    init_db(_app)

    from application.blueprints.open import bp_open
    _app.register_blueprint(bp_open)

    from application.blueprints.parents import bp_parent
    _app.register_blueprint(bp_parent)

    from application.blueprints.users import bp_user
    _app.register_blueprint(bp_user)

    login_manager = LoginManager()
    login_manager.init_app(_app)

    @login_manager.user_loader
    def load_user(user_id):
        from application.bll.controllers.user_controller import get_user_by_email, get_user_by_username
        if '@' in user_id:
            return get_user_by_email(user_id)
        else:
            return get_user_by_username(user_id)


    return _app

