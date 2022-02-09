import random

from flask import Blueprint, render_template, url_for, redirect, request, flash
from application.bll.controllers import game_controller, user_controller, image_controller
from application.blueprints.open import bp_open

i = 0


bp_games = Blueprint('bp_games',
                     __name__,
                     template_folder='templates',
                     url_prefix='/games'
                     )




@bp_games.get('/')
def index():
    games = game_controller.get_all_games()
    users = user_controller.get_all_users()

    for game in games:
        game.content['main_image'] = image_controller.get_game_image(game, '_main')
        for score in game.high_score:
            for user in users:
                if score['user_id'] == user._id:
                    score['user_id'] = user.display_name if user.parent else user.username
                    score['avatar'] = image_controller.get_profile_picture(user)

    return render_template('games_index_hs.html', games=games)



@bp_games.get('/reading_swedish')
def read_swe_get():
    global i
    cards = game_controller.game_sentances()
    while i < len(cards):
        return render_template('reading_game_swe.html', card=cards[i])
    else:
        return redirect(url_for("bp_open.index"))


@bp_games.post('/reading_swedish')
def read_swe_post():
    global i
    if request.form.get('option') == 'right':
        # ('Det var rätt! bra jobbat')
        i += 1
        return redirect(url_for("bp_games.read_swe_get"))
    else:
        return redirect(url_for("bp_games.read_swe_get"))
