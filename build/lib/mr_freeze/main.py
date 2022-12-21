from __future__ import annotations

import os
from typing import Optional


def saver(**kwargs) -> None:
    """Outputs appropriate command basis venv"""
    method = kwargs["method"]
    if method == "pipenv":
        os.system("pipenv lock -r > requirements.txt")
    elif method == "poetry":
        os.system("poetry export -f requirements.txt --output requirements.txt")


def virtual_env_detector_naive() -> Optional[str]:
    """Naively scans for lock files relevant to venv"""
    files = [file.name for file in os.scandir()]
    if "Pipfile" in files:
        return "pipenv"
    if "poetry.lock" in files:
        return "poetry"


# def main(argv: Sequence[str] | None = None) -> None:
def main() -> None:
    """Initial Entry Point"""
    venv_method = virtual_env_detector_naive()
    saver(method=venv_method)


if __name__ == "__main__":
    raise SystemExit(main())
