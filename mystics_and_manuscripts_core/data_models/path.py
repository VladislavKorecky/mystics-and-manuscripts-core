from dataclasses import dataclass, field

from marshmallow_dataclass import class_schema


@dataclass
class Path:
    from_id: str = field(metadata=dict(data_key="from"))
    to_id: str = field(metadata=dict(data_key="to"))


path_schema = class_schema(Path)()