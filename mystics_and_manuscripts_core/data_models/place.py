from dataclasses import dataclass, field

from marshmallow_dataclass import class_schema


@dataclass
class Place:
    id: str = field(metadata=dict(required=True))


place_schema = class_schema(Place)()