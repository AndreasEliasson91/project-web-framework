from flask import Blueprint, render_template, redirect, request, url_for, flash
from flask_login import login_user, logout_user, login_required
from werkzeug.security import check_password_hash


bp_open = Blueprint('bp_open',
                    __name__,
                    template_folder='templates'
                    )


@bp_open.get('/')
def index():
    return render_template('base.html')

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