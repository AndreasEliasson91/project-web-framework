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

#
# @bp_user.get('/profile')
# @login_required
# def profil_get():
#     return render_template('profil.html')


@bp_user.get('/settings')
@login_required
def settings_get():
    return render_template('settings.html')


@bp_user.get('/contacts')
@login_required
def contacts_get():
    return render_template('contacts.html')


@bp_user.get('/profile')
@login_required
def profile_get():
    # if 'children' in current_user.__dict__:
    #     children_pictures = []
    #     i = 0
    #
    #     for child in current_user.children:
    #         children_pictures.append(get_image(child['avatar'], f'child{i}'))
    #         i += 1
    #
    #     return render_template('profile.html',
    #                            profile_picture=get_image(current_user.avatar, 'profile'),
    #                            children_pictures=children_pictures)
    # else:
    return render_template('profile.html')
    #           profile_picture=get_image(current_user.avatar, 'profile'))


@bp_user.post('/profile')
@login_required
def profile_post():
    file = request.files.get('profile_picture')
    file.save(os.path.join('application/static/img/temp/', 'temp.png'))

    with open('application/static/img/temp/temp.png', 'rb') as in_file:
        contents = in_file.read()

    if Image.find(filename=file.filename).first_or_none() == None:
        images.put(contents, filename=file.filename)
    else:
        i = 0
        name = file.filename
        for img in Image.all():
            if img.filename == name:
                i += 1
                name = f'LBG{i}_{file.filename}'

        images.put(contents, filename=f'{i}_{file.filename}')

    image_id = Image.find(filename=file.filename).first_or_none()._id

    current_user.avatar = image_id
    User.save(current_user)

    return redirect(url_for('bp_user.profile_get'))
