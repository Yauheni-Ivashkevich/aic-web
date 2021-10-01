from flask import Flask
from database.db import initialize_db
from flask_restful import Api
from resources.routes import initialize_routes

app = Flask(__name__)
api = Api(app)

app.config['MONGODB_SETTINGS'] = {'host': 'mongodb://localhost/aic-web'}

initialize_db(app)
initialize_routes(api)

app.run()
