from flask import Blueprint, render_template, redirect, request, url_for, flash
from flask_login import login_required, current_user
from application.bll.controllers.image_controller import get_image, upload_image

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


@bp_user.get('/friends')
@login_required
def friends_get():
    return render_template('friends.html')


@bp_user.get('/profile')
@login_required
def profile_get():
    if 'children' in current_user.__dict__:
        children = []
        i = 0

        for child in current_user.children:
            children.append({
                'username': child['username'],
                'avatar': get_image(child['avatar'], f'child{i}')
            })
            i += 1

        return render_template('profile.html',
                               profile_picture=get_image(current_user.avatar, 'profile'),
                               children=children)
    else:
        return render_template('profile.html',
                               profile_picture=get_image(current_user.avatar, 'profile'))


@bp_user.post('/profile')
@login_required
def profile_post():
    rgb = [request.form.get('red'), request.form.get('green'), request.form.get('blue')]
    if rgb[0]:
        if request.form.get('title'):
            for i in range(len(current_user.settings['rgb_title'])):
                current_user.settings['rgb_title'][i] = int(rgb[i])
        else:
            for i in range(len(current_user.settings['rgb_subtitle'])):
                current_user.settings['rgb_subtitle'][i] = int(rgb[i])

        current_user.save()

    file = request.files.get('profile_picture')
    if file:
        upload_image(current_user, file)

    return redirect(url_for('bp_user.profile_get'))


