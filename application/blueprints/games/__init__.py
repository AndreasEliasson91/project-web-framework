from flask import Blueprint, render_template, redirect, request, url_for

bp_games = Blueprint('bp_games',
                     __name__,
                     template_folder='templates',
                     url_prefix='/games'
                     )


@bp_games.get('/high-scores')
def high_score_get():
    return render_template('high_score.html')
