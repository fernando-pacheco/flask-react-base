import os
from datetime import timedelta

from flask import make_response
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from src.models.token import TokenBlocklistModel

ACCESS_EXPIRES = timedelta(hours=12)
REFRESH_EXPIRES = timedelta(hours=24)


def config_jwt_token(app):
    app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY')
    app.config['JWT_TOKEN_LOCATION'] = ['headers']
    app.config['JWT_COOKIE_SECURE'] = False
    app.config['JWT_ACCESS_TOKEN_EXPIRES'] = ACCESS_EXPIRES
    app.config['JWT_REFRESH_TOKEN_EXPIRES'] = REFRESH_EXPIRES

    jwt = JWTManager(app)

    @jwt.token_in_blocklist_loader
    def check_if_token_is_revoked(jwt_header, jwt_payload):
        jti = jwt_payload['jti']
        token = TokenBlocklistModel.obter_token(jti)
        return token is not None

    @jwt.expired_token_loader
    @jwt.revoked_token_loader
    def custom_revoked_expired_message(jwt_header, jwt_payload):
        return make_response(
            {'message': 'Access token revoked or expired'}, 401
        )

    return jwt


def config_app_cors(app):
    CORS(app, resources={r'*': {'origins': '*'}})
