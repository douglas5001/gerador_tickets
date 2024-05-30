from api import ma
from marshmallow import fields

from api.models import ticket_model


class TicketSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = ticket_model.Ticket
        load_instance = True
        fields = (
            "id", "title", "description", "status", "created_at", "closed_at",
            "creator_id", "technician_id", "category_id", "creator", "technician", "category"
        )

    title = fields.String(required=True)
    description = fields.String(required=True)
    status = fields.String(required=True)
    created_at = fields.DateTime(required=True)
    closed_at = fields.DateTime(required=False)
    creator_id = fields.Integer(required=True)
    technician_id = fields.Integer(required=False)
    category_id = fields.Integer(required=True)
    #creator = fields.Nested('UserSchema', only=("id", "name", "email"), required=True)
    #technician = fields.Nested('UserSchema', only=("id", "name", "email"), required=False)
    #category = fields.Nested('CategorySchema', only=("id", "name"), required=True)
