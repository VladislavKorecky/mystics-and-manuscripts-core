from yaml import safe_load

from mystics_and_manuscripts_core.data_models.level import Level, level_schema


def yaml_to_level(level_yaml: str) -> Level:
    """
    Safely load a YAML string into a Level dataclass

    Args:
        level_yaml (str): YAML to parse as a level.

    Returns:
        Level: Level dataclass with cleaned and validated data.
    """

    data = safe_load(level_yaml)
    return level_schema.load(data)


def level_to_dict(level: Level) -> dict:
    """
    Dump the level data to a dictionary (JSON).

    Args:
        level (Level): Level to convert to the dictionary.

    Returns:
        dict: Dict representation of the level.
    """

    return level_schema.dump(level)


def level_yaml_to_dict(level_yaml: str) -> dict:
    """
    Convert level YAML to its dictionary representation. Missing fields are added and the data is validated.

    Args:
        level_yaml (str): A level as YAML.

    Returns:
        dict: Dictionary representing the level with clean data.
    """

    return level_to_dict(yaml_to_level(level_yaml))
