from dataclasses import dataclass

from marshmallow_dataclass import class_schema


@dataclass
class Place:
    id: str


place_schema = class_schema(Place)()