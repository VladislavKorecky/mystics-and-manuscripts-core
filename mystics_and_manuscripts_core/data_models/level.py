from dataclasses import dataclass, field

from marshmallow_dataclass import class_schema

from mystics_and_manuscripts_core.data_models.path import Path
from mystics_and_manuscripts_core.data_models.place import Place


@dataclass
class Level:
    places: list[Place] = field(metadata=dict(required=True))
    paths: list[Path] = field(metadata=dict(required=True))


level_schema = class_schema(Level)()