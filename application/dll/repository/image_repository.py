from flask import url_for
from application.dll.db import images
from application.dll.db.models import Image


def get_image(_id, filename):
    file = images.get(_id).read()
    with open(f'application/static/img/temp/{filename}.png', 'wb') as bin_file:
        bin_file.write(file)
    return url_for('static', filename=f'img/temp/{filename}.png')


def get_all_image_ids():
    return [image._id for image in Image.all()]
