import json
from application.bll.controllers.user_controller import get_all_users
from flask import Blueprint, render_template, redirect, url_for, request
from flask_login import login_required, current_user

bp_admin = Blueprint('bp_admin',
                     __name__,
                     template_folder='templates',
                     url_prefix='/admin'
                     )


@bp_admin.before_request
def before_request():
    if not current_user.admin:
        return redirect(url_for('bp_open.index'))


@bp_admin.get('/')
@login_required
def admin_get():
    return render_template('admin.html',
                           user_list=[value for user in get_all_users() for key, value in user.__dict__.items() if key == 'email'])


@bp_admin.post('/')
@login_required
def admin_post():
    from application.bll.controllers.admin_controller import suspend_user
    # Suspendera användaren eller aktivera
    email = request.form.get('List1')
    return render_template('admin.html',
                           user_list=[value for user in get_all_users() for key, value in user.__dict__.items() if key == 'email'],
                           active_suspend=json.dumps(suspend_user(email)))

