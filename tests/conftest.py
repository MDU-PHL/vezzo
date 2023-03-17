"""
Configuration for pytest.
"""

import pytest
import yaml


@pytest.fixture(scope="module")
def version_strings(request):
    """
    # A fixture that parses the version-string.yaml file and returns it as a list
    of dictionaries one for each tool in the file.
    """
    test_str_file = request.path.parent.joinpath("version-strings.yaml")
    with open(test_str_file, encoding="utf8") as f:
        return [tuple(dat.values()) for dat in yaml.safe_load(f)]


@pytest.fixture(scope="module")
def config_pass(request):
    """
    A fixture that returns the path to pass config yaml.
    """
    path = request.path.parent.joinpath("test-config-pass.yaml")
    return path


@pytest.fixture(scope="module")
def config_fail(request):
    """
    A fixture that returns the path to fail config yaml.
    """
    path = request.path.parent.joinpath("test-config-fail.yaml")
    return path
