from flask import Blueprint, render_template, redirect, request, url_for, flash
from flask_login import login_required

bp_user = Blueprint('bp_user',
                    __name__,
                    template_folder='templates',
                     url_prefix='/user'
                    )

              
@bp_user.get('/welcome')
@login_required
def user_index():
    return render_template('welcome.html')


@bp_user.get('/profile')
@login_required
def profil_get():
    return render_template('profil.html')


@bp_user.get('/settings')
@login_required
def settings_get():
    return render_template('settings.html')


@bp_user.get('/contacts')
@login_required
def contacts_get():
    return render_template('contacts.html')
 

