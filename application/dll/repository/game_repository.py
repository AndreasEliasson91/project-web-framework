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
            'text': 'Kalle har en grön boll som han brukar leka med på gården',
            'question': 'Vart brukar kalle leka?',
            'answer': 'På gården',
            'answer1': 'Hemma',
            'answer2': 'Hos grannen'
        },
         {
            'text': 'this is not the best text',
            'answer': 'True',
            'answer1': 'best',
            'answer2': 'Not true'
        }

    ]

    return cards


