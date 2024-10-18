from yaml import safe_load, dump

from mystics_and_manuscripts_core.data_models.level import Level, level_schema


def dict_to_level(level_dict: dict) -> Level:
    """
    Create a level from a dictionary. Raise a ValidationError if the data isn't valid.

    Args:
        level_dict (dict): Nested dictionary of level properties.

    Returns:
        Level: A level dataclass with all default values and clean data.
    """

    return level_schema.load(level_dict)


def level_to_dict(level: Level) -> dict:
    """
    Dump level data to a dictionary.

    Args:
        level (Level): Level to copy the data from.

    Returns:
        dict: Dictionary with all properties from the level.
    """

    return level_schema.dump(level)


def yaml_to_level(level_yaml: str) -> Level:
    """
    Create a level from a dictionary. Raise a ValidationError if the data isn't valid or YAMLError if the YAML can't be parsed.

    Args:
        level_yaml (str): A level in YAML.

    Returns:
         Level: A level dataclass with all default values and clean data.
    """

    data = safe_load(level_yaml)
    return level_schema.load(data)


def level_to_yaml(level: Level) -> str:
    data = level_schema.dump(level)
    return dump(data)


def level_yaml_to_validated_dict(level_yaml: str) -> dict:
    """
    Convert level YAML to its dictionary representation validating the data in the process.
    The validation is done by using the Level dataclass as an intermediary. Raise a ValidationError if the data isn't valid or YAMLError if the YAML can't be parsed.

    Args:
        level_yaml (str): A level as YAML. The data is dirty and may be incorrect/incomplete.

    Returns:
        dict: Dictionary representing the level with clean data.
    """

    return level_to_dict(yaml_to_level(level_yaml))


def level_dict_to_validated_yaml(level_dict: dict) -> str:
    """
    Convert a level dict to YAML validating the data in the process.
    The validation is done by using the Level dataclass as an intermediary. Raise a ValidationError if the data isn't valid.

    Args:
        level_dict (dict): A dictionary representing a level. The data is dirty and may be incorrect/incomplete.

    Returns:
        str: YAML level with clean data.
    """

    return level_to_yaml(dict_to_level(level_dict))


def validate_level_dict(level_dict: dict) -> dict:
    """
    Validate a level dict and populate it with missing properties.
    The validation is done by using the Level dataclass as an intermediary. Raise a ValidationError if the data isn't valid.

    Args:
        level_dict (dict): A dictionary representing a level. The data is dirty and may be incorrect/incomplete.

    Returns:
        dict: A cleaned-up level dict.
    """

    return level_to_dict(dict_to_level(level_dict))


def validate_level_yaml(level_yaml: str) -> str:
    """
    Validate a level YAML and populate it with missing properties.
    The validation is done by using the Level dataclass as an intermediary. Raise a ValidationError if the data isn't valid or YAMLError if the YAML can't be parsed.

    Args:
        level_yaml (str): A level as YAML. The data is dirty and may be incorrect/incomplete.

    Returns:
        dict: YAML level with clean data.
    """

    return level_to_yaml(yaml_to_level(level_yaml))
