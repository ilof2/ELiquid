from typing import List, Generator

from bson import ObjectId
from pydantic import BaseModel, PrivateAttr
from werkzeug.security import check_password_hash, generate_password_hash


class User(BaseModel):
    _uid: ObjectId = PrivateAttr(default_factory=lambda: ObjectId())
    username: str
    email: str
    password: str

    @property
    def uid(self):
        return self._uid

    @uid.setter
    def uid(self, val):
        if isinstance(val, ObjectId):
            self._uid = val

    @classmethod
    def create(cls, username: str, email: str, password: str, _id: ObjectId = ObjectId()):
        email = email.strip()
        username = username.strip()
        password = generate_password_hash(password)
        new_class = cls(username=username, email=email, password=password)
        new_class._uid = _id
        return new_class

    @classmethod
    def create_from_list(cls, users_list: List[dict]) -> Generator:
        for user in users_list:
            yield cls.create(**user)

    @staticmethod
    def check_password(pwhash: str, password):
        return check_password_hash(pwhash, password)
