from flask import Flask
from flask_cors import CORS
from flask_pymongo import PyMongo

app = Flask(__name__)

# Load Config File for DB
app.config.from_pyfile('config.cfg')
CORS(app)

mongo = PyMongo(app)
# Select the database
db = mongo.db
# Select the collection
collection = db.users

from api import users  # workaround to circular imports
