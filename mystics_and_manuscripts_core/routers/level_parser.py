from fastapi import APIRouter, HTTPException
from marshmallow import ValidationError
from pydantic import BaseModel
from yaml import YAMLError

from mystics_and_manuscripts_core.internal.level_parser import level_yaml_to_dict


level_parser_router = APIRouter()


class ParseLevelYAMLBody(BaseModel):
    level_yaml: str


@level_parser_router.post("/level-yaml-to-dict")
def level_yaml_to_dict_route(body: ParseLevelYAMLBody):
    try:
        result = level_yaml_to_dict(body.level_yaml)
    except YAMLError:
        raise HTTPException(status_code=400, detail="Not valid YAML.")
    except ValidationError:
        raise HTTPException(status_code=400, detail="Not a valid level.")

    return result
