from api import db


class Department(db.Model):
    __tablename__ = 'department'

    cod_depart = db.Column(db.Integer, autoincrement=True, primary_key=True, nullable=False)
    name_depart = db.Column(db.String(50), nullable=False)