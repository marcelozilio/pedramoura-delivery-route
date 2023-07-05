from flask import Flask, request, jsonify
from flask_restful import Resource, Api
import google_api
import routestore


app = Flask(__name__)
api = Api(app)


class DeliveryRoute(Resource):
    def post(self):
        origin = "Rolante, RS, 95690-000, Brasil"
        destination = "Rolante, RS, 95690-000, Brasil"

        # Lista de endereços
        waypoints = ["R. Ouro Preto, 408 - Jardim Floresta, Porto Alegre - RS, 91040-610, Brasil",
                     "Av. Assis Brasil, 2611 - Cristo Redentor, Porto Alegre - RS, 91010-006, Brasil",
                     "Av. Guilherme Schell, 6750 - Centro, Canoas - RS, 92310-564, Brasil"]

        directions = google_api.create_route(origin, destination, waypoints)

        # converte retorno da api para json
        route_info = jsonify(directions)

        # Salvar no banco de dados
        routestore.save(route_info)

        return route_info


class DeliveryRouteById(Resource):
    def delete(self, id):
        # Deletar do banco de dados
        jsonify("implement this method")

    def get(self, id):
        # Pegar no banco de dados
        return jsonify("implement this method")


api.add_resource(DeliveryRoute, '/delivery-route')
api.add_resource(DeliveryRouteById, '/delivery-route/<id>')

if __name__ == '__main__':
    app.run()