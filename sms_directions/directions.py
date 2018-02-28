from datetime import datetime

import googlemaps

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
    send_sms(directions_result)
