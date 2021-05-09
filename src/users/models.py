from typing import List, Generator

from bson import ObjectId
from pydantic import BaseModel, Field
from werkzeug.security import check_password_hash, generate_password_hash


class User(BaseModel):
    uid: ObjectId = Field(None, alias="_id")
    username: str
    email: str
    password: str

    class Config:
        arbitrary_types_allowed = True

    @classmethod
    def create_from_dict_db(cls, **kwargs) -> 'User':
        new_class = cls(**kwargs)
        return new_class

    @classmethod
    def create_new(cls, username: str, email: str, password: str) -> 'User':
        email = email.strip().lower()
        username = username.strip()
        password = generate_password_hash(password)
        return cls(username=username, email=email, password=password)

    @classmethod
    def create_from_list(cls, users_list: List[dict]) -> Generator:
        for user in users_list:
            yield cls.create_from_dict_db(**user)

    @staticmethod
    def check_password(pwhash: str, password) -> bool:
        return check_password_hash(pwhash=pwhash, password=password)
