from flask import Blueprint, render_template, jsonify, request, abort
from sqlalchemy.orm.exc import NoResultFound

from config import (
    Session,
)


from models.models import Book

query = Blueprint('query', __name__)

#Development tool to remove models from the database
@query.route('/query', methods=['POST'])
def query_book():
    j = request.get_json()
    if 'title' not in j or 'author' not in j:
        abort(400)
    title = j['title']
    auth = j['author']
    session = Session()
    b = session.query(Book).filter(Book.title == title and Book.author == auth).all()
    if len(b) > 0:
        return jsonify({'exists': True})
    return jsonify({'exists': False})

@query.route('/add', methods=['POST'])
def add_book():
    j = request.get_json()
    if 'title' not in j or 'author' not in j or 'owner' not in j:
        abort(400)
    title = j['title']
    author = j['author']
    owner = j['owner']
    session = Session()
    b = Book(title=title, author=author, owner_id=owner)
    session.add(b)
    session.commit()
    return jsonify({'success': True})
