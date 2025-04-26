#pip install Flask Flask-RESTful waitress
from flask import Flask
from flask_restful import Resource, Api
from waitress import serve

app = Flask(__name__)
api = Api(app)

class Film(Resource):
    def get(self):
        film_data = {
            "title": "Inception",
            "director": "Christopher Nolan",
            "year": 2010,
            "genre": "Science Fiction"
        }
        return film_data, 200

api.add_resource(Film, '/film')

if __name__ == '__main__':
    #app.run(debug=True)
    serve(app, host='127.0.0.1', port=5001, threads=4)