from application.bll.controllers.user_controller import register_adult, get_user_by_email, verify_user, signin_user
from flask import Blueprint, render_template, redirect, request, url_for, flash
from flask_login import logout_user

bp_open = Blueprint('bp_open',
                    __name__,
                    template_folder='templates',
                    )


@bp_open.get('/signin')
def signin_get():
    return render_template('signin.html')


@bp_open.post('/signin')
def signin_post():
    user_id = request.form.get('user_id')
    password = request.form.get('password')

    if not verify_user(user_id, password):
        flash('Username or password is incorrect')
        return redirect(url_for('bp_open.signin_get'))

    signin_user(user_id)

    return redirect(url_for('bp_user.profile_get'))


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

