import folium


def create_map(directions_result, _id):
    # Obtendo as coordenadas da rota
    route = directions_result[0]['legs'][0]['steps']
    route_coordinates = [(step['start_location']['lat'], step['start_location']['lng']) for step in route]
    route_coordinates.append((route[-1]['end_location']['lat'], route[-1]['end_location']['lng']))

    # Criando um mapa com folium
    map = folium.Map(location=route_coordinates[0], zoom_start=10)

    # Adicionando a linha da rota ao mapa
    folium.PolyLine(route_coordinates, color='blue', weight=2.5, opacity=1).add_to(map)

    # Salvando o mapa em um arquivo HTML
    map.save('maps/map-delivery-route-' + str(_id) + '.html')

