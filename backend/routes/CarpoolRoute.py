from flask import Flask
from flask import jsonify
from flask import request
from flask import Blueprint
from flask import make_response
import models.UserModel as userModel
import models.CommunityModel as communityModel
import models.CarpoolModel as carpoolModel
from sklearn.cluster import DBSCAN

carpoolRouter = Blueprint('carpoolRouter', __name__)

# For organizations and communities to create carpooling events (to be done)
@carpoolRouter.route("/create", methods=['POST'])
def create_carpool():
    community_id = request.json['community_id']
    return None

#get carpool(carpool time, user_id of partner)
#   if successful, return list of peoples ids
@carpoolRouter.route("/update", methods=['POST'])
def update_carpool():
    event_id = request.json['event_id']
    user_id = request.json['user_id']
    if user_id in carpoolModel.get_carpool(event_id):
        carpoolModel.leaving_carpool(user_id,event_id)
    else:
        carpoolModel.participating_carpool(user_id,event_id)
    matches = carpoolModel.get_carpool(event_id)
    if not matches:
        return make_response(status=500)
    return jsonify(matches = vars(matches))

@carpoolRouter.route("/<user_id>")
def get_carpool(user_id):
    success = carpoolModel.get_carpool_by_userid(user_id)
    if not success:
        return make_response(status=500)
    return make_response(status=200)

@carpoolRouter.route("/users")
def get_users():
    carpoolUsers = carpoolModel.get_carpool_users(2)
    coords = [[i['latitude'], i['longitude']] for i in carpoolUsers]

    clustering = DBSCAN(eps=0.012, min_samples=2).fit([[i[0], i[1]] for i in coords])
    if list(set(clustering.labels_))[0] == -1:
        n_clusters = len(set(clustering.labels_))-1
    else:
        n_clusters = len(set(clustering.labels_))
    print(clustering.labels_)
    print(n_clusters)
    clusters = [[] for i in range(n_clusters)]

    for i in range(len(clustering.labels_)):
        label = int(clustering.labels_[i])
        if label != -1:
            clusters[label].append(carpoolUsers[i])


    return clusters
