from flask import Flask
import flask_restful as rest

from sms_directions.sms import send_sms


app = Flask(__name__)
app.config.from_object('config')
api = rest.Api(app)


class GetDirections(rest.Resource):
    def get(self):
        return send_sms("Hello World"), 200


api.add_resource(GetDirections, '/')

if __name__ == '__main__':
    app.run()
