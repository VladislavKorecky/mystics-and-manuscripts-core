from fastapi import FastAPI

from mystics_and_manuscripts_core.routers.info import info_router
from mystics_and_manuscripts_core.routers.level_parser import level_parser_router

app = FastAPI()
app.include_router(info_router)
app.include_router(level_parser_router)
