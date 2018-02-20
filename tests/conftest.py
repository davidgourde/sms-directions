import pytest

from sms_directions import config

@pytest.fixture(autouse=True)
def set_env_config():
    config.SMS_SENDER_NUMBER = '1'
    config.TEST_NUMBER = '2'
