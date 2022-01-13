from flask import Flask
from flask_login import LoginManager


def create_app():
    _app = Flask(__name__)
    _app.config.from_pyfile('settings.py')

    login_manager = LoginManager()
    login_manager.init_app(_app)

    return _app


if __name__ == '__main__':
    create_app().run()
