import os

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError

db_instance = SQLAlchemy()


def config_sql_alchemy(app):

    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('POSTGRES_DSN')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = os.getenv(
        'SQLALCHEMY_TRACK_MODIFICATIONS'
    )
    app.config['SQLALCHEMY_ECHO'] = os.getenv('SQLALCHEMY_ECHO')
    db_instance.app = app
    db_instance.init_app(app)


def db_persist(func):
    def persist(*args, **kwargs):
        func(*args, **kwargs)
        try:
            db_instance.session.commit()
            return True
        except SQLAlchemyError:
            db_instance.session.rollback()
            return False

    return persist
