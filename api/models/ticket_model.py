from api import db
from datetime import datetime

class Ticket(db.Model):
    __tablename__ = 'ticket'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    status = db.Column(db.String(50), nullable=False, default='Open')
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    closed_at = db.Column(db.DateTime, nullable=True)
    #creator_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    #technician_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True)
    #category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=False)