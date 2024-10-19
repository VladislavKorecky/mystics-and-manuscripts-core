from fastapi import APIRouter, HTTPException
from marshmallow import ValidationError
from pydantic import BaseModel
from yaml import YAMLError

from mystics_and_manuscripts_core.internal.level_parser import level_yaml_to_validated_dict, \
    level_dict_to_validated_yaml, validate_level_dict, validate_level_yaml

level_parser_router = APIRouter()


class LevelDictBody(BaseModel):
    level_dict: dict


class LevelYAMLBody(BaseModel):
    level_yaml: str


@level_parser_router.post("/level-dict-to-validated-yaml")
def level_dict_to_validated_yaml_route(body: LevelDictBody) -> dict:
    try:
        result = level_dict_to_validated_yaml(body.level_dict)
    except ValidationError:
        raise HTTPException(status_code=400, detail="Not a valid level.")

    return {"level_yaml": result}


@level_parser_router.post("/level-yaml-to-validated-dict")
def level_yaml_to_validated_dict_route(body: LevelYAMLBody) -> dict:
    try:
        result = level_yaml_to_validated_dict(body.level_yaml)
    except YAMLError:
        raise HTTPException(status_code=400, detail="Not valid YAML.")
    except ValidationError:
        raise HTTPException(status_code=400, detail="Not a valid level.")

    return {"level_dict": result}


@level_parser_router.post("/validate-level-dict")
def validate_level_dict_route(body: LevelDictBody) -> dict:
    try:
        result = validate_level_dict(body.level_dict)
    except ValidationError:
        raise HTTPException(status_code=400, detail="Not a valid level.")

    return {"level_dict": result}


@level_parser_router.post("/validate-level-yaml")
def validate_level_yaml_route(body: LevelYAMLBody) -> dict:
    try:
        result = validate_level_yaml(body.level_yaml)
    except YAMLError:
        raise HTTPException(status_code=400, detail="Not valid YAML.")
    except ValidationError:
        raise HTTPException(status_code=400, detail="Not a valid level.")

    return {"level_yaml": result}
