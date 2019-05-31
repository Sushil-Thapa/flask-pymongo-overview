"""This module will serve the api request."""

import json
from bson.json_util import dumps
from flask import Flask, abort, request, jsonify
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

@app.route("/")
def get_initial_response():
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


@app.route("/api/v1/users", methods=['POST'])
def create_user():
    """
       Function to create new users.
       """
    try:
        # Create new users
        try:
            body = request.get_json()
        except:
            # Bad request as request body is not available
            return abort(400)

        record_id = collection.insert(body)
        return jsonify({"message":"Successfully Created the resource."}), 201

    except:
        # Error while trying to create the resource
        return "Error while trying to create the resource", 500


@app.route("/api/v1/users", methods=['GET'])
def fetch_users():
    """
       Function to fetch the users.
       """
    try:
        # Check if dictionary is not empty
        if query_params:

            # Try to convert the value to int
            query = {k: int(v) if isinstance(v, str) and v.isdigit() else v for k, v in query_params.items()}

            # Fetch all the record(s)
            records_fetched = collection.find(query)

            # Check if the records are found
            if records_fetched.count() > 0:
                # Prepare the response
                return dumps(records_fetched)
            else:
                # No records are found
                return "", 404

        # If dictionary is empty
        else:
            # Return all the records as query string parameters are not available
            if collection.find().count > 0:
                # Prepare response if the users are found
                return dumps(collection.find())
            else:
                # Return empty array if no users are found
                return jsonify([])
    except:
        # Error while trying to fetch the resource
        # Add message for debugging purpose
        return "", 500


@app.route("/api/v1/users/<user_id>", methods=['POST'])
def update_user(user_id):
    """
       Function to update the user.
       """
    try:
        # Get the value which needs to be updated
        try:
            body = ast.literal_eval(json.dumps(request.get_json()))
        except:
            # Bad request as the request body is not available
            # Add message for debugging purpose
            return "", 400

        # Updating the user
        records_updated = collection.update_one({"id": int(user_id)}, body)

        # Check if resource is updated
        if records_updated.modified_count > 0:
            # Prepare the response as resource is updated successfully
            return "", 200
        else:
            # Bad request as the resource is not available to update
            # Add message for debugging purpose
            return "", 404
    except:
        # Error while trying to update the resource
        # Add message for debugging purpose
        return "", 500


@app.route("/api/v1/users/<user_id>", methods=['DELETE'])
def remove_user(user_id):
    """
       Function to remove the user.
       """
    try:
        # Delete the user
        delete_user = collection.delete_one({"id": int(user_id)})

        if delete_user.deleted_count > 0 :
            # Prepare the response
            return "", 204
        else:
            # Resource Not found
            return "", 404
    except:
        # Error while trying to delete the resource
        # Add message for debugging purpose
        return "", 500


@app.errorhandler(404)
def page_not_found(e):
    """Send message to the user with notFound 404 status."""
    # Message to the user
    message = {
        "err":
            {
                "msg": "This route is currently not supported. Please refer API documentation."
            }
    }
    # Making the message looks good
    resp = jsonify(message)
    # Sending OK response
    resp.status_code = 404
    # Returning the object
    return resp