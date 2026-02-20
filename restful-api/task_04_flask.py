#!/usr/bin/python3
"""Basic Flask REST API.

This module defines a small Flask application exposing endpoints to:
- Get a welcome message
- Check API status
- List all usernames
- Retrieve a user by username
- Add a new user
"""

from flask import Flask, jsonify, request

app = Flask(__name__)

user_data = {

}


@app.route("/")
def home():
    """Return a welcome message for the API."""
    return "Welcome to the Flask API!", 200


@app.route("/data", methods=["GET"])
def get_all_user():
    """Return a JSON list of all usernames."""
    names = [user["username"] for user in user_data.values()]
    return jsonify(names), 200


@app.route("/status", methods=["GET"])
def status():
    """Return the API status."""
    return "OK", 200


@app.route("/users/<username>", methods=["GET"])
def get_user(username):
    """Return user data for a given username.

    Args:
        username (str): The username used as a key in the users store.

    Returns:
        flask.Response: JSON user object if found, otherwise an error message.
    """
    user_info = user_data.get(username)
    if user_info:
        return jsonify(user_info), 200
    else:
        return jsonify({"error": "User not found"}), 404


@app.route("/add_user", methods=["POST"])
def add_user():
    """Create a new user from a JSON request body.

    Expected JSON keys:
        - username (required)
        - name (optional)
        - age (optional)
        - city (optional)

    Returns:
        flask.Response: Confirmation message and created user data.
    """
    new_user = request.get_json()
    if not new_user:
        return jsonify(error="Invalid JSON"), 400
    if "username" not in new_user:
        return jsonify({"error": "Username is required"}), 400
    if new_user["username"] in user_data:
        return jsonify({"error": "Username already exists"}), 409
    username = new_user["username"]
    user_data[username] = {
        "username": username,
        "name": new_user.get("name", ""),
        "age": new_user.get("age", ""),
        "city": new_user.get("city", "")
    }
    return jsonify(message="User added", user=user_data[username]), 201


if __name__ == "__main__":
    app.run()
