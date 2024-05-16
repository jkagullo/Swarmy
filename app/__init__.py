from flask import Flask
from .blueprints.home import home
from .blueprints.schedname import schedname

def create_app():
    app = Flask(__name__)
    app.register_blueprint(home)
    app.register_blueprint(schedname)

    return app