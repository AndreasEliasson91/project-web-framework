from application.bll.controllers import admin_controller, user_controller
from flask import Blueprint, render_template, redirect, request, url_for, flash
from flask_login import logout_user, current_user

bp_open = Blueprint('bp_open',
                    __name__,
                    template_folder='templates',
                    )


@bp_open.get('/')
def index():
    return render_template('index.html')


@bp_open.get('/signin')
def signin_get():
    return render_template('signin.html')


@bp_open.post('/signin')
def signin_post():
    user_id = request.form.get('user_id').lower()
    password = request.form.get('password')

    if admin_controller.is_user_active(user_id):
        if not user_controller.verify_user(user_id, password):
            flash('Username or password is incorrect')
            return redirect(url_for('bp_open.signin_get'))

        user_controller.signin_user(user_id)
        return redirect(url_for('bp_user.profile_get', user_id=current_user._id))
    else:
        return redirect(url_for('bp_open.suspended'))


@bp_open.get('/suspended')
def suspended():
    return render_template('suspended.html')


@bp_open.get('/signup')
def signup_get():
    return render_template('signup.html')


@bp_open.post('/signup')
def signup_post():
    email = request.form.get('email').lower()
    password = request.form.get('password')
    birth_date = request.form.get('birth_date')

    user = user_controller.get_user_by_email(email)

    if user is not None:
        flash('Denna email är redan registrerad')
        return redirect(url_for('bp_open.signup_get'))

    user_controller.register_adult(email, password, birth_date)
    return redirect(url_for('bp_open.index'))


@bp_open.get('/about')
def about_get():
    return render_template('about.html')


@bp_open.get('/rules')
def rules_get():
    return render_template('rules.html')


@bp_open.get('/test_games')
def test_games_get():
    return render_template('test_games.html')


@bp_open.get('/signout')
def signout():
    logout_user()
    return render_template('signed_out_page.html')
