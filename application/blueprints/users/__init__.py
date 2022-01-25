import os

from flask import Blueprint, render_template, redirect, request, url_for, flash
from flask_login import login_required, current_user
from application.bll.controllers.image_controller import get_image, upload_image
from application.dll.db import images
from application.dll.db.models import Image, User

bp_user = Blueprint('bp_user',
                    __name__,
                    template_folder='templates',
                     url_prefix='/user'
                    )

              
@bp_user.get('/welcome')
@login_required
def user_index():
    return render_template('welcome.html')


@bp_user.get('/settings')
@login_required
def settings_get():
    return render_template('settings.html')


@bp_user.get('/contacts')
@login_required
def contacts_get():
    return render_template('contacts.html')


@bp_user.get('/friends')
@login_required
def friends_get():
    return render_template('friends.html')


@bp_user.get('/profile')
@login_required
def profile_get():
    # if 'children' in current_user.__dict__:
    #     children = []
    #     i = 0
    #
    #     for child in current_user.children:
    #         children.append({
    #             'username': child['username'],
    #             'avatar': get_image(child['avatar'], f'child{i}')
    #         })
    #         i += 1
    #
    #     return render_template('profile.html',
    #                            profile_picture=get_image(current_user.avatar, 'profile'),
    #                            children=children)
    # else:
    #     return render_template('profile.html',
    #                            profile_picture=get_image(current_user.avatar, 'profile'))

    return render_template('profile.html')

@bp_user.post('/profile')
@login_required
def profile_post():
    file = request.files.get('profile_picture')
    upload_image(current_user, file)
    return redirect(url_for('bp_user.profile_get'))


