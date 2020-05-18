from flask import Blueprint
from flask import Blueprint, jsonify, request, render_template

users = Blueprint("users", __name__)

@users.route("/users")
def username():
    return render_template("users.html", message='Here are some users', users=users)