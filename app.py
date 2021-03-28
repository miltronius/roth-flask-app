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
