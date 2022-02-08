from flask import Blueprint, render_template, redirect, url_for, request
from application.bll.controllers import game_controller, user_controller, image_controller

maze = None
maze_position_x = None
maze_position_y = None

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

    return render_template('games_index.html', games=games)


# @bp_games.post('/')
# def index_post():
#     return redirect(url_for('bp_game.difficulty_get'))


@bp_games.get('/math-maze/set-difficulty')
def difficulty_get():
    return render_template('math_maze_difficulty.html')


@bp_games.post('/math-maze/set-difficulty')
def difficulty_post():
    global maze, maze_position_x, maze_position_y

    from application.bll.math_maze import Maze
    from random import randrange

    maze_size = request.form.get('size')
    difficulty = request.form.get('difficulty')
    operators = request.form.getlist('operators[]')

    # Create a Maze
    maze = Maze(int(maze_size), int(maze_size), int(difficulty), operators, 'application/static/img-game/maze.svg')

    #  Set starting point
    maze_position_x, maze_position_y = randrange(0, (int(maze_size) - 1)), randrange(0, (int(maze_size) - 1))

    return redirect(url_for('bp_games.maze_get'))


@bp_games.get('/math-maze')
def maze_get():
    global maze, maze_position_x, maze_position_y

    return render_template('math_maze.html', current_location=maze.get_cell(*(maze_position_x, maze_position_y)))


@bp_games.post('/math-maze')
def maze_post():
    global maze, maze_position_x, maze_position_y

    direction = request.form.get('direction')
    if not maze.get_cell(*(maze_position_x, maze_position_y)).walls[direction]:

        match direction:
            case 'north':
                maze_position_y -= 1
            case 'south':
                maze_position_y += 1
            case 'west':
                maze_position_x -= 1
            case 'east':
                maze_position_x += 1

    return redirect(url_for('bp_games.maze_get', current_location=maze.get_cell(*(maze_position_x, maze_position_y))))
