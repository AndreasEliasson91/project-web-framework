from application.dll.db.models import Game


def add_game(game):
    Game(game).save()


def get_all_games():
    return [game for game in Game.all()]


def update_game(game):
    Game.save(game)
