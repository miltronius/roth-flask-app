import json

from flask import Flask, request
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)

app.config['CORS_HEADERS'] = 'Content-Type'


@app.route('/')
@cross_origin()
def hello_world():
    print('[/] REQUEST', request)
    return 'Hello, World! This app is deployed on heroku! 1'


@app.route('/getReq', methods=['GET'])
@cross_origin()
def getReq():
    print('[/getReq] REQUEST', request)
    return {
        'gurke': 'asd',
        'age': 28
    }


@app.route('/ping', methods=['POST'])
@cross_origin()
def postPing():
    print('[/ping] REQUEST', request)
    return request.data


@app.route('/addSong', methods=['POST'])
@cross_origin()
def addSong():
    print('[/addSong] REQUEST', request)
    song = request.data
    with open("music_list.json", "w") as jsonFile:
        json.dump(song, jsonFile)
    return True


@app.route('/getMusicDict', methods=['GET'])
@cross_origin()
def getMusicDict():
    print('[/getMusicDict] REQUEST', request)
    return read_json_file("music_list.json")


def read_json_file(filename: str):
    with open(filename) as f_in:
        return json.load(f_in)
