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
    username = request.form.get('username')
    password = request.form.get('password')
    birth_date = request.form.get('birth_date')

    user = get_user_by_username(username)

    if user is not None:
        flash('En användare med detta användarnamn existerar redan')
        return redirect(url_for('bp_parent.register_child_get'))

    register_child(username, password, birth_date)
    child = get_user_by_username(username)

    current_user.children.append(
        {
            '_id': child._id,
            'username': child.username,
            'avatar': child.avatar
        }
    )
    update_user_information(current_user)

    return redirect(url_for('bp_open.index'))
