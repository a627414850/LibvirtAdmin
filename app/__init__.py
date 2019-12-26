from flask import Flask
from config import Config

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from flask_login import LoginManager

#flask_app = Flask(__name__)
#flask_app.config.from_object(Config)

#login = LoginManager(flask_app)
#login.login_view = 'login'

#db = SQLAlchemy(flask_app)
#migrate = Migrate(flask_app, db)

import logging
from logging.handlers import RotatingFileHandler
import os

db = SQLAlchemy()
migrate = Migrate()
login = LoginManager()
login.login_view = 'auth.login'

def create_app(config_class=Config):
    flask_app = Flask(__name__)
    flask_app.config.from_object(config_class)

    db.init_app(flask_app)
    migrate.init_app(flask_app)
    login.init_app(flask_app)

    if not flask_app.debug:
        if not os.path.exists('logs'):
            os.mkdir('logs')
        file_handler = RotatingFileHandler('logs/VMSAdmin.log', maxBytes=10240,
                                        backupCount=10)
        file_handler.setFormatter(logging.Formatter(
            '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
        file_handler.setLevel(logging.INFO)
        flask_app.logger.addHandler(file_handler)

        flask_app.logger.setLevel(logging.INFO)
        flask_app.logger.info('VMS-Admin Startup')

    from app import models, errors

    from app.auth import bp as auth_bp
    from app.errors import bp as errors_bp
    from app.main import bp as main_bp

    flask_app.register_blueprint(auth_bp)
    flask_app.register_blueprint(errors_bp)
    flask_app.register_blueprint(main_bp)
    return flask_app
