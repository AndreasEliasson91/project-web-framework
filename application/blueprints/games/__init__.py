import time
import random
from bson import ObjectId

from application.bll.controllers import game_controller, image_controller
from application.bll.controllers.save_cute_memory_score import save_cute_memory_score
from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import current_user, login_required

current_game = None
win_condition = None

maze = None
timer = None
position_x = 0
position_y = 0

i = 0
points = 0
start = time.time()

bp_games = Blueprint('bp_games',
                     __name__,
                     template_folder='templates',
                     url_prefix='/games'
                     )


@bp_games.get('/')
def index():
    from application.bll.controllers import user_controller

    if current_user.is_authenticated:
        games = game_controller.get_all_games()
    else:
        games = [game for game in game_controller.get_all_games() if
                 game.name.lower() == 'cute memory' or game.name.lower() == 'hitta ordet!']
    users = user_controller.get_all_users()

    for game in games:
        game.content['main_image'] = image_controller.get_game_image(game, '_main')
        for score in game.high_score:
            for user in users:
                if score['user_id'] == user._id:
                    score['name'] = user.display_name if user.parent else user.username
                    score['avatar'] = image_controller.get_profile_picture(user)

    return render_template('games_index.html', games=games)


@login_required
@bp_games.get('/card_game')
def card_game_get():
    global i
    global points
    global current_game
    global start
    cards = game_controller.game_sentances()
    while i < len(cards):
        answers = cards[i]['answers']
        random.shuffle(answers)
        return render_template('reading_game_swe.html', card=cards[i], points=points, answers=answers)
    else:
        end = time.time()
        total_score = points * 10 - int(end - start)
        game_controller.set_high_score(current_game, current_user, total_score)
        i = 0
        points = 0
        start = time.time()
        return render_template('reading_game_swe_complete.html', points=int(total_score))


@login_required
@bp_games.post('/card_game')
def card_game_post():
    global i, points

    if request.form.get('option') == 'right':
        flash('Det var rätt, du fick ett poäng!')
        i += 1
        points += 1
    else:
        points -= 1
        flash('Det var inte rätt, försök igen!')

    return redirect(url_for('bp_games.card_game_get'))


@bp_games.get('/description/<game_id>')
def game_description_get(game_id):
    game = game_controller.get_game(ObjectId(game_id))
    game.content['main_image'] = image_controller.get_game_image(game, '_main')

    return render_template('game_description.html', game=game)


@bp_games.post('/description/<game_id>')
def game_description_post(game_id):
    global current_game

    game = game_controller.get_game(ObjectId(game_id))
    current_game = ObjectId(game_id)

    match game.name.lower():
        case 'hitta ordet!':
            return redirect(url_for('bp_games.find_the_word_game'))
        case 'cute memory':
            return redirect(url_for('bp_games.index_memory'))
        case 'a-maze-ing game':
            return redirect(url_for('bp_games.difficulty_get'))
        case 'ordgåtan':
            return redirect(url_for('bp_games.card_game_get'))


@bp_games.get('/hitta-ordet')
def find_the_word_game():
    return render_template('find_the_word_game.html')


@bp_games.get('/memory-game')
def index_memory():
    return render_template('index_memory.html')


@bp_games.post('/memory-game')
def save_score_post():
    get_score = request.form.get('t1')
    save_cute_memory_score(get_score)
    time.sleep(5)
    return render_template('index_memory.html')


@bp_games.get('/math-maze/set-difficulty')
@login_required
def difficulty_get():
    return render_template('math_maze_difficulty.html')


@bp_games.post('/math-maze/set-difficulty')
@login_required
def difficulty_post():
    global maze, position_x, position_y, win_condition, timer, points

    from application.bll.math_maze import Maze

    maze_size = int(request.form.get('size'))
    difficulty = request.form.get('difficulty')
    operators = request.form.getlist('operators[]')

    maze = Maze(maze_size, maze_size, int(difficulty), operators, 'application/static/img-game/maze.svg')
    position_x, position_y = (0, 0)
    win_condition = ((maze_size - 1), (maze_size - 1))
    points = 0
    timer = 120000

    return redirect(url_for('bp_games.maze_get'))


@bp_games.get('/math-maze')
@login_required
def maze_get():
    global position_x, position_y, timer, points
    return render_template('math_maze.html',
                           current_location=maze.get_cell(*(position_x, position_y)),
                           time_remaining=timer,
                           points=points)


@bp_games.post('/math-maze')
@login_required
def maze_post():
    global maze, position_x, position_y, timer, points, current_game, win_condition

    from application.bll.math_maze import move

    direction = request.form.get('direction')
    timer = request.form.get('timer')

    if not maze.get_cell(*(position_x, position_y)).walls[direction]:
        position_x, position_y = move(direction, position_x, position_y)
        points += 1
        if (position_x, position_y) == win_condition:
            score = len(timer) * points
            game_controller.set_high_score(current_game, current_user, score)
            flash(f'Grattis!\nDu fick {score} poäng!')
            return redirect(url_for('bp_games.game_description_get', game_id=current_game))
        else:
            flash('Rätt! Du går vidare!')

    else:
        flash('Fel! Försök igen!')
        if points > 0:
            points -= 1

    return redirect(url_for('bp_games.maze_get'))
