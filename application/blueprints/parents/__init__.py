import json

from application.bll.controllers import user_controller
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

    user = user_controller.get_user(username=username)

    if user is not None:
        flash('En användare med detta användarnamn existerar redan')
        return redirect(url_for('bp_parent.register_child_get'))

    user_controller.register_child(username, password, birth_date)
    child = user_controller.get_user(username=username)

    current_user.children.append(child._id)
    user_controller.update_user_information(current_user)

    return redirect(url_for('bp_open.index'))


@bp_parent.get('/control')
@login_required

def control_child_get():
    return render_template('parent_admin.html',
                           listan=[value for user in user_controller.get_all_users() for key, value in user.__dict__.items() if key == 'username'])


@bp_parent.post('/control')
@login_required
def control_child_post():
    from application.bll.controllers.admin_controller import child_control_clock, suspend_user

    if request.form.get('List1'):
        child = request.form.get('List1')
        return render_template('parent_admin.html',
                               listan=[value for user in user_controller.get_all_users() for key, value in user.__dict__.items() if key == 'username'],
                               active_suspend=json.dumps(suspend_user(child)))
    else:
        start = request.form.get('start')
        end = request.form.get('end')
        child_id = request.form.get('t1')
        child_control_clock(child_id, start, end)
        return render_template('parent_admin.html',
                               listan=[value for user in user_controller.get_all_users() for key, value in user.__dict__.items() if key == 'username'])
