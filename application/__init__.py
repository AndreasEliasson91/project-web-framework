from application.dll.db import init_db
from flask import Flask
from flask_debugtoolbar import DebugToolbarExtension
from flask_login import LoginManager


def create_app():
    _app = Flask(__name__)
    _app.config.from_pyfile('settings.py')
    init_db(_app)

    # toolbar = DebugToolbarExtension(_app)

    from application.blueprints.open import bp_open
    _app.register_blueprint(bp_open)


    from application.blueprints.parents import bp_parent
    _app.register_blueprint(bp_parent)
    login_manager = LoginManager()
    login_manager.init_app(_app)

    from application.blueprints.users import bp_user
    _app.register_blueprint(bp_user)

    @login_manager.user_loader
    def load_user(user_id):
        from application.dll.db.models import User
        if '@' in user_id:
            return User.find(email=user_id).first_or_none()
        else:
            return User.find(username=user_id).first_or_none()

    return _app


if __name__ == '__main__':
    create_app().run()
