"""
Test vezzo functions
"""

import semver
import pytest
from pytest import assume  # pylint: disable=no-name-in-module
from vezzo import parse, verify, verify_from_config
from vezzo.exceptions import UnableToParseVersionString


@pytest.mark.parametrize("version_strings", ["version_strings.yaml"], indirect=True)
def test_parse_version_string(version_strings):
    """
    Test the parse_version_string function
    """

    for tool, exp, version_string in version_strings:
        expected = semver.VersionInfo.parse(exp)
        print(f"Testing {tool}")
        if tool == "no-version-string":
            with pytest.raises(UnableToParseVersionString):
                parse(version_string)
        else:
            with assume:
                assert parse(version_string) == expected


test_data = [
    ("==1.2.3", "1.2.3", True),
    ("==1.2.3", "1.2.4", False),
    ("<=1.2.3", "1.2.2", True),
    ("<1.2.3", "1.2.3", False),
    ("<1.2.3", "1.2.2", True),
    (">=1.2.3", "1.2.3", True),
    (">=1.2.3", "1.2.4", True),
    (">=1.2.3", "1.2.2", False),
    (">1.2.3", "1.2.3", False),
    (">1.2.3", "1.2.4", True),
    (">1.2.3", "1.2.2", False),
    ("!=1.2.3", "1.2.3", False),
    ("!=1.2.3", "1.2.4", True),
    ("!=1.2.3", "1.2.2", True),
]


@pytest.mark.parametrize("exp_version,obs_version,expected", test_data)
def test_verify(exp_version, obs_version, expected):
    """
    Test the verify function
    """
    print("Testing verify")
    is_match, obs_version = verify(exp_version, obs_version)
    assert is_match == expected
    assert obs_version == obs_version


def test_verify_from_config_pass(config_pass):
    """
    Test the verify_from_config function
    """
    print("Testing verify_from_config")
    cmds = verify_from_config(config_pass)
    for result, version, _ in cmds:
        assert result
        assert version in ["1.17.0", "2.13.0"]


def test_verify_from_config_fail(config_fail):
    """
    Test the verify_from_config function
    """
    print("Testing verify_from_config")
    cmds = verify_from_config(config_fail)
    for result, version, _ in cmds:
        assert not result
        assert version in ["1.17.0", "2.13.0"]
