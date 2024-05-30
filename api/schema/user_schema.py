from api import ma
from marshmallow import fields

from api.models import user_model


class Usuario(ma.SQLAlchemyAutoSchema):

    class Meta:
        model = user_model.User
        load_instance = True
        fields = ("id", "nome", "email", "senha", "is_admin")

    nome = fields.String(required=True)
    email = fields.String(required=True)
    senha = fields.String(required=True)
    is_admin = fields.Boolean(required=True)