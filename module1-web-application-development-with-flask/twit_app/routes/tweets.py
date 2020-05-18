from flask import Blueprint
from flask import Blueprint, jsonify, request, render_template

tweets = Blueprint("tweets", __name__)

@tweets.route("/tweets")
def twitter():
    # books = [
    #     {"id": 1, "title": "Book 1"},
    #     {"id": 2, "title": "Book 2"},
    #     {"id": 3, "title": "Book 3"},
    # ]
    return render_template("tweets.html", message='Here are some tweets', tweets=tweets)

#     @book_routes.route("/books")
# def list_books_for_humans():
#     books = [
#         {"id": 1, "title": "Book 1"},
#         {"id": 2, "title": "Book 2"},
#         {"id": 3, "title": "Book 3"},
#     ]
#     return render_template("books.html", message="Here's some books", books=books)