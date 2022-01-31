from application.dll.repository import image_repository


def get_all_image_ids():
    return image_repository.get_all_image_ids()


def get_profile_picture(user):
    return image_repository.get_profile_picture(user)


def upload_profile_picture(user, file):
    return image_repository.upload_profile_picture(user, file)


def get_game_image(game, suffix):
    return image_repository.get_game_image(game, suffix)
