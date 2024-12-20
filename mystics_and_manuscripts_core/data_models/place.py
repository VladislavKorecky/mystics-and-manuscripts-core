from dataclasses import dataclass, field

from marshmallow_dataclass import class_schema


@dataclass
class Place:
    id: str

    name: str = field(default="Unknown place")
    description: str = field(default="")


place_schema = class_schema(Place)()