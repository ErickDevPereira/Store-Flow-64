from .endpoint_entity import EndpointsEntity
from flask import Response
from flask_restful import Resource

class EndpointsCategories(Resource, EndpointsEntity):

    def get(self) -> Response:
        pass

    def post(self) -> Response:
        pass

    def delete(self) -> Response:
        pass

    def patch(self) -> Response:
        pass