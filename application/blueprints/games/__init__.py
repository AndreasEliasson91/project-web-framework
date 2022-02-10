
import time

from application.bll.controllers import game_controller, user_controller, image_controller
from application.bll.controllers.save_cute_memory_score import save_cute_memory_score

from flask import Blueprint, render_template, redirect, url_for, request

maze = None
position_x = None
position_y = None

bp_games = Blueprint('bp_games',
                     __name__,
                     template_folder='templates',
                     url_prefix='/games'
                     )


@bp_games.get('/')
def index():
    from application.bll.controllers import game_controller, user_controller, image_controller

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
    time.sleep(5)
    return render_template('index_memory.html')

  


# @bp_games.post('/')
# def index_post():
#     return redirect(url_for('bp_game.difficulty_get'))


@bp_games.get('/math-maze/set-difficulty')
def difficulty_get():
    return render_template('math_maze_difficulty.html')


@bp_games.post('/math-maze/set-difficulty')
def difficulty_post():
    global maze, position_x, position_y

    from application.bll.math_maze import Maze
    from random import randrange

    maze_size = request.form.get('size')
    difficulty = request.form.get('difficulty')
    operators = request.form.getlist('operators[]')

    # Create a Maze
    maze = Maze(int(maze_size), int(maze_size), int(difficulty), operators, 'application/static/img-game/maze.svg')

    #  Set starting point
    position_x, position_y = randrange(0, (int(maze_size) - 1)), randrange(0, (int(maze_size) - 1))

    return redirect(url_for('bp_games.maze_get'))


@bp_games.get('/math-maze')
def maze_get():
    global maze, position_x, position_y

    return render_template('math_maze.html', current_location=maze.get_cell(*(position_x, position_y)))


@bp_games.post('/math-maze')
def maze_post():
    global maze, position_x, position_y

    from application.bll.math_maze import move

    direction = request.form.get('direction')
    if not maze.get_cell(*(position_x, position_y)).walls[direction]:
        position_x, position_y = move(direction, position_x, position_y)

    return redirect(url_for('bp_games.maze_get', current_location=maze.get_cell(*(position_x, position_y))))

