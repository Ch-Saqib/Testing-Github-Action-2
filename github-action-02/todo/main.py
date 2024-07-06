# from typing import Annotated, AsyncGenerator
# from fastapi import FastAPI, Depends
# from todo.models import *
# from todo.database import *
# from contextlib import asynccontextmanager
# from todo.router import *

# @asynccontextmanager
# async def lifespan(app: FastAPI) -> AsyncGenerator:
#     create_tables()
#     yield


# app: FastAPI = FastAPI(
#     title="Todo App",
#     description="A simple todo app ",
#     version="0.1.0",
#     lifespan=lifespan,
# )

# app.include_router(router,prefix="/todo",tags=["todo"])

# app.include_router(product_router, prefix="/product", tags=["product"])
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {
        "Hello": "World",
        "World2": "Pakistan Zindabad",
        "Testing-Zone": "I Am From Testing Zone.",
    }
