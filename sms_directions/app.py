from flask import Flask, request
import flask_restful as rest

from sms_directions.directions import get_directions
from sms_directions.sms import send_sms


def init_rest_api(app):
    api = rest.Api(app)

    class GetDirections(rest.Resource):
        def get(self):
            args = request.args.get('text').split(';')
            if len(args) == 2:
                origin, destination = args
                mode = 'driving'
            elif len(args) == 3:
                origin, destination, mode = args
            else:
                send_sms('La syntaxe correcte est: origin;destination;transit où ;transit est optionnel.')
            return get_directions(origin, destination, mode), 200

    api.add_resource(GetDirections, '/')


def init_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    init_rest_api(app)
    return app


app = init_app()

if __name__ == '__main__':
    app.run()
