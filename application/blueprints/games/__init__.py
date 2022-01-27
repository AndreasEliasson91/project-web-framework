from flask import Blueprint, render_template, redirect, request, url_for

bp_games = Blueprint('bp_games',
                     __name__,
                     template_folder='templates',
                     url_prefix='/games'
                     )


@bp_games.get('/')
def index_hs():
    return render_template('games_index_hs.html')
