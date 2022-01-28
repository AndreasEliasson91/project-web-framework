from flask import Blueprint, render_template, redirect, url_for, request
from flask_login import login_required, current_user
import json
from application.bll.controllers.admin_activate_user_controller import activate_email_user
from application.bll.controllers.admin_controller import get_all_users_from_db
from application.bll.controllers.admin_is_user_active_controller import is_user_activate
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
    # Suspendera användaren eller aktivera
    email = request.form.get('List1')
    user_status = suspend_email_user(email)
    if user_status == "Activated":
        user_status = "suspended"
    else:
        user_status = "activated"

    listan = get_all_users_from_db()

    return render_template('admin.html', listan=listan, active_suspend=user_status)
    # if user is not None:
    #     flash('Denna email är redan registrerad')
    #     return redirect(url_for('bp_open.signup_get'))
    #
    # register_adult(email, password, birth_date)
    # return redirect(url_for('bp_open.index'))
