from flask import Flask
from flask_pymongo import PyMongo
from config import Config


def create_app():
    app = Flask(__name__)

    @app.route("/health")
    def health():
        return "Healthy!"

    return app


app = create_app()
mongodb_client = PyMongo(app, uri=Config.MONGO_URI)
db = mongodb_client.db

