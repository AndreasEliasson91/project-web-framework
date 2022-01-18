from application.bll.controllers.user_controller import create_parent
from flask import Blueprint, render_template, redirect, request, url_for, flash
from flask_login import login_user, logout_user, login_required
from werkzeug.security import check_password_hash

bp_open = Blueprint('bp_open',
                    __name__,
                    template_folder='templates',
                    )


@bp_open.get('/')
def fake_index():
    return 'Testing'


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
