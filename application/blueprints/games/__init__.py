import time
import random
from bson import ObjectId

from application.bll.controllers import game_controller, image_controller
from application.bll.controllers.save_cute_memory_score import save_cute_memory_score
from flask import Blueprint, render_template, redirect, url_for, request

maze = None
position_x = None
position_y = None
i = 0
points = 0


bp_games = Blueprint('bp_games',
                     __name__,
                     template_folder='templates',
                     url_prefix='/games'
                     )




@bp_games.get('/')
def index():
    from application.bll.controllers import user_controller

    games = game_controller.get_all_games()
    users = user_controller.get_all_users()

    for game in games:
        game.content['main_image'] = image_controller.get_game_image(game, '_main')
        for score in game.high_score:
            for user in users:
                if score['user_id'] == user._id:
                    score['user_id'] = user._id
                    score['name'] = user.display_name if user.parent else user.username
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

    return render_template('games_index.html', games=games)


@bp_games.get('/description/<game_id>')
def game_description_get(game_id):
    game = game_controller.get_game(ObjectId(game_id))
    game.content['main_image'] = image_controller.get_game_image(game, '_main')

    return render_template('game_description.html', game=game)


@bp_games.post('/description/<game_id>')
def game_description_post(game_id):
    game = game_controller.get_game(ObjectId(game_id))
    match game.name.lower():
        case 'hitta ordet!':
            return redirect(url_for('bp_games.find_the_word_game'))
        case 'cute memory':
            return redirect(url_for('bp_games.index_memory'))
        case 'a-maze-ing game':
            return redirect(url_for('bp_games.difficulty_get'))
        # case 'ordgåtan':
            # return redirect(url_for('bp_games.word_game or something'))


@bp_games.get('/hitta-ordet')
def find_the_word_game():
    return render_template('find_the_word_game.html')


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

