from os import environ, path
from dotenv import load_dotenv

base_dir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(base_dir, "../.env"))


class Config:
    DEBUG = environ.get("DEBUG", True)
    APP_HOST = environ.get("APP_HOST", "localhost")
    APP_PORT = environ.get("APP_PORT", 5000)
    MONGO_DB_USER = environ.get("MONGO_DB_USER")
    MONGO_DB_PASSWORD = environ.get("MONGO_DB_PASSWORD")
    MONGO_DB_NAME = environ.get("MONGO_DB_NAME", "test")
    MONGO_DB_PORT = environ.get("MONGO_DB_PORT", 27017)
    MONGO_DB_HOST = environ.get("MONGO_DB_HOST", "localhost")
    MONGO_DB_URI = environ.get(
        "MONGO_URI",
        f"mongodb://{MONGO_DB_USER}:{MONGO_DB_PASSWORD}@{MONGO_DB_HOST}:{MONGO_DB_PORT}/{MONGO_DB_NAME}?authSource=admin",
    )
    TEST_MONGO_DB_NAME = "testdb"
    TEST_MONGO_URI = f"mongodb://{MONGO_DB_USER}:{MONGO_DB_PASSWORD}@{MONGO_DB_HOST}:{MONGO_DB_PORT}/{TEST_MONGO_DB_NAME}?authSource=admin"
