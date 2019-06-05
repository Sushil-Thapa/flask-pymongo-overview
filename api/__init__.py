from flask import Flask, jsonify
from flask_cors import CORS
from flask_pymongo import PyMongo

# Create Flask application
app = Flask(__name__)

# Load Config File for DB
app.config.from_pyfile('config.cfg')
CORS(app)

mongo = PyMongo(app)
# Select the database
db = mongo.db
# Select the collection
collection = db.users

@app.route("/")
@app.route("/index")  # Decorators as callbacks for requests
def index():
    """Welcome message for the API."""
    # Message to the user
    message = {
        'api_version': 'v1.0',
        'status': '200',
        'message': 'Welcome to the Flask API'
    }
    # Making the message looks good
    resp = jsonify(message)

    # Returning the object
    return resp

from api import users  # workaround to circular imports
