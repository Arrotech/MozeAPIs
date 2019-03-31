import json

from flask import request, jsonify, make_response
from flask_jwt_extended import jwt_required
from flask_restful import Resource

from app.api.v1.models.library_model import LibraryModel


class Library(Resource):

    @jwt_required
    def post(self):
        """Add a new book."""

        details = request.get_json()

        author = details['author']
        title = details['title']
        subject = details['subject']
        book_identity = details['book_identity']

        book = LibraryModel().save(author, title, subject, book_identity)
        return make_response(jsonify({
            "message": "Book awarded successfully"
        }), 201)


class GetBooks(Resource):

    @jwt_required
    def get(self):
        """Fetch all books."""

        empty_list = {}
        books = LibraryModel().get_all_books()
        books = json.loads(books)
        if books:
            return make_response(jsonify({
                "message": "Retrieved successfully",
                "Books": books
            }), 200)
        return make_response(jsonify({
            "message": "success",
            "Books": empty_list
        }), 200)


class GetOneBook(Resource):

    @jwt_required
    def get(self, book_id):
        """Fetch a book."""

        book = LibraryModel().get_one_book(book_id)
        book = json.loads(book)
        if book:
            return make_response(jsonify({
                "message": "Retrieved successfully",
                "Book": book
            }), 200)
        return make_response(jsonify({
            "message": "Book Not Found"
        }), 404)
