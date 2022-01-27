from application.dll.repository import game_repository


def add_game(game):
    game_repository.add_game(game)


def get_all_games():
    return game_repository.get_all_games()


def update_high_score(game_id, user_id, score):
    high_score = game_repository.get_high_scores_by_game_id(game_id)
    for i in range(len(high_score)):
        if score > high_score[i]:
            high_score.insert(i, {'user_id': user_id, 'score': score})
            high_score.pop()

    game_repository.update_high_score(high_score)


def get_high_scores_by_game_id(game_id):
    return game_repository.get_high_scores_by_game_id(game_id)


def set_high_score(hs):
    game_repository.set_high_score(hs)
