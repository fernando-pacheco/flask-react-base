from flask_migrate import Migrate


def load_migrate(db_instance, app):
    return Migrate(app, db_instance)
