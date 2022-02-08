import json

from application.bll.controllers.child_suspend_user import suspend_child
from application.bll.controllers.parent_admin import get_all_children_from_db
from application.bll.controllers.parent_control import child_control_clock
from application.bll.controllers.user_controller import register_child, get_user_by_username, update_user_information
from flask import Blueprint, render_template, redirect, request, url_for, flash
from flask_login import login_required, current_user

bp_parent = Blueprint('bp_parent',
                      __name__,
                      template_folder='templates',
                      url_prefix='/parent'
                      )


@bp_parent.get('/register-child')
@login_required
def register_child_get():
    return render_template('register_child.html')


@bp_parent.post('/register-child')
@login_required
def register_child_post():
    username = request.form.get('username').lower()
    password = request.form.get('password')
    birth_date = request.form.get('birth_date')

    user = get_user_by_username(username)

    if user is not None:
        flash('En användare med detta användarnamn existerar redan')
        return redirect(url_for('bp_parent.register_child_get'))

    register_child(username, password, birth_date)
    child = get_user_by_username(username)

    current_user.children.append(child._id)
    update_user_information(current_user)

    return redirect(url_for('bp_open.index'))


@bp_parent.get('/control')
@login_required
def control_get():
    listan = get_all_children_from_db()
    return render_template('parent_admin.html', listan=listan)


@bp_parent.post('/control')
@login_required
def control_post():
    status_on_user = ""
    child = request.form.get('List1')
    child_status = suspend_child(child)
    if child_status == 'activated':
        status_on_user = 'suspended'
    else:
        status_on_user = "activated"

    listan = get_all_children_from_db()
    return render_template('parent_admin.html', listan=listan, active_suspend=json.dumps(status_on_user))


@bp_parent.post('/control')
@login_required
def control_post_clock():
    start = request.form.get('start')
    end = request.form.get('end')
    xx = request.form.get('t1')
    child_control_clock(xx, start, end)
    listan = get_all_children_from_db()
    return redirect(url_for('bp_parent.control_get', listan=listan))
