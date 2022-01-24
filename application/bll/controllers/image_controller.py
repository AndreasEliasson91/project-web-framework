from application.dll.repository import image_repository


def get_image(_id, filename):
    return image_repository.get_image(_id, filename)


def get_all_image_is():
    return image_repository.get_all_image_ids()


def upload_image(current_user, file):
    return image_repository.upload_picture(current_user, file)
