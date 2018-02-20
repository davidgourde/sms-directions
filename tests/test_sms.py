import mock

from sms_directions.sms import send_sms
from sms_directions import config


def test_send_sms():
    with mock.patch('sms_directions.sms.client.send_message') as mocked_send_sms:
        send_sms('expected')
    mocked_send_sms.assert_called_with({'from': config.SMS_SENDER_NUMBER,
                                        'to': config.TEST_NUMBER,
                                        'text': 'expected'})
