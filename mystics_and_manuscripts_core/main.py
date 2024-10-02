from fastapi import FastAPI

from mystics_and_manuscripts_core.routers.greeting_router import greeting_router

app = FastAPI()
app.include_router(greeting_router)
