from itsdangerous import SignatureExpired, URLSafeTimedSerializer

from application.bll.controllers import admin_controller, user_controller
from flask import Blueprint, render_template, redirect, request, url_for, flash
from flask_login import logout_user, current_user

from application.bll.controllers.user_controller import time_is_right, get_user_by_email

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

    if not user_controller.verify_user(user_id, password):
        flash('Username or password is incorrect')
        return redirect(url_for('bp_open.signin_get')) 

    if admin_controller.is_user_active(user_id, 1 if '@' in user_id else 2):
        if '@' not in user_id:
            if time_is_right(user_id):
                flash('You cannot log in at this time')
                return redirect(url_for('bp_open.signin_get'))
            user_controller.signin_user(user_id)
            return redirect(url_for('bp_user.profile_get', user_id=current_user._id))
    else:
        return redirect(url_for('bp_open.suspended'))


@bp_open.get('/suspended')
def suspended():
    return render_template('suspended.html')


@bp_open.get('/signin/forgot_password')
def forgot_get():
    return render_template('forgot_password.html')


@bp_open.post('/signin/forgot_password')
def forgot_post():
    email = request.form.get('email').lower()
    user = user_controller.get_user_by_email(email)
    if user is not None:
        user_controller.send_email_password(email)
        flash('Emailet skickades!')
    else:
        flash('Det gick inte att skicka till e postaddressen')
    return redirect(url_for('bp_open.signin_get'))

@bp_open.get('/forgot_password/<token>')
def forgot_password_get(token):
    from application.settings import SECRET_KEY
    s = URLSafeTimedSerializer([SECRET_KEY])
    try:
        email = s.loads(token, salt='password', max_age=3600)
        user_controller.signin_user(email)
    except SignatureExpired:
        return '<h1>Tiden för att byta lösenord gick ut, begär en ny länk igen för att byta lösenord</h1>'
    return render_template('change_password_by_link.html', token=token)


@bp_open.post('/forgot_password/<token>')
def forgot_password_post(token):
    email = current_user.email
    password = request.form.get('password')
    user_controller.change_user_password(email, password)
    flash('Lösenordet ändrades!')
    return redirect(url_for('bp_user.profile_get', user_id=current_user._id))


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
    user_controller.send_email_registration(email)
    return redirect(url_for('bp_open.index'))


@bp_open.get('/verified/<token>')
def verified_get_link(token):
    s = URLSafeTimedSerializer([SECRET_KEY])
    try:
        email = s.loads(token, salt='email-confirm', max_age=86400)
    except SignatureExpired:
        return '<h1>The token is expired!</h1>'
    user_controller.verify_user_email(email)
    return render_template('email_activiation.html')




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
