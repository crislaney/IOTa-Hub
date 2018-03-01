
from flask import Flask, request, send_from_directory
import sys
sys.path.insert(0, './classes')
import LiveUpdater


app = Flask(__name__, static_url_path='')

def setup_app(app):
    updater = LiveUpdater()


    return

@app.route("/")
def index():
    return send_from_directory('static/iota-frontend/src/', 'index.html')

@app.route("/lights")
def get_lights():

        return 0

@app.route("/setup")

if __name__=='__main__':
    app.run(debug=True)
