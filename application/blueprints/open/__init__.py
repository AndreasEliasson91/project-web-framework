from application.bll.controllers.user_controller import register_adult, get_user_by_email, get_user_by_username
from flask import Blueprint, render_template, redirect, request, url_for, flash
from flask_login import login_user
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

    if '@' in username:
        user = get_user_by_email(username)
    else:
        user = get_user_by_username(username)

    if user is None:
        flash('Username or password is incorrect')
        return redirect(url_for('bp_open.signin_get'))

    if not check_password_hash(user.password, password):
        flash('Username or password is incorrect')
        return redirect(url_for('bp_open.signin_get'))

    login_user(user)
    return redirect(url_for('bp_user.user_index'))


@bp_open.get('/signup')
def signup_get():
    return render_template('signup.html')


@bp_open.post('/signup')
def signup_post():
    email = request.form.get('email')
    password = request.form.get('password')
    birth_date = request.form.get('birth_date')

    user = get_user_by_email(email)

    if user is not None:
        flash('Denna email är redan registrerad')
        return redirect(url_for('bp_open.signup_get'))




    register_adult(email, password, birth_date)
    return redirect(url_for('bp_open.index'))


@bp_open.get('/')
def index():
    return render_template('index.html')


@bp_open.get('/user/user')
def profile_get_view():
    return render_template('profile_parent_view.html')


@bp_open.get('/about')
def about_get():
    return render_template('about.html')


@bp_open.get('/game_rules')
def rules_get():
    return render_template('game_rules.html')


@bp_open.get('/games')
def games_get():
    return render_template('games.html')


@bp_open.get('/test_games')
def test_games_get():
    return render_template('test_games.html')


@bp_open.get('/signout')
def signout():
    logout_user()
    return render_template('signed_out_page.html')

