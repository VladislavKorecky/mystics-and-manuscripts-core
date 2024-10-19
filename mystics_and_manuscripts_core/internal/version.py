from collections import namedtuple


Version = namedtuple("Version", ["major", "minor", "patch"])


def parse_version(version: str) -> Version:
    """
    Break down an app version to its major, minor and patch numbers.

    Args:
        version (str): An M&M core version, e.g. 3.2.4

    Returns:
        Version: Tuple with a major, minor and patch version numbers from the version string.

    Raises:
        ValueError: The version can't be parsed because its format is invalid.
    """

    # separate the version numbers, e.g. 3.2.4 to ["3", "2", "4"]
    version_numbers = version.split(".")

    if len(version_numbers) != 3:
        raise ValueError("Not a valid version format. Include 3 dot-separated numbers, e.g. 3.2.4")

    try:
        major_version, minor_version, patch_version = [int(num) for num in version_numbers]
    except ValueError:
        raise ValueError("Major, minor or patch version isn't a number.")

    return Version(major_version, minor_version, patch_version)


def is_version_supported(version: Version, target_version: Version) -> bool:
    """
    Check if an M&M version is compatible with a target version. This means the target supports all features from the
    compared version.

    Args:
        version (Version): Version of an M&M standard.
        target_version (Version): Version of a core.

    Returns:
        bool: True of the standard can run on the target, False otherwise.
    """

    # major versions are incompatible between each other
    if version.major != target_version.major:
        return False

    # higher minor versions are backwards compatible with the previous ones
    if version.minor > target_version.minor:
        return False

    return True


def read_current_version() -> str:
    """
    Return the M&M standard this core is running on.

    Returns:
        str: Version read from the version.txt file.
    """

    with open("version.txt", "r") as f:
        return f.read()
