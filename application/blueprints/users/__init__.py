from flask import Blueprint, render_template, redirect, request, url_for, flash
from flask_login import login_required

bp_user = Blueprint('bp_user',
                    __name__,
                    template_folder='templates',
                    url_prefix='/user'
                    )


@bp_user.get('/profile')
@login_required
def profile_get():
    return render_template('profile.html')
