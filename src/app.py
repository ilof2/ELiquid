from flask import Flask

from config import Config

app = Flask(__name__)


if __name__ == "__main__":
    app.run(
        host=Config.APP_HOST,
        port=Config.APP_PORT,
        debug=Config.DEBUG
    )
