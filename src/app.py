from flask import Flask
from flask_pymongo import PyMongo
from config import Config

app = Flask(__name__)
mongodb_client = PyMongo(app, uri=Config.MONGO_URI)
db = mongodb_client.db


@app.route("/health")
def health():
    return "Healthy!"


if __name__ == "__main__":
    app.run(
        host=Config.APP_HOST,
        port=Config.APP_PORT,
        debug=Config.DEBUG
    )
