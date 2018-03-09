
from flask import Flask, request, send_from_directory
import sys
import json
from classes.LiveUpdater import LiveUpdater
from flask_cors import CORS, cross_origin

app = Flask(__name__, static_url_path='')
CORS(app, support_credentials=True)
updater = LiveUpdater()

@app.route("/")
def index():
    return send_from_directory('static/', 'index.html')

@app.route("/lights")
@cross_origin(origin='localhost',headers=['Content- Type','Authorization'])
def get_lights():
    temp = json.dumps(updater.create_step())
    return temp

@app.route("/light/<name>", methods=['PUT'])
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

@app.route("/setup")
def setup():
    return

@app.route("/step", methods=['POST'])
def record_step():
    updater.create_step()


if __name__=='__main__':
    app.run(debug=True)
