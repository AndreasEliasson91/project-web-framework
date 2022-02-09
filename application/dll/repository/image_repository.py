from application.dll.db import images
from application.dll.db.models import Image
from bson import ObjectId


def get_all_image_ids():
    return [image._id for image in Image.all()]


def get_profile_picture(user):
    return images.get(user.avatar).read()


def get_game_image(game):
    return images.get(game.content['main_image']).read()


def upload_profile_picture(user, content):
    from application.dll.repository import user_repository

    for image in Image.all():
        if image.filename == f'{str(user._id)}.png':
            images.delete(image._id)
            break

    images.put(content, filename=f'{str(user._id)}.png')
    image_id = Image.find(filename=f'{str(user._id)}.png').first_or_none()._id

    if not user.parent:
        parent = user_repository.get_parent_from_child_id(ObjectId(user._id))
        if parent:
            for child in parent.children:
                if child._id == user._id:
                    child.avatar = image_id
            user_repository.update_user_information(parent)

    user.avatar = image_id
    user_repository.update_user_information(user)


def upload_game_image(game, suffix, content):
    from application.dll.repository import game_repository

    for image in Image.all():
        if image.filename == f'{str(game._id)}{suffix}.png':
            images.delete(image._id)
            break

    images.put(content, filename=f'{str(game._id)}{suffix}.png')
    image_id = Image.find(filename=f'{str(game._id)}{suffix}.png').first_or_none()._id

    if 'main' in suffix:
        game.content['main_image'] = image_id

    game_repository.update_game(game)
