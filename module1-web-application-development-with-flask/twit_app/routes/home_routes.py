# web_app/routes/home_routes.py

from flask import Blueprint

home_routes = Blueprint("home_routes", __name__)

@home_routes.route("/tweets")
def tweet():
    return f"@ElonMusk: 'Tesla is awesome!'"

@home_routes.route("/user")
def user():
    return "@ElonMusk, @KanyeWest"