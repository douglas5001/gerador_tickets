from api import ma
from marshmallow import fields

from api.models import user_model


class Login(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = user_model.User
        load_instance = True
        fields = ("id", "nome", "email", "senha")

    nome = fields.String(required=False)
    email = fields.String(required=True)
    senha = fields.String(required=True)