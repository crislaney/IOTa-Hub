
from flask import Flask, request, send_from_directory
import sys
import json
from flask_jwt import JWT, jwt_required, current_identity
from werkzeug.security import safe_str_cmp
from flask_cors import CORS, cross_origin
from flask_httpauth import HTTPBasicAuth

from classes.LiveUpdater import LiveUpdater
from classes.DB_Manager import DB_Manager


class User(object):
    def __init__(self, id):
        self.id = id
    def __str__(self):
        return "User(id='%s')" % self.id

app = Flask(__name__, static_url_path='')
auth = HTTPBasicAuth()
CORS(app, support_credentials=True)
updater = LiveUpdater()
db_manager = DB_Manager()
app.config['SECRET_KEY'] = 'development_key_here'

def authenticate(user_name, password):
    print("Authenticating")
    user = db_manager.Authorize_User(user_name, password)
    if user is not None:
        return User(user)

def identity(payload):
    print("identifying")
    user_id = payload['identity']
    return {"user_id":user_id}

jwt = JWT(app, authenticate, identity)


@app.route("/")
def index():
    return send_from_directory('static/', 'index.html')

@app.route("/api/lights")
@cross_origin(origin='localhost',headers=['Content- Type','Authorization'])
def get_lights():
    temp = json.dumps(updater.create_step())
    return temp

@app.route("/api/light/<name>", methods=['PUT'])
@cross_origin(origin='localhost',headers=['Content- Type','Authorization'])
def update_light(name):
    new_dict = {}
    try:
        new_dict[name] = json.loads(request.data)
    except Exception as e:
        return 'malformed json', 400
    
    try:
        updater.run_step(new_dict)
    except Exception as e:
        print("EXCEPTION: " + e)
        return 'error updating light', 400

    return 'success', 200

@app.route("/api/setup")
def setup():
    return

@app.route("/api/step", methods=['POST'])
def record_step():
    updater.create_step()

#@app.route("/api/auth", methods=['POST'])
#def authorize_user():
    # username
    # password
    # return jwt

if __name__=='__main__':
    app.run(debug=True)
