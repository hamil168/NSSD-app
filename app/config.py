import os
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_sslify import SSLify
from flask_stormpath import StormpathManager


def set_config(app):
    """Set configuration for Flask app
    """

    SSLify(app)
    Bootstrap(app)
    app.config.from_object(os.environ['APP_SETTINGS'])

    # Set up SQLAlchemy DB
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
    db = SQLAlchemy(app)

    # OAuth credentials and configuration
    app.config['SECRET_KEY'] = os.environ['STORMPATH_SECRET_KEY']
    app.config['STORMPATH_API_KEY_ID'] = os.environ['STORMPATH_API_KEY_ID']
    app.config['STORMPATH_API_KEY_SECRET'] = os.environ['STORMPATH_API_KEY_SECRET']
    app.config['STORMPATH_APPLICATION'] = os.environ['STORMPATH_APPLICATION']
    app.config['STORMPATH_ENABLE_MIDDLE_NAME'] = False
    app.config['STORMPATH_ENABLE_FORGOT_PASSWORD'] = True
    StormpathManager(app)

    return db

max_docs = 500