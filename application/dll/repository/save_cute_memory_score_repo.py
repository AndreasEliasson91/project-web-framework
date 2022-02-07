from flask_login import current_user


def save_cute_memory_score(get_score):
    player_score = (int(get_score))
    cur_user = current_user.score

    # Make check if the new score is higher than the last saved score.
    if player_score > cur_user:
        current_user.score = player_score
        current_user.save()
    return True
