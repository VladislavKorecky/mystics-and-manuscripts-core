from fastapi import APIRouter, HTTPException
from marshmallow import ValidationError
from pydantic import BaseModel

from mystics_and_manuscripts_core.internal.level_parser import validate_level_dict

level_parser_router = APIRouter()


class LevelDictBody(BaseModel):
    level_dict: dict


@level_parser_router.post("/validate-level-dict")
def validate_level_dict_route(body: LevelDictBody) -> dict:
    try:
        result = validate_level_dict(body.level_dict)
    except ValidationError:
        raise HTTPException(status_code=400, detail="Not a valid level.")

    return {"level_dict": result}
