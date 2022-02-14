import random
import time

from flask import Blueprint, render_template, url_for, redirect, request, flash
from flask_login import login_required

from application.bll.controllers import game_controller, user_controller, image_controller
from application.blueprints.open import bp_open

i = 0
points = 0

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


@login_required
@bp_games.get('/reading_swedish')
def read_swe_get():
    global i
    global points

    cards = game_controller.game_sentances()
    while i < len(cards):
        answers = cards[i]['answers']
        random.shuffle(answers)
        return render_template('reading_game_swe.html', card=cards[i], points=points, answers=answers)
    else:
        time.sleep(5)
        return render_template('reading_game_swe_complete.html', points=points)

@login_required
@bp_games.post('/reading_swedish')
def read_swe_post():
    global i
    global points
    if request.form.get('option') == 'right':
        flash('Det var rätt, du fick ett poäng!')
        i += 1
        points += 1
        return redirect(url_for("bp_games.read_swe_get"))
    else:
        points -= 1
        flash('Det var inte rätt, försök igen!')
        return redirect(url_for('bp_games.read_swe_get'))

