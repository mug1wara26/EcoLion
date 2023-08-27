import sys
import os
sys.path.append(os.path.abspath('schema'))
sys.path.append(os.path.abspath('models'))
sys.path.append(os.path.abspath('routes'))

from flask import jsonify
from flask import request
from flask_cors import CORS
from routes.UserRoute import userRouter
from routes.CommunityRoute import communityRouter
from routes.EventRoute import eventRouter
from routes.CarpoolRoute import carpoolRouter
from routes.RecycleRoute import recycleRouter
import models.UserModel
from config import app, mysql, dbfetch

app.register_blueprint(userRouter, url_prefix='/user')
app.register_blueprint(communityRouter, url_prefix='/community')
app.register_blueprint(eventRouter, url_prefix='/event')
app.register_blueprint(carpoolRouter, url_prefix='/carpool')
app.register_blueprint(recycleRouter,url_prefix='/recycle')
CORS(app)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)

