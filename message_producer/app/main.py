from flask import Flask
from routes.email_routes import email_blueprint
from db.models import *


def create_app():
    app = Flask(__name__)
    app.register_blueprint(email_blueprint, url_prefix="/api/")
    return app


if __name__ == '__main__':
    app = create_app()
    app.run()
