import flask_jwt_extended as jwt
import graphene

from . import User
from .controller import login, register, get_user_by_email, validate_unique_user
from .schema import UserSchema


class Query(graphene.ObjectType):
    get_user = graphene.Field(UserSchema, email=graphene.String())

    @jwt.jwt_required()
    def resolve_get_user(self, inf, email):
        user: User = get_user_by_email(email)
        return UserSchema(**user.dict(exclude={"password", }))


class LoginUser(graphene.Mutation):
    class Arguments:
        email = graphene.NonNull(graphene.String)
        password = graphene.NonNull(graphene.String)

    ok = graphene.Boolean()
    access_token = graphene.String()
    refresh_token = graphene.String()
    user = graphene.Field(lambda: UserSchema)

    def mutate(root, info, email, password):
        user = login(email, password)
        if not user:
            raise Exception(
                "The profile by the email {} is not exist or password is incorrect".format(
                    email))
        user = UserSchema(**user.dict(exclude={"password", }, by_alias=True))
        ok = True
        access_token = jwt.create_access_token(str(user._id))
        refresh_token = jwt.create_refresh_token(str(user._id))
        return LoginUser(user=user, ok=ok, access_token=access_token, refresh_token=refresh_token)


class RefreshMutation(graphene.Mutation):
    new_token = graphene.String()

    @jwt.jwt_required(refresh=True)
    def mutate(root):
        current_user = 1
        access_token = jwt.create_access_token(identity=current_user)
        return RefreshMutation(new_token=access_token)


class CreateUser(graphene.Mutation):
    class Arguments:
        email = graphene.NonNull(graphene.String)
        username = graphene.NonNull(graphene.String)
        password = graphene.NonNull(graphene.String)

    ok = graphene.Boolean()
    user = graphene.Field(lambda: UserSchema)

    @validate_unique_user
    def mutate(root, info, email, username, password):
        user = register(email, username, password)
        user = UserSchema(username=user.username, email=email, _id=str(user.uid))
        ok = True
        return CreateUser(user=user, ok=ok)


class Mutation(graphene.ObjectType):
    create_user = CreateUser.Field()
    login = LoginUser.Field()
    refresh_token = RefreshMutation.Field()


users_schema = graphene.Schema(
                            query=Query,
                            mutation=Mutation,
                            types=[UserSchema],
                        )
