from flask import Blueprint, render_template, redirect, url_for, request
from flask_login import login_required, current_user

from application.bll.controllers.admin_controller import get_all_users_from_db
from application.bll.controllers.admin_suspend_email_user import suspend_email_user
from application.dll.db.models import User

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
def admin():
    listan = get_all_users_from_db()
    return render_template('admin.html', listan=listan)


@bp_admin.post('/')
@login_required
def admin_post():
    email = request.form.get('List1')

    user_suspend = suspend_email_user(email)
    listan = get_all_users_from_db()
    print(user_suspend)
    return render_template('admin.html', listan=listan)
    # if user is not None:
    #     flash('Denna email är redan registrerad')
    #     return redirect(url_for('bp_open.signup_get'))
    #
    # register_adult(email, password, birth_date)
    # return redirect(url_for('bp_open.index'))
