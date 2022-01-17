from flask import Blueprint, render_template, redirect, request, url_for
from flask_login import login_user, logout_user, login_required
from werkzeug.security import check_password_hash

bp_open = Blueprint('bp_open',
                    __name__,
                    template_folder='templates'
                    )


@bp_open.get('/signup')
def signup_get():
    return render_template('signup.html')


@bp_open.get('/')
def index():
    return render_template('index.html')
