from pytest import mark, raises

from mystics_and_manuscripts_core.internal.version import Version, parse_version, is_version_supported


@mark.parametrize("version_string, parsed_version", [
    ("3.2.4", Version(3, 2, 4)),
    ("10.0.1", Version(10, 0, 1)),
    ("-1.0.155", Version(-1, 0, 155)),
    ("-2.-4.-6", Version(-2, -4, -6)),
    ("1.20.6", Version(1, 20, 6))
])
def test_parse_version(version_string: str, parsed_version: Version) -> None:
    assert parse_version(version_string) == parsed_version


length_err_message = "Not a valid version format. Include 3 dot-separated numbers, e.g. 3.2.4"
conversion_err_message = "Major, minor or patch version isn't a number."


@mark.parametrize("version_string, error_message", [
    ("", length_err_message),
    ("1", length_err_message),
    ("5.2", length_err_message),
    ("6.2.3.5", length_err_message),
    ("1.2.", conversion_err_message),
    ("hello.world.hi", conversion_err_message),
    ("1.1.1a", conversion_err_message)
])
def test_parse_version_exception(version_string: str, error_message: str) -> None:
    with raises(ValueError, match=error_message):
        parse_version(version_string)


@mark.parametrize("version, target_version, expected_result", [
    # major version compatibility
    (Version(1, 1, 1), Version(2, 1, 1), False),
    (Version(2, 1, 1), Version(2, 3, 2), True),
    (Version(2, 10, 5), Version(3, 1, 2), False),
    # minor version compatibility
    (Version(0, 2, 5), Version(0, 1, 1), False),
    (Version(0, 2, 5), Version(0, 2, 5), True),
    (Version(0, 2, 5), Version(0, 69, 0), True),
    # patch shouldn't make a difference
    (Version(5, 8, 1), Version(5, 8, 0), True)
])
def test_is_version_supported(version: Version, target_version: Version, expected_result: bool) -> None:
    assert is_version_supported(version, target_version) == expected_result
