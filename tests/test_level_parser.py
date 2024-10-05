import pytest
from marshmallow import ValidationError
from pytest import mark
from yaml import YAMLError

from mystics_and_manuscripts_core.data_models.level import Level
from mystics_and_manuscripts_core.data_models.path import Path
from mystics_and_manuscripts_core.data_models.place import Place
from mystics_and_manuscripts_core.internal.level_parser import yaml_to_level

valid_level_yaml1 = """
places:
    - id: a
    - id: b

paths:
    - from: a
      to: b
"""
valid_level1 = Level(
    places=[Place("a"), Place("b")],
    paths=[Path("a", "b")]
)

valid_level_yaml2 = """
paths:
    - to: room2
      from: room3
    - from: room1
      to: room3

places:
    - id: room1
    
    - id: room2
    
    - id: room3
"""
valid_level2 = Level(
    places=[Place("room1"), Place("room2"), Place("room3")],
    paths=[Path("room3", "room2"), Path("room1", "room3")]
)

invalid_level_yaml1 = """
paths:
    - to
      from:

places:
    - id: some
"""
exception1 = YAMLError

invalid_level_yaml2 = """
paths: A lot of em

places:
    - id: some
"""
exception2 = ValidationError


@mark.parametrize("level_yaml,level", [(valid_level_yaml1, valid_level1), (valid_level_yaml2, valid_level2)])
def test_yaml_to_level(level_yaml: str, level: Level):
    assert yaml_to_level(level_yaml) == level


@mark.parametrize("level_yaml,exception", [(invalid_level_yaml1, exception1), (invalid_level_yaml2, exception2)])
def test_yaml_to_level_error(level_yaml: str, exception):
    with pytest.raises(Exception) as e:
        assert isinstance(e, exception)
