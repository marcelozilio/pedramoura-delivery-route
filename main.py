from flask import Flask, request, jsonify, make_response
from flask_restful import Resource, Api
import google_api
import routestore
import validation
import maps

app = Flask(__name__)
api = Api(app)

pedramoura_location = "Rolante, RS, Brasil"


class DeliveryRoute(Resource):
    def post(self):
        enderecos = request.json['enderecos']

        validation.validate_endereco_request(enderecos)

        directions_result = google_api.create_route(pedramoura_location, enderecos)

        _id = routestore.save(jsonify(directions_result))

        maps.create_map(directions_result, _id)

        return jsonify({
            'id': str(_id),
            'route': directions_result
        })


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
api.add_resource(DeliveryRouteById, '/delivery-route/<_id>')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
