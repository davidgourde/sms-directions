from flask_script import Manager

from sms_directions.app import app

manager = Manager(app)


if __name__ == '__main__':
    manager.run()
