import random

from bson import ObjectId
from flask import Blueprint, render_template, redirect, request, url_for

from application.bll.controllers import game_controller
from application.bll.controllers.user_controller import get_all_users

bp_games = Blueprint('bp_games',
                     __name__,
                     template_folder='templates',
                     url_prefix='/games'
                     )


@bp_games.get('/')
def index_hs():
    hs = []
    for game in game_controller.get_all_games():
        hs.append(game_controller.get_high_scores_by_game_id(ObjectId(game._id)))
    return render_template('games_index_hs.html', games=game_controller.get_all_games(), hs=hs)
