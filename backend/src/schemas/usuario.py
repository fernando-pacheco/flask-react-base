from marshmallow import Schema, fields
from src.schema import ma


class UsuarioResponseSchema(ma.Schema):
    id = fields.UUID()
    nome_usuario = fields.Str()
    nome = fields.Str()
    sobrenome = fields.Str()
    email = fields.Str()
    cpf = fields.Str()
    data_criacao = fields.DateTime()
    data_atualizacao = fields.DateTime()
    ativo = fields.Bool()

    class Meta:
        fields = (
            'id',
            'nome_usuario',
            'nome',
            'sobrenome',
            'cpf',
            'email',
            'data_criacao',
            'data_atualizacao',
            'ativo',
        )

    _links = ma.Hyperlinks({'self': ma.URLFor('usuario')})


class UsuarioRequestPostSchema(Schema):
    nome_usuario = fields.Str(
        required=True, default='usuario', help='Esse campo não pode ser nulo'
    )
    senha = fields.Str(
        required=True, default='senha', help='Esse campo não pode ser nulo'
    )
    cpf = fields.Str(
        required=True,
        default='111.111.111-11',
        help='Esse campo não pode ser nulo',
    )
    nome = fields.Str(
        required=True, default='nome', help='Esse campo não pode ser nulo'
    )
    email = fields.Str(
        required=True,
        default='nome@xpto.com',
        help='Esse campo não pode ser nulo',
    )
    sobrenome = fields.Str()


class UsuarioRequestPutSchema(Schema):
    nome_usuario = fields.Str()
    senha = fields.Str()
    cpf = fields.Str()
    nome = fields.Str()
    email = fields.Str()
    sobrenome = fields.Str()
    ativo = fields.Bool()


usuario_schema = UsuarioResponseSchema()
usuario_post_schema = UsuarioRequestPostSchema()
