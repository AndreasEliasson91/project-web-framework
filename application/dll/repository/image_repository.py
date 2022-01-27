import os

from bson import ObjectId
from flask import url_for
from application.dll.db import images
from application.dll.db.models import Image, User
from application.dll.repository import user_repository


def get_image(_id, filename):
    file = images.get(_id).read()
    with open(f'application/static/img/temp/{filename}.png', 'wb') as bin_file:
        bin_file.write(file)
    return url_for('static', filename=f'img/temp/{filename}.png')


def get_all_image_ids():
    return [image._id for image in Image.all()]


def upload_picture(current_user, file):
    file.save(os.path.join('application/static/img/temp/', 'temp.png'))

    with open('application/static/img/temp/temp.png', 'rb') as in_file:
        contents = in_file.read()

    if Image.find(filename=file.filename).first_or_none() is None:
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

    if not current_user.parent:
        parent = user_repository.get_parent_from_child_id(ObjectId(current_user._id))
        if parent:
            for child in parent.children:
                if child._id == current_user._id:
                    child.avatar = image_id
            user_repository.update_user_information(parent)

    current_user.avatar = image_id
    User.save(current_user)
