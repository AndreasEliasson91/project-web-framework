from application.bll.controllers.user_controller import create_parent
from flask import Blueprint, render_template, redirect, request, url_for, flash
from flask_login import login_user, logout_user, login_required
from werkzeug.security import check_password_hash

bp_open = Blueprint('bp_open',
                    __name__,
                    template_folder='templates',
                    )


@bp_open.get('/signin')
def signin_get():
    return render_template('signin.html')


@bp_open.post('/signin')
def signin_post():
    username = request.form.get('username')
    password = request.form.get('password')
    from application.dll.db.models import User
    if '@' in username:
        user = User.find(email=username).first_or_none()
    else:
        user = User.find(username=username).first_or_none()
    if user is None:
        flash('Username or password is incorrect')
        return redirect(url_for('bp_open.signin_get'))

    if not check_password_hash(user.password, password):
        flash('Username or password is incorrect')
        return redirect(url_for('bp_open.signin_get'))

    login_user(user)
    return redirect(url_for('bp_open.index'))


@bp_open.get('/signup')
def signup_get():
    return render_template('signup.html')


@bp_open.post('/signup')
def signup_post():
    email = request.form.get('email')
    password = request.form.get('password')
    birth_date = request.form.get('birth_date')

    from application.dll.db.models import User
    user = User.find(email=email).first_or_none()

    if user is not None:
        flash('Denna email är redan registrerad')
        return redirect(url_for('bp_open.signup_get'))

    create_parent(email, password, birth_date)
    return redirect(url_for('bp_open.fake_index'))


@bp_open.get('/')
def index():
    return render_template('index.html')
