from flask import Flask, request
from flask_restful import Resource, Api, reqparse, abort

app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument("phone", type = int, help="Number is required", required = True )
parser.add_argument("age", type = int, help = "Age must be an integer")
'''
TODO 1: Declare arguments to be used in your request parser
Eg. parser.add_argument("", type=, help="", required=)
'''
info = {}
class HelloWorld(Resource):
    def get(self):
        name = request.args.get("name")
        return {"Hello": name}

def not_found(name):
    '''
    TODO 2: Create function to check if entry is not found in database
    Call abort with 2 arguments, error code and message to display
    '''
    if name not in info:
        abort(404, message = "cannot find friend")

def dupe_entry(name):
    '''
    TODO 3: Create function to check if entry already exists in database
    Call abort with 2 arguments, error code and message to display
    '''
    if name in info:
        abort(409, message = "name is taken")

class Basics(Resource):
    '''
    TODO 4: Fill in the 4 HTTP methods, GET, POST, PUT and DELETE
    Each method should return a tuple, 1st Arg is the Data, 2nd Arg is the Status Code (200, 201, ...)
    '''
    def get(self, name):
        not_found(name)
        return info[name]

    def post(self, name):
        dupe_entry(name)
        args = parser.parse_args()
        info[name] = args
        return info[name]

    def put(self, name):
        args = parser.parse_args()
        info[name] = args
        return info[name]

    def delete(self,name):
        del info[name]
        return ""

api.add_resource(HelloWorld, '/hi')
api.add_resource(Basics, '/basic/<string:name>')

if __name__ == '__main__':
    app.run(debug=True)