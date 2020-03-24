import sqlite3

import click
from flask import current_app, g
from flask.cli import with_appcontext


def get_db():
    if 'db' not in g: #g is an object takes requests to store data that might be accessed multipul times during that request.
        g.db = sqlite3.connect( #establishes connection to file that points at DATABASE wont exist untill you initialize database.
            current_app.config['DATABASE'], #current_app is a special obj points to flask handles request. to create app. So it can be used
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row #Creates the rows of the dicts allows columns accessing by name

    return g.db

#checks if connection was created if so its closed
def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()

def init_db():
    db = get_db()

    with current_app.open_resource('schema.sql') as f:
        db.executescript(f.read().decode('utf8'))


@click.command('init-db') #simialir to the run command for this file
@with_appcontext
def init_db_command():
    """Clear the existing data and create new tables."""
    init_db()
    click.echo('Initialized the database.')

def init_app(app):
    app.teardown_appcontext(close_db) #Call the function after returning response
    app.cli.add_command(init_db_command) #adds new command that can be called with the flask command
