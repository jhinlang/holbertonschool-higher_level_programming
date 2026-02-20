#!/usr/bin/python3
"""Flask API with JWT Authentication and Basic Security."""

from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import (
    JWTManager,
    create_access_token,
    get_jwt_identity,
    jwt_required,
)
from werkzeug.security import check_password_hash, generate_password_hash

app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = "super-super-secret"
jwt = JWTManager(app)
auth = HTTPBasicAuth()

users = dict()


@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    """Handle missing or invalid token."""
    return jsonify({"error": "Missing or invalid token"}), 401


@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    """Handle invalid token errors."""
    return jsonify({"error": "Invalid token"}), 401


@jwt.expired_token_loader
def handle_expired_token_error(err):
    """Handle expired token errors."""
    return jsonify({"error": "Token has expired"}), 401


@jwt.revoked_token_loader
def handle_revoked_token_error(err):
    """Handle revoked token errors."""
    return jsonify({"error": "Token has been revoked"}), 401


@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(err):
    """Handle fresh token requirement errors."""
    return jsonify({"error": "Fresh token required"}), 401


@auth.verify_password
def verify_password(username, password):
    if username in users and check_password_hash(users[username]["password"], password):
        return username


@app.route("/login", methods=["POST"])
def login():
    """Authenticate user and return JWT access token."""
    username = request.json.get("username", None)
    password = request.json.get("password", None)

    if username not in users or not check_password_hash(
        users[username]["password"], password
    ):
        return jsonify({"msg": "Bad username or password"}), 401

    access_token = create_access_token(identity=username)
    return jsonify(access_token=access_token)


@app.route("/basic-protected", methods=["GET"])
@auth.login_required
def basic_protected():
    return "Basic Auth: Access Granted", 200


@app.route("/jwt-protected", methods=["GET"])
@jwt_required()
def jwt_protected():
    """Protected endpoint requiring valid JWT."""
    return "JWT Auth: Access Granted", 200


@app.route("/admin-only", methods=["GET"])
@jwt_required()
def admin_only():
    """Admin-only endpoint requiring JWT and admin role."""
    current_user = get_jwt_identity()

    if users[current_user]["role"] == "admin":
        return "Admin Access: Granted", 200

    return jsonify({"error": "Admin access required"}), 403


if __name__ == "__main__":
    users["user1"] = {
        "username": "user1",
        "password": generate_password_hash("password"),
        "role": "user",
    }
    users["admin1"] = {
        "username": "admin1",
        "password": generate_password_hash("password"),
        "role": "admin",
    }
    app.run(host="0.0.0.0")
