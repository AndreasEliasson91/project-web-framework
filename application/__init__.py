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

    login_manager = LoginManager()
    login_manager.init_app(_app)

    @login_manager.user_loader
    def load_user(user_id):
        from application.dll.db.models import User
        return User.find(_id=user_id).first_or_none()

    return _app


if __name__ == '__main__':
    create_app().run()
