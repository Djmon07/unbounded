import os

from flask import Flask, render_template

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    app.config.from_mapping(
        SECRET_KEY='dev',
    )

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)

    else:
        app.config.from_mapping(test_config)

    @app.route('/')
    def index():
        return render_template('index.html')

    from . import scenes
    app.register_blueprint(scenes.bp)
    app.add_url_rule('/', endpoint='index')

    return app
