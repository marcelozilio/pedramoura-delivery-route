import googlemaps
import maps
from datetime import datetime

api_key = open('keys/googlemaps-api-key.txt')


def create_route(pedramoura_location, waypoints):
    gmaps = googlemaps.Client(key=api_key.read())

    # Converter os endereços em uma string separada por "|"
    waypoints_str = "|".join(waypoints)

    # Request directions com otimização de waypoints
    now = datetime.now()
    directions_result = gmaps.directions(origin=pedramoura_location,
                                         destination=pedramoura_location,
                                         waypoints=waypoints_str,
                                         optimize_waypoints=True,
                                         mode="driving",
                                         departure_time=now,
                                         language="pt-BR",
                                         units="metric")

    maps.create_map(directions_result)

    return directions_result
