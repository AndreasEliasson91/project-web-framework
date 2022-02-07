from flask import Blueprint, render_template, request


from application.bll.controllers import game_controller, user_controller, image_controller
from application.bll.controllers.save_cute_memory_score import save_cute_memory_score

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


@bp_games.get('/memory-game')
def index_memory():
    return render_template('index_memory.html')


@bp_games.post('/memory-game')
def save_score_post():
    # username = request.form.get('username').lower()
    get_score = request.form.get('t1')
    save_cute_memory_score(get_score)
    return render_template('index_memory.html')
