from graphene import ObjectType, String


class UserSchema(ObjectType):
    """
    Profile Schema defining the types and relationship between Fields in your
    API.
    """
    _id = String(required=True)
    username = String(required=True)
    email = String(required=True)
