from flask import Response, request
from flask_jwt_extended import jwt_required 
from database.models import Customer, User
from flask_jwt_extended import jwt_required, get_jwt_identity 
from flask_restful import Resource


class CustomersApi(Resource):
    def get(self):
        query = Customer.objects()
        customers = Customer.objects().to_json()
        return Response(customers, mimetype="application/json", status=200)

    @jwt_required 
    def post(self):
        user_id = get_jwt_identity()
        body = request.get_json()
        user = User.objects.get(id=user_id)
        customer = Customer(**body, added_by=user)
        customer.save()
        user.update(push__customers=customer) 
        user.save()
        id = customer.id
        return {'id': str(id)}, 200


class CustomerApi(Resource):
    @jwt_required
    def put(self, id):
        user_id = get_jwt_identity()
        customer = Customer.objects.get(id=id, added_by=user_id)
        body = request.get_json()
        Customer.objects.get(id=id).update(**body)
        return '', 200

    @jwt_required 
    def delete(self, id):
        user_id = get_jwt_identity()
        customer = Customer.objects.get(id=id, added_by=user_id)
        customer.delete() 
        return '', 200

    def get(self, id):
        customers = Customer.objects.get(id=id).to_json()
        return Response(customers, mimetype="application/json", status=200)
