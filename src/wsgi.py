from app import app
from config import Config


if __name__ == "__main__":
    app.run(
        host=Config.APP_HOST,
        port=Config.APP_PORT,
        debug=Config.DEBUG
    )
