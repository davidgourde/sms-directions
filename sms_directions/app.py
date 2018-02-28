from flask import Flask, request
import flask_restful as rest

from sms_directions.directions import get_directions


app = Flask(__name__)
app.config.from_pyfile('config.py')
api = rest.Api(app)


class GetDirections(rest.Resource):
    def get(self):
        origin, destination, mode = request.args['text'].split()
        return get_directions(), 200


api.add_resource(GetDirections, '/')

if __name__ == '__main__':
    app.run()
