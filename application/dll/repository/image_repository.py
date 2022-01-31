import os

from bson import ObjectId
from flask import url_for
from application.dll.db import images
from application.dll.db.models import Image, User, Game
from application.dll.repository import user_repository


def get_all_image_ids():
    return [image._id for image in Image.all()]


def get_profile_picture(user):
    file = images.get(user.avatar).read()
    with open(f'application/static/img-profile/{str(user._id)}.png', 'wb') as bin_file:
        bin_file.write(file)
    return url_for('static', filename=f'img-profile/{str(user._id)}.png')


def upload_profile_picture(user, file):
    file.save(os.path.join('application/static/img-profile/', f'{str(user._id)}.png'))

    with open(f'application/static/img-profile/{str(user._id)}.png', 'rb') as in_file:
        contents = in_file.read()

    for image in Image.all():
        if image.filename == f'{str(user._id)}.png':
            images.delete(image._id)
            break

    images.put(contents, filename=f'{str(user._id)}.png')
    image_id = Image.find(filename=f'{str(user._id)}.png').first_or_none()._id

    if not user.parent:
        parent = user_repository.get_parent_from_child_id(ObjectId(user._id))
        if parent:
            for child in parent.children:
                if child._id == user._id:
                    child.avatar = image_id
            user_repository.update_user_information(parent)

    user.avatar = image_id
    User.save(user)


def get_game_image(game, suffix):
    file = images.get(game.content['main_image']).read()
    with open(f'application/static/img-game/{str(game._id)}{suffix}.png', 'wb') as bin_file:
        bin_file.write(file)
    return url_for('static', filename=f'img-game/{str(game._id)}{suffix}.png')


# def upload_game_image(game, suffix, file):
#     file.save(os.path.join('application/static/img-game/', f'{str(game._id)}{suffix}.png'))
#
#     with open(f'application/static/img-game/{str(game._id)}{suffix}.png', 'rb') as in_file:
#         contents = in_file.read()
#
#     for image in Image.all():
#         if image.filename == f'{str(game._id)}{suffix}.png':
#             images.delete(image._id)
#             break
#
#     images.put(contents, filename=f'{str(game._id)}{suffix}.png')
#     image_id = Image.find(filename=f'{str(game._id)}{suffix}.png').first_or_none()._id
#
#     if 'main' in suffix:
#         game.content['main_image'] = image_id
#
#     Game.save(game)
