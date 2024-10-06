from dataclasses import dataclass, field

from marshmallow_dataclass import class_schema

from mystics_and_manuscripts_core.data_models.path import Path
from mystics_and_manuscripts_core.data_models.place import Place


@dataclass
class Level:
    places: list[Place]
    paths: list[Path]

    name: str = field(default="Unnamed level")
    description: str | None = field(default=None)
    introduction: str | None = field(default=None)


level_schema = class_schema(Level)()