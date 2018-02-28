from flask import Flask, request
import flask_restful as rest

from sms_directions.directions import get_directions


def init_rest_api(app):
    api = rest.Api(app)

    class GetDirections(rest.Resource):
        def get(self):
            try:
                origin, destination, mode = request.args.get('text').split(';')
                print('argsText = ' + request.args.get('text'))
            except Exception as e:
                print(e)
                origin, destination, mode = 'Laval', 'Montreal', 'transit'
            finally:
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
