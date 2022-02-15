from application.dll.repository import game_repository, user_repository


def add_game_information(name, description):
    game = {
        'name': name,
        'level': 0,
        'description': description,
        'content': {
            'main_image': None,
            'images': []
        },
        'high_score': []
    }

    game_repository.add_game_information(game)


def get_game(game_id):
    for game in get_all_games():
        if game._id == game_id:
            return game


def get_all_games():
    return game_repository.get_all_games()


def get_high_score(game_id):
    return [score for game in get_all_games() if game._id == game_id for score in game.high_score]


def set_high_score(game_id, user, score):
    game = get_game(game_id)
    high_score = get_high_score(game_id)

    for phs in user.personal_high_score:
        if phs['game'] == game_id:
            if phs['score'] < score:
                phs['score'] = score
                break

    for hs in high_score:
        if hs['score'] < score:
            game.high_score.append({
                'user_id': user._id,
                'score': score
            })
            game.high_score = sorted(game.high_score, key=lambda x: x['score'], reverse=True)
            if len(game.high_score) > 5:
                game.high_score.pop()
            break

    user_repository.update_user_information(user)
    game_repository.update_game(game)


def game_sentances():
    return game_repository.game_sentances()
