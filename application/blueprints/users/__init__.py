from application.bll.controllers import image_controller, user_controller
from bson import ObjectId
from flask import Blueprint, render_template, redirect, request, url_for
from flask_login import login_required, current_user

bp_user = Blueprint('bp_user',
                    __name__,
                    template_folder='templates',
                    url_prefix='/user'
                    )


@bp_user.get('/friends')
@login_required
def friends_get():
    friends = []
    for friend in user_controller.get_user_friends(current_user):
        friends.append({
            '_id': friend._id,
            'name': friend.display_name if friend.parent else friend.username,
            'image': image_controller.get_profile_picture(friend),
            'colors': friend.settings['rgb_title']
        })

    return render_template('friends.html', friends=friends)


@bp_user.get('/profile/<user_id>')
@login_required
def profile_get(user_id):
    if 'children' in current_user.__dict__:
        children = []

        for child in current_user.children:
            c = user_controller.get_user(_id=child)
            children.append({
                '_id': child,
                'username': c.username,
                'avatar': image_controller.get_profile_picture(c)
            })

        return render_template('profile.html',
                               profile_picture=image_controller.get_profile_picture(current_user),
                               children=children)
    else:
        return render_template('profile.html',
                               profile_picture=image_controller.get_profile_picture(current_user))


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
        image_controller.upload_profile_picture(current_user, file)

    return redirect(url_for('bp_user.profile_get', user_id=current_user._id))


@bp_user.get('/view-profile/<user_id>')
@login_required
def view_profile_get(user_id):
    user = user_controller.get_user(_id=user_id)

    if 'children' in user.__dict__:
        children = []

        for child in user.children:
            c = user_controller.get_user(_id=child)
            children.append({
                '_id': child,
                'username': c.username,
                'avatar': image_controller.get_profile_picture(c)
            })

        return render_template('profile_view.html',
                               user=user,
                               profile_picture=image_controller.get_profile_picture(user),
                               children=children)
    else:
        return render_template('profile_view.html',
                               user=user,
                               profile_picture=image_controller.get_profile_picture(user))


@bp_user.post('/view-profile/<user_id>')
@login_required
def view_profile_post(user_id):
    request.form.get('add-friend')
    current_user.friends.append(ObjectId(user_id))
    current_user.save()
    return redirect(url_for('bp_user.view_profile_get', user_id=user_id))

