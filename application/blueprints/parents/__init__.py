import json

from application.bll.controllers import admin_controller
from application.bll.controllers.admin_controller import suspend_user
from application.bll.controllers.user_controller import register_child, get_user, update_user_information
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

    user = get_user(username=username)

    if user is not None:
        flash('En användare med detta användarnamn existerar redan')
        return redirect(url_for('bp_parent.register_child_get'))

    register_child(username, password, birth_date)
    child = get_user(username=username)

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
def control_child():

    if request.form.get('List1'):
        child = request.form.get('List1')
        child_status = suspend_user(child)
        if child_status == 'activated':
            status_on_user = 'suspended'
        else:
            status_on_user = "activated"
        listan = get_all_children_from_db()
        return render_template('parent_admin.html', listan=listan, active_suspend=json.dumps(status_on_user))
    else:
        start = request.form.get('start')
        end = request.form.get('end')
        child_id = request.form.get('t1')
        admin_controller.child_control_clock(child_id, start, end)
        return render_template('parent_admin.html', listan=get_all_children_from_db())
