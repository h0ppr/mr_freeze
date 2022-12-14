from __future__ import annotations

import pytest

try:
    from mr_freeze.main import virtual_env_detector_naive
    from mr_freeze.main import line_checker
except (ImportError, ModuleNotFoundError):
    from ..mr_freeze.main import virtual_env_detector_naive
    from ..mr_freeze.main import line_checker


def test_env_detector_naive() -> None:
    """Asserts that output is relevant to the venv"""
    assert virtual_env_detector_naive() == "pipenv"


@pytest.mark.parametrize(
    "test_input, output",
    [
        (".\n", False),
        ("\n", False),
        ("test\n", True),
        ("double_test_\n", True),
    ],
)
def test_line_checker(test_input: str, output: str):
    """tests line checker -> *sigh* pylint..."""
    assert line_checker(test_input) == output
