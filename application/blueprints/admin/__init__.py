import json
from application.bll.controllers import admin_controller
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
    return render_template('admin.html', listan=admin_controller.get_all_users_from_db())


@bp_admin.post('/')
@login_required
def admin_post():
    # Suspendera användaren eller aktivera
    email = request.form.get('List1')
    user_status = admin_controller.suspend_email_user(email)
    if user_status == "Activated":
        user_status = "suspended"
    else:
        user_status = "activated"

    return redirect(url_for('bp_admin.admin_get',
                    listan=admin_controller.get_all_users_from_db(),
                    status=json.dumps(user_status)))

