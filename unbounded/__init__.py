from . import db
from . import auth
from flask import Flask


def create_app(test_config=None):
    app = Flask(__name__)
    app.config.from_mapping(
        SECRET_KEY='dev'
    )

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route('/')
    def index():
        return render_template('base.html')

    from . import db
    db.init_app(app)
    app.register_blueprint(auth.bp)
    app.add_url_rule('/', endpoint='index')

    from . import auth
    db.init_app(app)
    app.register_blueprint(auth.bp)
    app.add_url_rule('/', endpoint='index')

    return app
