from flask import Flask
from flask_graphql import GraphQLView
from flask_jwt_extended import JWTManager

from config import Config
from graphql_init import global_schema


auth = JWTManager()


def create_app():
    app = Flask(__name__)
    app.config_class = Config
    app.config['JWT_SECRET_KEY'] = Config.JWT_SECRET_KEY
    auth.init_app(app)

    @app.route("/health")
    def health():
        return "Healthy!"

    return app


app = create_app()
app.add_url_rule(
    "/graphql",
    view_func=GraphQLView.as_view(
        "graphql",
        schema=global_schema,
        graphiql=True,
    )
)
