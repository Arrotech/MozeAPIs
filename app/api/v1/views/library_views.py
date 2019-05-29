import json

from flask import request, jsonify, make_response
from flask_jwt_extended import jwt_required
from flask_restful import Resource

from app.api.v1.models.library_model import LibraryModel


class Library(Resource):
    """The library."""

    @jwt_required
    def post(self):
        """Add a new book."""
        details = request.get_json()
        admission_no = details['admission_no']
        author = details['author']
        title = details['title']
        subject = details['subject']

        book = LibraryModel().save(admission_no,
                                   author,
                                   title,
                                   subject)
        book = json.loads(book)
        return make_response(jsonify({
            "status": "201",
            "message": "Book awarded successfully",
            "book": book
        }), 201)

    @jwt_required
    def get(self):
        """Fetch all books."""
        return make_response(jsonify({
            "status": "200",
            "message": "Retrieved successfully",
            "books": json.loads(LibraryModel().get_all_books())
        }), 200)


class GetOneBook(Resource):
    """Book."""

    @jwt_required
    def get(self, admission_no):
        """Fetch a book."""
        book = LibraryModel().get_admission_no(admission_no)
        book = json.loads(book)
        if book:
            return make_response(jsonify({
                "status": "200",
                "message": "Retrieved successfully",
                "Book": book
            }), 200)
        return make_response(jsonify({
            "status": "404",
            "message": "Book Not Found"
        }), 404)
