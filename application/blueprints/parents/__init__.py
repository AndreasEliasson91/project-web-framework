from flask import Blueprint, render_template, redirect, request, url_for, flash
from flask_login import login_user, logout_user, login_required
from werkzeug.security import check_password_hash

from application.bll.controllers.user_controller import create_child

bp_parent = Blueprint('bp_parent',
                      __name__,
                      template_folder='templates',
                      url_prefix='/parent'
                      )


@bp_parent.get('/register-child')
# @login_required
def register_child_get():
    return render_template('register_child.html')


@bp_parent.post('/register-child')
# @login_required
def register_child_post():
    username = request.form.get('child_username')
    password = request.form.get('child_password_1')
    birth_date = request.form.get('child_birth_date')

    from application.dll.db.models import User
    user = User.find(username=username).first_or_none()

    if user is not None:
        flash('En användare med detta användarnamn existerar redan'
              '')
        return redirect(url_for('bp_parent.register_child_get'))

    create_child(username, password, birth_date)
    return redirect(url_for('bp_open.fake_index'))
