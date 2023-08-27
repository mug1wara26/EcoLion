import sys
import os
sys.path.append(os.path.abspath('../models'))

from flask import Flask
from flask import jsonify
from flask import request
from flask import Blueprint
from flask  import make_response
import models.UserModel as userModel

userRouter = Blueprint('userRouter', __name__)

@userRouter.route('/register', methods=['POST'])
def register_user():
    data = request.json
    user_data = data['user']
    token = userModel.register(user_data)
    if token:
        return jsonify(token = token)
    else:
        return make_response(status=400)

@userRouter.route('/login', methods=['POST'])
def login_user():
    data = request.json
    user_data = data['user']
    token = userModel.login(user_data)
    if token:
        return jsonify(token = token)
    else:
        return make_response(status=400)

@userRouter.route('/')
@userRouter.route('/<user_id>')
def get_user(user_id=None):
    if user_id:
        user = userModel.get_user_by_id(user_id)
        return user
        limited_data = True
    else:
        token = request.headers['Authorization']
        user = userModel.login_with_token(token)
        limited_data = False
    if user:
        if limited_data:
            username = user['username']
            biography = user['biography']
            return jsonify(username = username, biography = biography)
        else:
            return jsonify(user = vars(user))
    else:
        return make_response('', 400)

@userRouter.route('/edit', methods=['POST'])
def edit_user():
    data = request.json
    new_user_data = data['user']
    token = request.cookies['token']
    user = userModel.login_with_token(token)
    user_id = user.id
    success = userModel.edit_user(user_id, new_user_data)
    if success:
        return make_response(status=200)
    else:
        return make_response(status=400)

@userRouter.route('/delete', methods=['POST'])
def delete_user():
    token = request.cookies['token']
    user = userModel.login_with_token(token)
    success = userModel.delete_user(user.id)
    if success:
        return make_response(status=200)
    else:
        return make_response(status=400)
