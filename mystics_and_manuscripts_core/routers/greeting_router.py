from fastapi import APIRouter

from mystics_and_manuscripts_core.internal.greetings import say_hello

greeting_router = APIRouter()


@greeting_router.get("/hello-world")
def hello_world():
    return {"message": say_hello()}
