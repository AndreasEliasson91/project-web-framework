import dotenv

from flask import Flask
from flask_login import LoginManager


def create_app():
    _app = Flask(__name__)
    _app.config.from_pyfile('settings.py')
    _app.config.from_pyfile('config.cfg')

    from flask_mail import Mail
    mail = Mail(_app)

    from application.dll.db import init_db
    init_db(_app)

    from application.blueprints.open import bp_open
    _app.register_blueprint(bp_open)

    from application.blueprints.parents import bp_parent
    _app.register_blueprint(bp_parent)

    from application.blueprints.users import bp_user
    _app.register_blueprint(bp_user)

    from application.blueprints.admin import bp_admin
    _app.register_blueprint(bp_admin)

    from application.blueprints.games import bp_games
    _app.register_blueprint(bp_games)

    login_manager = LoginManager()
    login_manager.init_app(_app)

    @login_manager.user_loader
    def load_user(user_id):
        from application.bll.controllers.user_controller import check_parent_status, get_user
        if check_parent_status(user_id):
            return get_user(email=user_id)
        else:
            return get_user(username=user_id)

    return _app


if __name__ == '__main__':
    dotenv.load_dotenv()
    create_app().run(debug=True)

