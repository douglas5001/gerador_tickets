from ..models import user_model
from api import db

def create_user(user):
    user_db = user_model.User(name=user.name, email=user.email, password=user.password, is_admin=user.is_admin)
    db.session.add(user_db)
    db.session.commit()
    return  user_db