from flask import Blueprint, render_template
from application.bll.controllers import game_controller, user_controller, image_controller
from application.dll.db import images

bp_games = Blueprint('bp_games',
                     __name__,
                     template_folder='templates',
                     url_prefix='/games'
                     )


@bp_games.get('/')
def index_hs():
    games = game_controller.get_all_games()
    users = user_controller.get_all_users()
    for game in games:
        game.content['main_image'] = image_controller.get_game_image(game, '_main')
        for i, score in enumerate(game.high_score):
            for user in users:
                if score['user_id'] == user._id:
                    score['user_id'] = user.get_id()
                    score['avatar'] = image_controller.get_profile_picture(user)
    #
    # file = f'C:/Users/andre/OneDrive/Skrivbord/61f2b9927b8b30662bb44ada_main.png'
    #
    # with open(file, 'rb') as f:
    #     contents = f.read()
    #
    # images.put(contents, filename=f'61f2b9927b8b30662bb44ada_main.png')

    return render_template('games_index_hs.html', games=games)
