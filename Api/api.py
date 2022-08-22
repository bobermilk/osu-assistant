from flask import Flask
from flask_restful import Resource, Api, reqparse
import data

app = Flask(__name__)
api = Api(app)

class Tournaments(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        type=parser.add_argument("type", type=int, location='args')
        gamemode=parser.add_argument("gamemode", type=int, location='args')
        return data.search_tournament(type, gamemode)

class Beatconnect(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        type=parser.add_argument("status", type=int, location='args')
        gamemode=parser.add_argument("gamemode", type=int, location='args')
        return data.search_beatconnect(type, gamemode)

api.add_resource(Tournaments, '/tournament', endpoint='tournament')
api.add_resource(Beatconnect, '/beatconnect', endpoint='beatconnect')
if __name__ == '__main__':
    app.run(debug=True)