from flask_login import current_user

from application.dll.db.models import User


def save_cute_memory_score(get_score):
    # Först kolla om fälten game och score existerarer

    # beroende på om de finns eller ej, skall olika saker göras.

    # 1 om det inte finns, gå direkt till skapa (skriv till databasen)

    # 2 om det existerar, kontrollera tidigare score, mot det nya.

    # 3 om det nya scoret är högre än det gamla skriv till databas annars
    # spara inte.

    user1 = User.find(email=current_user.email).first_or_none()

    player_score = (int(get_score))
    placeholder2 = str(user1)

    if "game" not in placeholder2:
        user1.game = {'game name': "Cute memory game", 'SCORE': player_score}
        user1.save()

    else:

        placeholder = user1.game.get('SCORE')

        if player_score > placeholder:
            user1.game = {'game name': "Cute memory game", 'SCORE': player_score}
            user1.save()

        else:
            pass

    return True
