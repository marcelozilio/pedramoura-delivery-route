from flask import Flask, request, jsonify, make_response
from flask_restful import Resource, Api
import google_api
import routestore
import validation

app = Flask(__name__)
api = Api(app)

pedramoura_location = "Rolante, RS, 95690-000, Brasil"


class DeliveryRoute(Resource):
    def post(self):
        enderecos = request.json['enderecos']

        validation.validate_endereco_request(enderecos)

        directions = google_api.create_route(pedramoura_location, enderecos)
        route_info = jsonify(directions)

        routestore.save(route_info)

        return route_info


class DeliveryRouteById(Resource):
    def delete(self, _id):
        response = make_response(routestore.delete(_id))
        response.headers['Content-Type'] = 'application/json'
        return response

    def get(self, _id):
        response = make_response(routestore.get_by_id(_id))
        response.headers['Content-Type'] = 'application/json'
        return response


api.add_resource(DeliveryRoute, '/delivery-route')
api.add_resource(DeliveryRouteById, '/delivery-route/<id>')

if __name__ == '__main__':
    app.run()