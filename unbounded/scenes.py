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

    current_scene = {'riddle':
    """You are out of the city on your first vaction in awhile.
    Yet round fifty miles out you car stars to sputter.
    Darn you should have gotten your car checked out on time.
    What do you do? 1.Road, 2.Forest, 3.CheckEngine"""
    }

    if (request.method == 'POST'):
        input = request.form['riddle']

        if input == "1":
            return redirect(url_for('scenes.road'))
        elif input == "2":
            return redirect(url_for('scenes.death'))
        elif input == "3":
            return redirect(url_for('scenes.death'))
        else:
            return redirect(url_for('scenes.death'))
    else:
        return render_template('scenes/game.html', scene=current_scene)

@bp.route('/road', methods=('GET', 'POST'))
def road():

    current_scene = {'riddle':
    """As you travel back down the road you notice a barn.
    You are feeling tired but unsure of what to do.
    What do you decide? 1.barn 2.road"""
    }

    if (request.method == 'POST'):
        input = request.form['riddle']

        if input == "1":
            return redirect(url_for('scenes.barn'))
        elif input == "2":
            return redirect(url_for('scenes.death'))
        else:
            return redirect(url_for('scenes.death'))
    else:
        return render_template('scenes/game.html', scene=current_scene)

@bp.route('/barn', methods=('GET', 'POST'))
def barn():

    current_scene = {'riddle':
    """The barn is warm inside.
    You decide to stay for the night and rest till morning.
    Time passes and you begin to drift off.
    As you awake you hear the farmer yelling at you to get out or he will shoot.
    What do you do? 1.Walk out with hands rasied 2.Sneak past 3.Run out"""
    }

    if (request.method == 'POST'):
        input = request.form['riddle']
        if input == "1":
            return redirect(url_for('scenes.death'))
        elif input == "2":
            return redirect(url_for('scenes.path'))
        else:
            return redirect(url_for('scenes.path'))
    else:
        return render_template('scenes/game.html', scene=current_scene)

@bp.route('/path', methods=('GET', 'POST'))
def path():

    current_scene = {'riddle':
    """The Road is not finished! Sorry about that."""
    }

    if (request.method == 'POST'):
        input = request.form['riddle']
        if input == "":
            return render_template('index.html')
        else:
            return render_template('index.html')
    else:
        return render_template('scenes/game.html', scene=current_scene)
