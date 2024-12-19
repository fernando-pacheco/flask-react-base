from flask_restful import Api
from src.resources.health_checker import HealthCheckerResource
from src.resources.token import (
    TokenRefresherResource,
    TokenRevokeResource,
    TokenUsuarioResource,
)
from src.resources.usuario import UsuarioResource, UsuariosResource


def config_app_routes(app, docs):
    api = Api(app)

    # Usuário
    __setting_route_doc(UsuariosResource, '/usuario', api, docs)
    __setting_route_doc(UsuarioResource, '/usuario/<string:id>', api, docs)

    # Token
    __setting_route_doc(TokenUsuarioResource, '/login', api, docs)
    __setting_route_doc(TokenRefresherResource, '/token/refresh', api, docs)
    __setting_route_doc(TokenRevokeResource, '/token', api, docs)

    # Health Checker
    __setting_route_doc(HealthCheckerResource, '/health', api, docs)

    return api


def __setting_route_doc(resource, route, api, docs):
    api.add_resource(resource, route)
    docs.register(resource)
