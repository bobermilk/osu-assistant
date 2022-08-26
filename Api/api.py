from flask import Flask
from flask_restful import Resource, Api, reqparse
import data
import time
from threading import Thread

app = Flask(__name__)
api = Api(app)

def start():
    app.run(debug=False)

def update_data():
    while True:
        data.update_tournaments()
        data.update_mappacks()
        time.sleep(60)

class Tournaments(Resource):
    def get(self):
        # example: localhost:80?gamemode=m
        # parser = reqparse.RequestParser()
        # type=parser.add_argument("type", type=int, location='args')
        # gamemode=parser.add_argument("gamemode", type=int, location='args')
        return data.tournament_json

class Mappack(Resource):
    def get(self):
        # example: localhost:80?status=r&gamemode=m
        # parser = reqparse.RequestParser()
        # type=parser.add_argument("status", type=int, location='args')
        # gamemode=parser.add_argument("gamemode", type=int, location='args')
        return data.mappack_json

api.add_resource(Tournaments, '/tournament', endpoint='tournament')
api.add_resource(Mappack, '/mappack', endpoint='mappack')

if __name__ == '__main__':
    p1=Thread(target=update_data)
    p1.start()
    start()