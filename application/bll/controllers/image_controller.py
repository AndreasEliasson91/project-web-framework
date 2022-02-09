import os

from application.dll.repository import image_repository
from flask import url_for


def get_all_image_ids():
    return image_repository.get_all_image_ids()


def get_profile_picture(user):
    file = image_repository.get_profile_picture(user)
    with open(f'application/static/img-profile/{str(user._id)}.png', 'wb') as bin_file:
        bin_file.write(file)
    return url_for('static', filename=f'img-profile/{str(user._id)}.png')


def get_game_image(game, suffix):
    file = image_repository.get_game_image(game)
    with open(f'application/static/img-game/{str(game._id)}{suffix}.png', 'wb') as bin_file:
        bin_file.write(file)
    return url_for('static', filename=f'img-game/{str(game._id)}{suffix}.png')


def upload_profile_picture(user, file):
    file.save(os.path.join('application/static/img-profile/', f'{str(user._id)}.png'))

    with open(f'application/static/img-profile/{str(user._id)}.png', 'rb') as in_file:
        content = in_file.read()

    image_repository.upload_profile_picture(user, content)


def upload_game_image(game, suffix, file):
    file.save(os.path.join('application/static/img-game/', f'{str(game._id)}{suffix}.png'))

    with open(f'application/static/img-game/{str(game._id)}{suffix}.png', 'rb') as in_file:
        content = in_file.read()

    image_repository.upload_game_image(game, suffix, content)
