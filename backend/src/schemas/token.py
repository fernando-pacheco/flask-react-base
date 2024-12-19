from marshmallow import Schema, fields


class AccessRefreshTokenUidResponseSchema(Schema):
    token_acesso = fields.Str()
    refresh_token = fields.Str()
    usuario_id = fields.UUID()


class AccessRefreshTokenRequestSchema(Schema):
    credencial = fields.Str(required=True)
    senha = fields.Str(required=True)
