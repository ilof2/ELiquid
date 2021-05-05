import graphene
from users import UserMutation, UserSchema, UserQuery


class GlobalMutation(UserMutation, ):
    pass


class GlobalQuery(UserQuery, ):
    pass


global_schema = graphene.Schema(
    query=GlobalQuery,
    mutation=GlobalMutation,
    types=[UserSchema],
)

