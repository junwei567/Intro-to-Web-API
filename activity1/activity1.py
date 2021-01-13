from flask import Flask
from flask_restful import Resource, Api, reqparse, abort

app = Flask(__name__)
api = Api(app)

info = {}

parser = reqparse.RequestParser()
parser.add_argument("phone", type=int, help="Number is required", required=True)
parser.add_argument("age", type=int, help="Age must be an integer")

class HelloWorld(Resource):
    def get(self):
        return {"Hello": "World"}

def not_found(name):
    if name not in info:
        abort(404, message='Cannot find friend')

def dupe_entry(name):
    if name in info:
        abort(409, message='friend already exists')

class Basics(Resource):
    # def get(self, name):
    #     return {"Hello": name}
    def get(self, name):
        not_found(name)
        return info[name], 200

    def post(self, name):
        dupe_entry(name)
        args = parser.parse_args()
        info[name] = args
        return info[name], 201

    def put(self, name):
        args = parser.parse_args()
        info[name] = args
        return info[name], 201

    def delete(self,name):
        del info[name]
        return '', 204

api.add_resource(HelloWorld, '/hi')
api.add_resource(Basics, '/basic/<string:name>')

if __name__ == '__main__':
    app.run(debug=True)