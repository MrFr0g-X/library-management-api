from flask import Flask, request, jsonify
import json, os

app = Flask(__name__)

DATA_FILE = 'books_data.json'

if not os.path.exists(DATA_FILE):
    with open(DATA_FILE, 'w') as f:
        json.dump([], f)  # Writes an empty JSON array into the file


def load_books():
    with open(DATA_FILE, 'r') as f:
        return json.load(f)

def save_books(books):
    with open(DATA_FILE, 'w') as f:
        json.dump(books, f, indent=4)

# GET /books - list all
@app.route('/books', methods=['GET'])
def list_books():
    return jsonify(load_books()), 200

# POST /books - add book
@app.route('/books', methods=['POST'])
def add_book():
    data = request.get_json()
    required = ['title','author','published_year','isbn']
    for field in required:
        if field not in data:
            return jsonify({"error": f"{field} is required"}), 400
    books = load_books()
    if any(b['isbn'] == data['isbn'] for b in books):
        return jsonify({"error": "ISBN already exists"}), 400
    new_book = {
        "title": data['title'],
        "author": data['author'],
        "published_year": data['published_year'],
        "isbn": data['isbn'],
        "genre": data.get('genre')
    }
    books.append(new_book)
    save_books(books)
    return jsonify(new_book), 201

@app.route('/health')
def health_check():
    return 'OK', 200

# GET /books/search - search books by author, year, genre
@app.route('/books/search', methods=['GET'])
def search_books():
    author = request.args.get('author')
    year = request.args.get('year')
    genre = request.args.get('genre')
    books = load_books()
    filtered = books
    if author:
        filtered = [b for b in filtered if b['author'].lower()==author.lower()]
    if year:
        filtered = [b for b in filtered if str(b['published_year'])==str(year)]
    if genre:
        filtered = [b for b in filtered if b.get('genre','').lower()==genre.lower()]
    return jsonify(filtered), 200

# DELETE /books/<isbn> - delete by ISBN
@app.route('/books/<isbn>', methods=['DELETE'])
def delete_book(isbn):
    books = load_books()
    new_books = [b for b in books if b['isbn']!=isbn]
    if len(new_books)==len(books):
        return jsonify({"error":"Book not found"}),404
    save_books(new_books)
    return jsonify({"message":"Book deleted"}),200

# PUT /books/<isbn> - update book
@app.route('/books/<isbn>', methods=['PUT','PATCH'])
def update_book(isbn):
    data = request.get_json()
    books = load_books()
    for b in books:
        if b['isbn']==isbn:
            b['title'] = data.get('title', b['title'])
            b['author'] = data.get('author', b['author'])
            b['published_year'] = data.get('published_year', b['published_year'])
            b['genre'] = data.get('genre', b.get('genre'))
            save_books(books)
            return jsonify(b),200
    return jsonify({"error":"Book not found"}),404

# Swagger Setup
from flask_swagger_ui import get_swaggerui_blueprint
from flask import send_from_directory

@app.route('/swagger/swagger.yaml')
def swagger_file():
    return send_from_directory('swagger', 'swagger.yaml')

SWAGGER_URL = '/api-docs'
API_URL = '/swagger/swagger.yaml'  # This matches the new route

swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={'app_name': "Library Management API"}
)
app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
