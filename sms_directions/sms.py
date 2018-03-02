import nexmo

from sms_directions import config

client = nexmo.Client(key=config.NEXMO_API_KEY, secret=config.NEXMO_API_SECRET)


def send_sms(directions, number):
    client.send_message({'from': config.SMS_SENDER_NUMBER,
                         'to': number,
                         'text': directions})
