from application.dll.repository import game_repository


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
    return [score for game in get_all_games() if game._id == game_id for score in game['high_score']]


def set_high_score(game_id, user):
    game = get_game(game_id)
    high_score = [score for game in get_all_games() if game._id == game_id for score in game['high_score']]

    for score in high_score:
        if score < user['score']:
            high_score.append(user['score'])
            break

    high_score = sorted(high_score, key=lambda x: x['score'])
    high_score.pop()

    game_repository.update_game(game)
