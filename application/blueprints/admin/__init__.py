from flask import Blueprint, render_template, redirect, url_for
from flask_login import login_required, current_user

from application.bll.controllers.admin_controller import get_all_users_from_db
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

