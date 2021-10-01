from flask import Flask
from flask_bcrypt import Bcrypt
from database.db import initialize_db
from flask_restful import Api
from resources.routes import initialize_routes

app = Flask(__name__)
api = Api(app)
bcrypt = Bcrypt(app)

app.config['MONGODB_SETTINGS'] = {'host': 'mongodb://localhost/aic-web'}
# app.config['MONGODB_HOST'] = "mongodb+srv://eugene_ivashkevich:wpLV8ZJcC1spQoc6@aic-web.u94a7.mongodb.net/aic-web?retryWrites=true&w=majority" 

initialize_db(app)
initialize_routes(api)

app.run()
