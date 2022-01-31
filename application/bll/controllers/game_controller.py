from application.dll.repository import game_repository


def add_game(game):
    game_repository.add_game(game)


def get_all_games():
    return game_repository.get_all_games()


def update_game(game):
    game_repository.update_game(game)
