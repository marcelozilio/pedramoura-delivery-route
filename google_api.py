import googlemaps
from datetime import datetime

api_key = 'chave-de-acesso'


def create_route(origin, destination, waypoints):
    if len(waypoints) > 10:
        raise ValueError("A lista de waypoints deve conter no máximo 10 itens.")

    gmaps = googlemaps.Client(key=api_key)

    # Converter os endereços em uma string separada por "|"
    waypoints_str = "|".join(waypoints)

    # Request directions com otimização de waypoints
    now = datetime.now()
    directions_result = gmaps.directions(origin=origin,
                                         destination=destination,
                                         waypoints=waypoints_str,
                                         optimize_waypoints=True,
                                         mode="driving",
                                         departure_time=now,
                                         language="pt-BR",
                                         units="metric")

    return directions_result
