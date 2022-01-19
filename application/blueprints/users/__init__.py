from flask import Blueprint, render_template, redirect, request, url_for, flash
from flask_login import login_required, current_user
from application.dll.db.models import Image
from application.dll.db import fs

bp_user = Blueprint('bp_user',
                    __name__,
                    template_folder='templates',
                    url_prefix='/user'
                    )


@bp_user.get('/profile')
@login_required
def profile_get():
    # file = Image.find(_id=current_user.avatar).first_or_none()
    image = url_for('static', filename='img/father3.png')
    return render_template('profile.html', image_file=image)
    # return render_template('profile.html')
