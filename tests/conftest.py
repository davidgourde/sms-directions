import pytest

from sms_directions import config
from sms_directions.app import init_app

@pytest.fixture(autouse=True)
def set_env_config():
    config.SMS_SENDER_NUMBER = '1'


@pytest.fixture
def app():
    app = init_app()
    app.debug = True
    return app
