
from flask import Flask, request, send_from_directory, Response
import sys
import json
from flask_jwt import timedelta, JWT, jwt_required, current_identity
from werkzeug.security import safe_str_cmp
from flask_cors import CORS, cross_origin
from flask_httpauth import HTTPBasicAuth

from classes.LiveUpdater import LiveUpdater
from classes.DB_Manager import DB_Manager
import time


class User(object):
    def __init__(self, id):
        self.id = id
    def __str__(self):
        return "User(id='%s')" % self.id

app = Flask(__name__, static_url_path='')
auth = HTTPBasicAuth()
# cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
updater = LiveUpdater()
db_manager = DB_Manager()
app.config['SECRET_KEY'] = 'development_key_here'
app.config['JWT_EXPIRATION_DELTA'] = timedelta(seconds=86400)
app.config['CORS_HEADERS'] = 'Content-Type'
app.config['CORS_HEADERS'] = 'Authorization'
cors = CORS(app, headers=["Content-Type", "Authorization"], resources=r"/*")


def authenticate(user_name, password):
    user = db_manager.Authorize_User(user_name, password)
    print(user)
    print(password)
    if user is not None:
        return User(user)

def identity(payload):
    user_id = payload['identity']
    return {"user_id":user_id}

jwt = JWT(app, authenticate, identity)


@app.route("/")
def index():
    return send_from_directory('static/', 'index.html')

@app.route("/api/lights")
@cross_origin()
def get_lights():
    step = updater.create_step()
    temp = json.dumps(step)
    return temp

@app.route("/api/light/<name>", methods=['PUT'])
@cross_origin()
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


@app.route("/api/step", methods=['GET', 'PUT'])
@cross_origin(allow_headers=['Content-Type', 'Authorization'])
@jwt_required()
def current_step2():
    if request.method == 'GET':
        resp = json.dumps(updater.create_step())
        return resp, 200

    if request.method == 'PUT':
        data_converted = json.loads(request.data)
        script = []
        if type(data_converted) is list:
            for step in data_converted:
                script.append(json.loads(step))
        else:
            script.append(data_converted)

        updater.run_script(script)
        return 'success', 200



@app.route("/api/script", methods=['POST', 'GET'])
@cross_origin(allow_headers=['Content-Type', 'Authorization'])
@jwt_required()
def post_script():
    id_num = dict(current_identity)['user_id']

    if request.method == 'POST':
        # post script to server
        db_manager.Insert_Script(id_num, json.loads(request.data))
        return 'success', 200

    if request.method == 'GET':
        all_scripts = db_manager.Get_All_Scripts(id_num)

        script_names_and_ids = []
        for script in all_scripts:
            script_names_and_ids.append({'name': script['name'], 'id': script['id']})
        return json.dumps(script_names_and_ids), 200
    
    return 'error', 500


# TODO Test!
@app.route("/api/script/<script_id>", methods=['PUT'])
@cross_origin(allow_headers=['Content-Type', 'Authorization'])
@jwt_required()
def put_script(script_id):
    # post script to server
    if request.method == 'PUT':
        id_num = dict(current_identity)['user_id']
        
        script = db_manager.Get_Script(id_num, script_id)[2]
        processed_script = []
        script_json = json.loads(script)
        for step in script_json:
            processed_script.append(json.loads(step))
        updater.run_script(processed_script)
        return 'success', 200

    return 'failure', 500

@app.route("/api/account", methods=['POST'])
def create_account():
    try:
        req_data = json.loads(request.data)
        db_manager.Insert_User(req_data['username'], req_data['password'])
    except Exception as e:
        print(e)
        return 'failure', 400

    return 'success', 201

if __name__=='__main__':
    app.run(debug=True)
