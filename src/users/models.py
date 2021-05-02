from typing import List, Generator

from bson import ObjectId
from pydantic import BaseModel, Field
from werkzeug.security import check_password_hash, generate_password_hash


class User(BaseModel):
    uid: ObjectId = Field(default_factory=lambda: ObjectId())
    username: str
    email: str
    password: str

    class Config:
        arbitrary_types_allowed = True
    
    @classmethod
    def create_from_dict(cls, *args, **kwargs) -> 'User':
        email = kwargs["email"]
        username = kwargs["username"]
        password = kwargs["password"]
        new_class = cls(username=username, email=email, password=password)
        new_class.uid = kwargs["_id"]
        return new_class

    @classmethod
    def create_new(cls, username: str, email: str, password: str, *args, **kwargs) -> 'User':
        email = email.strip().lower()
        username = username.strip()
        password = generate_password_hash(password)
        return cls(username=username, email=email, password=password)

    @classmethod
    def create_from_list(cls, users_list: List[dict]) -> Generator:
        for user in users_list:
            yield cls.create_from_dict(**user)

    @staticmethod
    def check_password(pwhash: str, password) -> bool:
        return check_password_hash(pwhash=pwhash, password=password)
