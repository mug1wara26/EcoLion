from flask import Flask
from flask import jsonify
from flask import request
from flask import Blueprint
from flask import make_response
import models.UserModel as userModel
import models.CommunityModel as communityModel

communityRouter = Blueprint('communityRouter', __name__)

@communityRouter.route('/create', methods=['POST'])
def create_community():
    data = request.json
    token = request.headers['Authorization']
    user = userModel.login_with_token(token)
    community = data['community']
    if user:
        community_id = communityModel.create_community(user.id, community)
        if community_id:
            return jsonify(community_id=community_id)
        else:
            return make_response(status=500)
    else:
        return make_response(status=400)


@communityRouter.route('/join', methods=['POST'])
def join_community():
    data = request.json
    token = request.headers['Authorization']
    community_id = data['community_id']
    user = userModel.login_with_token(token)
    user_id = user.id
    if user:
        success = communityModel.join_community(user_id, community_id)
        if success:
            return make_response(status=200)
        else:
            return make_response(status=500)
    else:
        return make_response(status=400)

@communityRouter.route('/get_communities')
def get_communities():
    # Dummy data
    communities = communityModel.get_communities()
    print(communities)
    return jsonify(communities=communities)


@communityRouter.route('/<community_id>')
def get_community(community_id):
    community = communityModel.get_community(community_id)
    if community:
        return jsonify(community=vars(community))
    else:
        return make_response(status=400)

@communityRouter.route('/edit', methods=['POST'])
def edit_community():
    data = request.json
    token = request.headers['Authorization']
    user = userModel.login_with_token(token)
    user_id = user.id
    community = data['community']
    success = communityModel.edit_community(community)
    community_id = data['community_id']
    if communityModel.is_user_admin(user_id, community_id):
            if success:
                return make_response(status=200)
            else:
                return make_response(status=500)
    else:
        return make_response(status=400)

@communityRouter.route('/delete', methods=['POST'])
def delete_community():
    data = request.json
    token = request.headers['Authorization']
    user = userModel.login_with_token(token)
    community_id = data['community_id']
    user_id = user.id
    if communityModel.is_user_admin(user_id, community_id):
        community_name = data['community_name']
        success = delete_community(community_name, community_id)
        if success:
            return make_response(status=200)
        else:
            return make_response(status=500)
    else:
        return make_response(status=400)

@communityRouter.route('/leave', methods=['POST'])
def leave_community():
    data = request.json
    token = request.headers['Authorization']
    user = userModel.login_with_token(token)
    if user:
        community_id = data['community_id']
        user_id = user.id
        success = communityModel.leave_community(user_id, community_id)
        if success:
            return make_response(status=200)
        else:
            return make_response(status=500)
    else:
        return make_response(status=400)

@communityRouter.route('/test')
def test():
    return str(communityModel.get_communities(1))