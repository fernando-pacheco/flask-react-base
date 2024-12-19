import os

import sqlalchemy as sa
from sqlalchemy.sql import func
from src.db import db_instance as db
from src.db import db_persist


class TokenBlocklistModel(db.Model):
    __tablename__ = 'TokenBlockList'
    __table_args__ = {'schema': os.getenv('DEFAULT_DB_SCHEMA')}

    id = db.Column(db.Integer, primary_key=True)
    jti = db.Column(db.String(36), nullable=False, index=True)
    data_criacao = db.Column(
        db.DateTime(timezone=True), nullable=False, default=func.now()
    )

    @classmethod
    def obter_token(cls, jti):
        return (
            db.session.query(TokenBlocklistModel.id)
            .filter_by(jti=jti)
            .scalar()
        )

    @db_persist
    def salvar(self):
        db.session.add(self)


sa.orm.configure_mappers()
