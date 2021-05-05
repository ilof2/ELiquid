import graphene

from . import User
from .contoller import login, register, get_user_by_email
from .schema import UserSchema


class Query(graphene.ObjectType):
    get_user = graphene.Field(UserSchema, email=graphene.String())

    def resolve_get_user(self, inf, email):
        user: User = get_user_by_email(email)
        return UserSchema(**user.dict(exclude={"password", }))


class LoginUser(graphene.Mutation):
    class Arguments:
        email = graphene.NonNull(graphene.String)
        password = graphene.NonNull(graphene.String)

    ok = graphene.Boolean()
    user = graphene.Field(lambda: UserSchema)

    def mutate(root, info, email, password):
        user = login(email, password)
        if not user:
            raise Exception(
                "The profile by the email {} is not exist or password is incorrect".format(
                    email))
        user = UserSchema(**user.dict(exclude={"password", }))
        ok = True
        return CreateUser(user=user, ok=ok)


class CreateUser(graphene.Mutation):
    class Arguments:
        email = graphene.NonNull(graphene.String)
        username = graphene.NonNull(graphene.String)
        password = graphene.NonNull(graphene.String)

    ok = graphene.Boolean()
    user = graphene.Field(lambda: UserSchema)

    def mutate(root, info, email, username, password):
        user = register(email, username, password)
        user = UserSchema(username=user.username, email=email, uid=user.uid)
        ok = True
        return CreateUser(user=user, ok=ok)


class Mutation(graphene.ObjectType):
    create_user = CreateUser.Field()
    login = LoginUser.Field()


users_schema = graphene.Schema(
                            query=Query,
                            mutation=Mutation,
                            types=[UserSchema],
                        )
