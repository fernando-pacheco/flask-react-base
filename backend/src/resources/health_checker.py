from flask import make_response
from flask_apispec import doc, marshal_with
from flask_apispec.views import MethodResource
from flask_restful import Resource


@doc(description='Health Checker API', tags=['Health Checker'])
class HealthCheckerResource(MethodResource, Resource):
    @marshal_with({}, code=200)
    @doc(description='Verifica se o servidor está online')
    def get(self):
        return make_response({'message': 'Service is up'}, 200)
