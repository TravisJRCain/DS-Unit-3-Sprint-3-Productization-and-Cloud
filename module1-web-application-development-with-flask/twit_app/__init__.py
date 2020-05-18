from flask import Flask

from twit_app.routes.home_routes import home_routes
from twit_app.routes.book_routes import book_routes
from twit_app.routes.tweets import tweets
from twit_app.routes.users import users

def create_app():
    app = Flask(__name__)
    app.register_blueprint(home_routes)
    app.register_blueprint(book_routes)
    app.register_blueprint(tweets)
    app.register_blueprint(users)
    return app

if __name__ == "__main__":
    my_app = create_app()
    my_app.run(debug=True)