from flask import Flask
import flask_restful as rest


app = Flask(__name__)
app.config.from_object('config')
api = rest.Api(app)


class GetDirections(rest.Resource):
    def get(self):
        return {'status': 'success', 'data': ""}, 200


api.add_resource(GetDirections, '/')

if __name__ == '__main__':
    app.run()
