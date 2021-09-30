from flask import Flask, request, Response
from database.db import initialize_db
from database.models import Customer

app = Flask(__name__)

app.config['MONGODB_SETTINGS'] = {
    'host': 'mongodb://localhost/aic-web'
}

initialize_db(app)

@app.route('/customers')
def get_customers():
    customers = Customer.objects().to_json()
    return Response(customers, mimetype="application/json", status=200)

@app.route('/customers', methods=['POST'])
def add_customer():
    body = request.get_json() # 
    customer = Customer(**body).save()
    id = customer.id
    return {'id': str(id)}, 200

@app.route('/customers/<id>', methods=['PUT'])
def update_customer(id):
    body = request.get_json()
    Customer.objects.get(id=id).update(**body)
    return '', 200    

@app.route('/customers/<id>', methods=['DELETE'])
def delete_customer(id):
    customer = Customer.objects.get(id=id).delete()
    return '', 200

@app.route('/customers/<id>')
def get_customer(id): 
    customers = Customer.objects.get(id=id).to_json()
    return Response(customers, mimetype="application/json", status=200)

app.run()
