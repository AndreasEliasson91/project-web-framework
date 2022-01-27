from bson import ObjectId
from flask import Blueprint, render_template, redirect, request, url_for, flash
from flask_login import login_required, current_user
from application.bll.controllers.image_controller import get_image, upload_image
from application.bll.controllers.user_controller import get_user_by_user_id, get_user_by_username

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


@bp_user.get('/profile/<user_id>')
@login_required
def profile_get(user_id):
    if 'children' in current_user.__dict__:
        children = []
        i = 0

        for child in current_user.children:
            c = get_user_by_user_id(child)
            children.append({
                '_id': child,
                'username': c.username,
                'avatar': get_image(c.avatar, f'child{i}')
            })
            i += 1

        return render_template('profile.html',
                               profile_picture=get_image(current_user.avatar, 'profile'),
                               children=children)
    else:
        return render_template('profile.html',
                               profile_picture=get_image(current_user.avatar, 'profile'))


@bp_user.post('/profile/<user_id>')
@login_required
def profile_post(user_id):
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

    return redirect(url_for('bp_user.profile_get', user_id=current_user._id))


@bp_user.get('/view-profile/<user_id>')
@login_required
def view_profile_get(user_id):
    user = get_user_by_user_id(user_id)

    if 'children' in user.__dict__:
        children = []
        i = 0

        for child in user.children:
            c = get_user_by_user_id(child)
            children.append({
                '_id': child,
                'username': c.username,
                'avatar': get_image(c.avatar, f'child{i}')
            })
            i += 1

        return render_template('profile_view.html',
                               user=user,
                               profile_picture=get_image(user.avatar, 'profile'),
                               children=children)
    else:
        return render_template('profile_view.html',
                               user=user,
                               profile_picture=get_image(user.avatar, 'profile'))
