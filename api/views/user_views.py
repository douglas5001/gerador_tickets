from flask_restful import Resource
from ..schema import user_schema
from ..entidades import user
from flask import request, make_response, jsonify

from ..service.user_service import create_user


class UsuarioList(Resource):
    def post(self):
        us = user_schema.Usuario()
        validate = us.validate(request.json)
        if validate:
            return make_response(jsonify('Usuario nao encontrador'), 404)
        else:
            name = request.form['nome']
            email = request.form['email']
            is_admin = request.form['is_admin']
            password = request.form['password']
            new_user = user.User(name=name, email=email, password=password, is_admin=is_admin)
            result = create_user(new_user)
            x = us.jsonify(result)
            return make_response(x, 200)

