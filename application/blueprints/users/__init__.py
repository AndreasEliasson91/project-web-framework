from flask import Blueprint, render_template

bp_user = Blueprint('bp_user',
                    __name__,
                    template_folder='templates',
                    )


@bp_user.get('/welcome')
def user_index():
    return render_template('welcome.html')


@bp_user.get('/profil')
def profil_get():
    return render_template('profil.html')


@bp_user.get('/settings')
def settings_get():
    return render_template('settings.html')


@bp_user.get('/contacts')
def contacts_get():
    return render_template('contacts.html')
