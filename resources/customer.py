from flask import Response, request
from database.models import Customer
from flask_restful import Resource


class CustomersApi(Resource):
  def get(self):
    customers = Customer.objects().to_json()
    return Response(customers, mimetype="application/json", status=200)

  def post(self):
    body = request.get_json()
    customer = Customer(**body).save()
    id = customer.id
    return {'id': str(id)}, 200
 
class CustomerApi(Resource):
  def put(self, id):
    body = request.get_json()
    Customer.objects.get(id=id).update(**body)
    return '', 200
 
  def delete(self, id):
    customer = Customer.objects.get(id=id).delete()
    return '', 200

  def get(self, id):
    customers = Customer.objects.get(id=id).to_json()
    return Response(customers, mimetype="application/json", status=200)
