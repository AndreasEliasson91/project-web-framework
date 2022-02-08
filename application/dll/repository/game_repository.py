from application.dll.db.models import Game


def add_game(game):
    Game(game).save()


def get_all_games():
    return [game for game in Game.all()]


def update_game(game):
    Game.save(game)


def game_sentances():
    cards =  [
        {
            'text': 'this is the best text',
            'wanswer': 'best',
            'ranswer': 'not best'
        },
         {
            'text': 'this is not the best text',
            'wanswer': 'True',
            'ranswer': 'Not true'
        }

    ]

    return cards


