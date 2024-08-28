from flask import Flask

def init_app():
    """Construct core Flask app"""
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object("config.Config")

    with app.app_context():
        # import parts of our core flask app
        from . import routes

        # import dash app
        from .plotlydash.dashboard import init_dashboard
        app = init_dashboard(app)

        from .plotlydash.dashboard import init_dashboard
        app = init_dashboard(app)

        return app

