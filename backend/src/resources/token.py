import re
from datetime import datetime, timezone

from flask import make_response
from flask_apispec import doc, use_kwargs
from flask_apispec.views import MethodResource
from flask_jwt_extended import (
    create_access_token,
    create_refresh_token,
    get_jwt,
    get_jwt_identity,
    jwt_required,
)
from flask_login import login_user, logout_user
from flask_restful import Resource
from src.models.token import TokenBlocklistModel
from src.models.usuario import UsuarioModel
from src.schemas.message import MessageTokenRevoked
from src.schemas.token import (
    AccessRefreshTokenRequestSchema,
    AccessRefreshTokenUidResponseSchema,
)
from src.utils.decorators import error_decorators, marshal_with


@doc(tags=['Auth'])
@error_decorators()
@marshal_with(AccessRefreshTokenUidResponseSchema, code=200)
class TokenUsuarioResource(MethodResource, Resource):
    @use_kwargs(AccessRefreshTokenRequestSchema, location='json')
    @doc(description='Login e gerador de novo acesso de usuario')
    def post(self, **kwargs):
        resposta = make_response(
            {'message': 'Erro na autenticação, credenciais inválidas.'},
            401,
        )
        credencial = kwargs['credencial']
        senha = kwargs['senha']

        if re.match(r'[^@]+@[^@]+\.[^@]+', credencial):
            usuario = UsuarioModel.encontrar_por_email(credencial)
        else:
            usuario = UsuarioModel.encontrar_por_nome_usuario(credencial)

        if usuario and usuario.verificar_senha(senha):
            login_user(usuario)
            token_acesso = create_access_token(identity=usuario.id)
            refresh_token = create_refresh_token(usuario.id)
            resposta = make_response(
                {
                    'access_token': token_acesso,
                    'refresh_token': refresh_token,
                    'usuario_id': usuario.id,
                },
                201,
            )

        return resposta


@doc(tags=['Auth'])
@marshal_with(AccessRefreshTokenUidResponseSchema, code=200)
@use_kwargs(AccessRefreshTokenRequestSchema, location='json')
class TokenRefresherResource(MethodResource, Resource):
    @doc(
        description='Atualiza um token de acesso usando o token de atualização'
    )
    @jwt_required()
    def post(self):
        jwt_usuario_atual = get_jwt_identity()
        novo_token = create_access_token(
            identity=jwt_usuario_atual, fresh=False
        )
        return make_response({'token_acesso': novo_token}, 201)


@doc(tags=['Auth'])
@error_decorators(status_codes=[400])
@marshal_with(MessageTokenRevoked, code=200)
class TokenRevokeResource(MethodResource, Resource):
    @jwt_required()
    @doc(description='Revogar token de acesso atual')
    def delete(self):
        resposta = make_response({'message': 'Erro ao excluir o token.'}, 400)

        jti = get_jwt()['jti']
        logout_user()
        agora = datetime.now(timezone.utc)

        if TokenBlocklistModel(jti=jti, data_criacao=agora).salvar():
            resposta = make_response(
                {'message': 'Token de acesso revogado ou expirado'}, 200
            )

        return resposta
