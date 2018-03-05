
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
def update_light(name):
    # updater.run_script(request.)
    resp_dict = json.loads(request.data)
    
    new_dict = {}
    new_dict[name] = resp_dict
    print(new_dict)
    updater.run_step(new_dict)


    return 'success', 200

@app.route("/setup")
def setup():
    return



if __name__=='__main__':
    app.run(debug=True)
