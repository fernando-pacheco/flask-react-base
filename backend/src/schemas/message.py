from marshmallow import Schema, fields


class MessageErro400(Schema):
    message = fields.Str(example='Operação não processada, erro do cliente.')


class MessageErro401(Schema):
    message = fields.Str(
        example='Erro na autenticação, credenciais inválidas.'
    )


class MessageErro403(Schema):
    message = fields.Str(
        example='Usuário não autorizado a realizar esta ação.'
    )


class MessageErro404(Schema):
    message = fields.Str(example='Item ou objeto não encontrado.')


class MessageTokenRevoked(Schema):
    message = fields.Str(example='Token de acesso revogado ou expirado.')
