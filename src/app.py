from flask import Flask
from flask_graphql import GraphQLView
from graphql_init import global_schema


def create_app():
    app = Flask(__name__)

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

