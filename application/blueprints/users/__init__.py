from flask import Blueprint, render_template, redirect, request, url_for, flash
from flask_login import login_required, current_user
from application.dll.db import images


bp_user = Blueprint('bp_user',
                    __name__,
                    template_folder='templates',
                    url_prefix='/user'
                    )


@bp_user.get('/profile')
@login_required
def profile_get():
    # file = images.get(current_user.avatar).read()
    # with open('application/static/img/file.png', 'wb') as bin_file:
    #     bin_file.write(file)
    # image = url_for('static', filename='img/file.png')
    # return render_template('profile.html', image_file=image)
    return render_template('profile.html', image_file=url_for('static', filename='img/barn.jpg'))


@bp_user.get('/')
@login_required
def profile():
    return render_template('profile_parent_edit.html')
