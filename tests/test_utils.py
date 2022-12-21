from __future__ import annotations

try:
    from mr_freeze.main import virtual_env_detector_naive
except (ImportError, ModuleNotFoundError):
    from ..mr_freeze.main import virtual_env_detector_naive


def test_env_detector_naive() -> None:
    """Asserts that output is relevant to the venv"""
    assert virtual_env_detector_naive() == "pipenv"
