from flask import Flask, request, jsonify
from flask_restful import Resource, Api


app = Flask(__name__)
api = Api(app)


class DeliveryRoute(Resource):
    def get(self):
        return jsonify("implement this method")

    def post(self):
        return jsonify("implement this method")

    def put(self):
        return jsonify("implement this method")


class DeliveryRouteById(Resource):
    def delete(self, id):
        jsonify("implement this method")

    def get(self, id):
        return jsonify("implement this method")


api.add_resource(DeliveryRoute, '/delivery-route')
api.add_resource(DeliveryRouteById, '/delivery-route/<id>')

if __name__ == '__main__':
    app.run()