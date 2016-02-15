from flask import Flask
from flask_restful import Resource, Api
from send import rpc
import json

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        a = json.dumps(['foo', {'bar': ('baz', None, 1.0, 2)}])
        response = rpc.call(a)
        return json.loads(response)

api.add_resource(HelloWorld, '/')

if __name__ == '__main__':
    app.run(debug=True)
