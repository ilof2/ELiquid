from pydantic import BaseModel
from werkzeug.security import check_password_hash, generate_password_hash
from bson import ObjectId


class User(BaseModel):
    _id: ObjectId = ObjectId()
    username: str
    email: str
    password: str

    @classmethod
    def create(cls, username: str, email: str, password: str):
        email = email.strip()
        username = username.strip()
        password = generate_password_hash(password)
        return cls(username=username, email=email, password=password)

    @staticmethod
    def check_password(pwhash: str, password):
        return check_password_hash(pwhash, password)
