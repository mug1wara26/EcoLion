import sys
import os
sys.path.append(os.path.abspath('../models'))

from flask import Flask, jsonify, request, Blueprint, make_response
import models.EventModel as eventModel
import models.CommunityModel as communityModel
import models.UserModel as userModel

eventRouter = Blueprint('eventRouter', __name__)


@eventRouter.route('/create', methods=['POST'])
def create_event():
    data = request.json
    token = request.headers['Authorization']
    user = userModel.login_with_token(token)
    community_id = data['community_id']
    user_id = user.id
    if communityModel.is_user_admin(user_id, community_id):
        event = data['event']
        event_id = eventModel.create_event(community_id, event)
        if event_id:
            return jsonify(event_id=vars(event_id))
        else: 
            return make_response(status=500)
    else:
        return make_response(status=400)

@eventRouter.route('/join', methods=['POST'])
def join_event():
    token = request.headers['Authorization']
    event_id = request.json['event_id']
    user = userModel.login_with_token(token)
    user_id = user.id
    if user:
        success = eventModel.join_event(user_id, event_id)
        if success:
            return make_response(status=200)
        else:
            return make_response(status=500)
    else:
        return make_response(status=400)


@eventRouter.route('/<event_id>')
def get_event(event_id):
    event = eventModel.get_event(event_id)
    if event:
        return jsonify(event=vars(event))
    else: 
        return make_response(status=400)

@eventRouter.route('/edit', methods=['POST'])
def edit_event():
    data = request.json
    token = request.headers['Authorization']
    user = userModel.login_with_token(token)
    community_id = data['community_id']
    user_id = user.id
    if communityModel.is_user_admin(user_id, community_id):
        event = data['event']
        event_id = event.id
        success = eventModel.edit_event(event_id, event)
        if success:
            return make_response(status=200)
        else: 
            return make_response(status=500)
    else:
        return make_response(status=400)

@eventRouter.route('/delete', methods=['POST'])
def delete_event():
    data = request.json
    token = request.headers['Authorization']
    user = userModel.login_with_token(token)
    community_id = data['community_id']
    user_id = user.id
    if communityModel.is_user_admin(user_id, community_id):
        event_id = data['event_id']
        success = eventModel.delete_event(event_id)
        if success:
            return make_response(status=200)
        else: 
            return make_response(status=500)
    else:
        return make_response(status=400)

@eventRouter.route('/leave', methods=['POST'])
def leave_event():
    data = request.json
    token = request.headers['Authorization']
    user = userModel.login_with_token(token)
    if user:
        event_id = data['event_id']
        user_id = user.id
        success = eventModel.leave_event(user_id, event_id)
        if success:
            return make_response(status=200)
        else: 
            return make_response(status=500)
    else:
        return make_response(status=400)

