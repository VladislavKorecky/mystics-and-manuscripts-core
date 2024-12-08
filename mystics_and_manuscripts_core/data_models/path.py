from dataclasses import dataclass, field

from marshmallow_dataclass import class_schema


@dataclass
class Path:
    from_id: str = field(metadata=dict(data_key="from"))
    to_id: str = field(metadata=dict(data_key="to"))

    name: str = field(default="Unnamed path")
    description: str = field(default="")


path_schema = class_schema(Path)()