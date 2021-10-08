from .customer import CustomersApi, CustomerApi
from .auth import SignupApi, LoginApi 


def initialize_routes(api):
    api.add_resource(CustomersApi, '/api/customers')
    api.add_resource(CustomerApi, '/api/customers/<id>')

    api.add_resource(SignupApi, '/api/auth/signup')
    api.add_resource(LoginApi, '/api/auth/login') 
