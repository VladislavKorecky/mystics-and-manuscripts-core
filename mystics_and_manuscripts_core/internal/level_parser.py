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
