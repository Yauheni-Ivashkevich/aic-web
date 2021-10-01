from flask import Flask
from flask_bcrypt import Bcrypt
from database.db import initialize_db
from flask_restful import Api
from resources.routes import initialize_routes

app = Flask(__name__)
api = Api(app)
bcrypt = Bcrypt(app) 

app.config['MONGODB_SETTINGS'] = {'host': 'mongodb://localhost/aic-web'}

initialize_db(app)
initialize_routes(api)

app.run()
