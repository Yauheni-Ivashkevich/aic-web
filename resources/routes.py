from .customer import CustomersApi, CustomerApi


def initialize_routes(api):
    api.add_resource(CustomersApi, '/api/customers')
    api.add_resource(CustomerApi, '/api/customers/<id>')
