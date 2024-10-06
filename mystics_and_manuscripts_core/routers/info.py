from fastapi import APIRouter


info_router = APIRouter()


with open("version.txt", "r") as f:
    version = f.read()


@info_router.get("/")
def info_route():
    return {"service": "Mystics and Manuscripts CORE", "version": version}
