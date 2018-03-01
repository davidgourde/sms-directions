from datetime import datetime

import googlemaps
from bs4 import BeautifulSoup

from sms_directions.config import GOOGLE_MAPS_DIRECTIONS_API_KEY
from sms_directions.sms import send_sms


gmaps = googlemaps.Client(key=GOOGLE_MAPS_DIRECTIONS_API_KEY) if GOOGLE_MAPS_DIRECTIONS_API_KEY else None


def get_directions(origin, destination, mode):
    if not gmaps:
        return
    now = datetime.now()
    directions_result = gmaps.directions(origin=origin,
                                         destination=destination,
                                         mode=mode,
                                         departure_time=now,
                                         language='fr')

    try:
        result = ""
        i = 1
        leg = directions_result[0]['legs'][0]
        result += 'Départ: ' + leg['start_address'] + '\n'
        result += 'Arrivée: ' + leg['end_address'] + '\n\n'

        for step in leg['steps']:
            html_instructions = step['html_instructions']
            soup = BeautifulSoup(html_instructions, "html.parser")
            instructions = soup.get_text()
            result += "{}. {}".format(i, instructions) + '\n\n'
            i = i + 1

        send_sms(result)
    except Exception as e:
        print(e)
        send_sms('Oups désolé, bug!\n\n' + str(e))
