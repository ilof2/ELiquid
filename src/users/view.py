from graphene import String, Field, ObjectType, Schema

from .contoller import login
from .schema import UserSchema


class Query(ObjectType):
    """
    Defines the query types
    """
    login = Field(UserSchema, email=String(), password=String())

    def resolve_login(self, inf, email: str, password: str):
        """
        Login resolver
        :param inf:
        :param email: email to lookup
        :param password: password to hash against
        :return: the user fetched from mongoDB
        """
        user = login(email, password)
        if not user:
            raise Exception(
                "The profile by the email {} is not exist or password is incorrect".format(
                    email))

        return user.dict(exclude={"password", })


authentication_schema = Schema(
                            query=Query,
                            types=[UserSchema]
                        )
