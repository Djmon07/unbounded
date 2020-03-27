from flask import Flask, flash, Blueprint, g, redirect, render_template, request, session, url_for

bp = Blueprint('scenes', __name__)

@bp.route('/')
def index():
    return render_template('base.html')

@bp.route('/death')
def death():
    return render_template('scenes/death.html')

@bp.route('/beginning', methods=('GET', 'POST'))
def beginning():

    current_scene = {
    'riddle':"""You are out of the city on your first vaction in awhile.
    Yet round fifty miles out you car stars to sputter.
    Darn you should have gotten your car checked out on time.
    What do you do? 1.Road, 2.Forest, 3.CheckEngine"""
    }

    if (request.method == 'POST'):
        input = request.form['riddle']

        if input == "1":
            return render_template('index.html')
        else:
            return redirect(url_for('scenes.death'))
    else:
        return render_template('scenes/game.html', scene=current_scene)
