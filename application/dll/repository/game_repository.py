from application.dll.db.models import Game


def add_game_information(game):
    Game(game).save()


def get_all_games():
    return [game for game in Game.all()]


def update_game(game):
    Game.save(game)


def game_sentances():
    cards = [
        {
            'text': 'Kalle har en grön boll som han brukar leka med på gården',
            'question': 'Vart brukar kalle leka?',
            'answers': [{'alternative': 'På gården',
                         'correct': True},
                        {'alternative': 'Hemma',
                         'correct': False},
                        {'alternative': 'Hos grannen',
                         'correct': False}],

        },
        {
            'text': 'Kalle har en grön boll som han brukar leka med på gården',
            'question': 'Vilken färg har kalles boll?',
            'answers': [{'alternative': 'Grön',
                         'correct': True},
                        {'alternative': 'Blå',
                         'correct': False},
                        {'alternative': 'Grå',
                         'correct': False}],
        },

        {
            'text': 'Kalle har en grön boll som han brukar leka med på gården',
            'question': 'Vad brukar kalle göra?',
            'answers': [{'alternative': 'Leka',
                         'correct': True},
                        {'alternative': 'Spela',
                         'correct': False},
                        {'alternative': 'Äta',
                         'correct': False}],

        },
        {
            'text': 'Frida har en kanin som gillar att äta gräs',
            'question': 'Vad gillar fridas kanin att äta?',
            'answers': [{'alternative': 'Gräs',
                         'correct': True},
                        {'alternative': 'Gröt',
                         'correct': False},
                        {'alternative': 'Gryn',
                         'correct': False}],
        },
        {
            'text': 'Frida har en kanin som gillar att äta gräs',
            'question': 'Vilket husdjur har Frida?',
            'answers': [{'alternative': 'En kanin',
                         'correct': True},
                        {'alternative': 'En hund',
                         'correct': False},
                        {'alternative': 'En katt',
                         'correct': False}],
        },
        {
            'text': 'Erik är vän med Frida men Erik har en katt',
            'question': 'Vad har erik för husdjur?',
            'answers': [{'alternative': 'Katt',
                         'correct': True},
                        {'alternative': 'Hund',
                         'correct': False},
                        {'alternative': 'Kanin',
                         'correct': False}],
        },
        {
            'text': 'Erik är vän med Frida men Erik har en katt',
            'question': 'Vem är Erik vän med?',
            'answers': [{'alternative': 'Frida',
                         'correct': True},
                        {'alternative': 'Kalle',
                         'correct': False},
                        {'alternative': 'Fridolf',
                         'correct': False}],
        },
        {
            'text': 'Lenny har två döttrar som gillar att spela spel',
            'question': 'Vad gillar lennys döttrar att göra?',
            'answers': [{'alternative': 'Spela spel',
                         'correct': True},
                        {'alternative': 'Leka',
                         'correct': False},
                        {'alternative': 'Äta mat',
                         'correct': False}],

        },
        {
            'text': 'Lenny har två döttrar som gillar att spela spel',
            'question': 'Vad har Lenny?',
            'answers': [{'alternative': 'Två döttrar',
                         'correct': True},
                        {'alternative': 'Två söner',
                         'correct': False},
                        {'alternative': 'Två fruar',
                         'correct': False}],
        },
        {
            'text': 'Andreas har en hund som heter Elvis',
            'question': 'Vad heter Andreas hund?',
            'answers': [{'alternative': 'Elvis',
                         'correct': True},
                        {'alternative': 'Erik',
                         'correct': False},
                        {'alternative': 'Lufsen',
                         'correct': False}],
        },
        {
            'text': 'Anna gillar att skriva på sin dator',
            'question': 'Vad gillar Anna att skriva på?',
            'answers': [{'alternative': 'Sin dator',
                         'correct': True},
                        {'alternative': 'En skrivare',
                         'correct': False},
                        {'alternative': 'Ett papper',
                         'correct': False}],
        }
    ]

    return cards
