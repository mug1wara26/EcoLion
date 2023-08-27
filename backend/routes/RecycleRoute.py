import sys
import os
sys.path.append(os.path.abspath('../models'))

from flask import Flask, jsonify, request, Blueprint, make_response
import models.EventModel as eventModel
import models.CommunityModel as communityModel
import models.RecycleModel as recycleModel
import models.UserModel as userModel
from config import dbfetch, dbcommit

recycleRouter = Blueprint('recycleRouter', __name__)

@recycleRouter.route('/create', methods=['POST'])
def create_recycle():
    data = request.json
    token = request.headers['Authorization']
    user = userModel.login_with_token(token)
    if user:
        user_id = user.id
        recycle = data['recycle']
        recycle_id = recycleModel.create_recycle(user_id, recycle)
        if recycle_id:
            return jsonify(recycle_id=vars(recycle_id))
        else: 
            return make_response(status=500)
    else:
        return make_response(status=400)


@recycleRouter.route('/accept', methods=['POST'])
def accept_recycle():
    token = request.headers['Authorization']
    recycle_id = request.json['recycle_id']
    user = userModel.login_with_token(token)
    user_id = user.id
    if user:
        success = recycleModel.accept_recycle(user_id, recycle_id)
        if success:
            return make_response(status=200)
        else:
            return make_response(status=500)
    else:
        return make_response(status=400)


@recycleRouter.route('/<recycle_id>')
def get_recycle(recycle_id):
    recycle = recycleModel.get_recycle(recycle_id)
    if recycle:
        return jsonify(recycle=vars(recycle))
    else: 
        return make_response(status=400)

@recycleRouter.route('/<user_id>')
def get_user_id_recycles(user_id):
    pass

@recycleRouter.route('/edit', methods=['POST'])
def edit_recycle():
    data = request.json
    token = request.headers['Authorization']
    user = userModel.login_with_token(token)
    user_id = user.id
    recycle_id = data['recycle_id']
    if recycleModel.is_user_creator(user_id, recycle_id):
        recycle = data['recycle']
        recycle_id = recycleModel.edit_recycle(user_id, recycle)
        if recycle_id:
            return make_response(status=200)
        else: 
            return make_response(status=500)
    else:
        return make_response(status=400)


@recycleRouter.route('/remove', methods=['POST'])
def remove_recycle():
    data = request.json
    token = request.headers['Authorization']
    user = userModel.login_with_token(token)
    user_id = user.id
    recycle_id = data['recycle_id']
    if recycleModel.is_user_creator(user_id, recycle_id):
        success = recycleModel.delete_recycle(user_id, recycle_id)
        if success:
            return make_response(status=200)
        else: 
            return make_response(status=500)
    else:
        return make_response(status=400)



@recycleRouter.route('/undo', methods=['POST'])
def undo_recycle():
    data = request.json
    token = request.headers['Authorization']
    user = userModel.login_with_token(token)
    if user:
        recycle_id = data['recycle_id']
        user_id = user.id
        success = recycleModel.undo_recycle(user_id, recycle_id)
        if success:
            return make_response(status=200)
        else: 
            return make_response(status=500)
    else:
        return make_response(status=400)
    
    
@recycleRouter.route('/test')
def test():
    return recycleModel.get_recycle_posts_from_community()