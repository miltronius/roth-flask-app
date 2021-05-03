import json
import uuid

from flask import Flask, request
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)

app.config['CORS_HEADERS'] = 'Content-Type'

# Variables
musicFile = "music_list.json"


@app.before_first_request
def init():
    print('INIT')


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
        'lorem': 'ipsum',
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
    song = request.get_json()

    # add uuid to object
    songUuid = uuid.uuid4()
    song['uuid'] = str(songUuid)  # evt str(...)

    # append song to json file
    jsonObj = read_json_file(musicFile)
    jsonObj['songs'].append(song)

    with open(musicFile, 'w') as jsonFile:
        json.dump(dict(jsonObj), jsonFile)

    return {'message': 'success',
            'uuid': songUuid
            }


@app.route('/updateSong', methods=['POST'])
@cross_origin()
def updateSong():
    print('[/updateSong] REQUEST', request)
    newSong = request.get_json()

    # replace newly updated song
    jsonObj = read_json_file(musicFile)
    jsonObj['songs'] = [newSong if obj['uuid'] == newSong['uuid'] else obj for obj in jsonObj['songs']]

    with open(musicFile, 'w') as jsonFile:
        json.dump(dict(jsonObj), jsonFile)

    return {'message': 'success'}


@app.route('/deleteSong', methods=['POST'])
@cross_origin()
def deleteSong():
    print('[/deleteSong] REQUEST', request)
    songToBeDeleted = request.get_json()

    print('SONG TO BE DELETED:', songToBeDeleted)

    # remove song
    jsonObj = read_json_file(musicFile)
    jsonObj['songs'].remove(songToBeDeleted)

    with open(musicFile, 'w') as jsonFile:
        json.dump(dict(jsonObj), jsonFile)

    return {'message': 'success'}


@app.route('/getMusicDict', methods=['GET'])
@cross_origin()
def getMusicDict():
    print('[/getMusicDict] REQUEST', request)
    return read_json_file(musicFile)


def read_json_file(filename: str):
    with open(filename) as jsonFile:
        return json.load(jsonFile)
