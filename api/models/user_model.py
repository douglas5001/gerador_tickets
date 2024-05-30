from passlib.hash import pbkdf2_sha256
from api import db


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(100), nullable=False)
    is_admin = db.Column(db.Boolean)

    def cripto(self):
        self.senha = pbkdf2_sha256.hash(self.senha)

    def verifyPass(self, senha):
        return pbkdf2_sha256.verify(senha, self.senha)

