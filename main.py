from fastapi import FastAPI
from strawberry import Schema
from strawberry.asgi import GraphQL

from configs.Environment import get_environment_variables
from metadata.Tags import Tags
from models.BaseModel import init
from routers.v1.AuthorRouter import AuthorRouter
from routers.v1.BookRouter import BookRouter
from schemas.graphql.Query import Query

# Application Environment Configuration
env = get_environment_variables()

# Core Application Instance
app = FastAPI(
    title=env.APP_NAME,
    version=env.API_VERSION,
    openapi_tags=Tags,
)

# Add Routers
app.include_router(AuthorRouter)
app.include_router(BookRouter)

# GraphQL Application Instance
graphql = GraphQL(Schema(query=Query))

# Integrate GraphQL Application to the Core one
app.add_route("/graphql", graphql)
app.add_websocket_route("/graphql", graphql)

# Initialise Data Model Attributes
init()
