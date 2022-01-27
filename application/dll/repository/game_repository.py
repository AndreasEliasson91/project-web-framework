from application.dll.db.models import Game, HighScore


def add_game(game):
    Game(game).save()


def get_all_games():
    return Game.all()


def get_high_scores_by_game_id(game_id):
    return HighScore.find(game_id=game_id)


def update_high_score(high_score):
    HighScore.save(high_score)


def set_high_score(hs):
    HighScore(hs).save()
