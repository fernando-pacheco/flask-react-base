import os
import uuid

import sqlalchemy as sa
from flask_login import UserMixin
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func
from src.db import db_instance as db
from src.db import db_persist
from src.login_manager import login_manager
from werkzeug.security import check_password_hash, generate_password_hash


@login_manager.user_loader
def get_user(user_id):
    return UsuarioModel.query.filter_by(id=user_id).first()


class UsuarioModel(db.Model, UserMixin):
    __tablename__ = 'Usuários'
    __table_args__ = {'schema': os.getenv('DEFAULT_DB_SCHEMA')}

    id = db.Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
        unique=True,
        nullable=False,
    )
    nome = db.Column(db.String(50), nullable=False)
    sobrenome = db.Column(db.String(100), nullable=True)
    cpf = db.Column(db.String(14), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    nome_usuario = db.Column(db.String(50), unique=True, nullable=False)
    senha = db.Column(db.String(200))
    data_criacao = db.Column(db.DateTime(timezone=True), default=func.now())
    data_atualizacao = db.Column(
        db.DateTime(timezone=True), default=func.now(), onupdate=func.now()
    )
    ativo = db.Column(db.Boolean, default=True)

    def __init__(self, nome_usuario, nome, sobrenome, senha, email, cpf):
        self.nome_usuario = nome_usuario
        self.definir_senha(senha)
        self.email = email
        self.nome = nome
        self.sobrenome = sobrenome
        self.cpf = cpf

    def __repr__(self):
        return f'<UsuarioModel(id={self.id}, nome_usuario={self.nome_usuario}), senha={self.senha})>'

    def definir_senha(self, senha):
        self.senha = generate_password_hash(senha)

    @db_persist
    def salvar(self):
        db.session.add(self)

    @db_persist
    def excluir(self):
        db.session.delete(self)

    @classmethod
    def encontrar_por_nome_usuario(cls, nome_usuario):
        return cls.query.filter_by(nome_usuario=nome_usuario).first()

    @classmethod
    def encontrar_por_id(cls, id):
        return cls.query.filter_by(id=id).first()

    @classmethod
    def encontrar_por_email(cls, email):
        return cls.query.filter_by(email=email).first()

    @classmethod
    def encontrar_por_cpf(cls, cpf):
        return cls.query.filter_by(cpf=cpf).first()

    def verificar_senha(self, senha):
        return check_password_hash(self.senha, senha)

    @staticmethod
    def init_data():
        if db.session.query(UsuarioModel.id).count() == 0:
            usuario = UsuarioModel(
                nome_usuario='fepacheco',
                senha='4210',
                cpf='111.111.111-11',
                email='email@xpto.com',
                nome='fernando',
            )
            usuario.salvar()


sa.orm.configure_mappers()
