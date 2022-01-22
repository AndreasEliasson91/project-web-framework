import os

from flask import Blueprint, render_template, redirect, request, url_for, flash
from flask_login import login_required, current_user
from application.bll.controllers.image_controller import get_image
from application.dll.db import images


bp_user = Blueprint('bp_user',
                    __name__,
                    template_folder='templates',
                    url_prefix='/user'
                    )


@bp_user.get('/profile')
@login_required
def profile_get():
    if len(current_user.children) > 0:
        children_pictures = []
        i = 0

        for child in current_user.children:
            children_pictures.append(get_image(child['avatar'], f'child{i}'))
            i += 1

        return render_template('profile.html',
                               profile_picture=get_image(current_user.avatar, 'profile'),
                               children_pictures=children_pictures)
    else:
        return render_template('profile.html',
                               profile_picture=get_image(current_user.avatar, 'profile'))


@bp_user.get('/')
@login_required
def profile():
    return render_template('profile_parent_edit.html')
