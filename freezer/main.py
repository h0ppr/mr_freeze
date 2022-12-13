from __future__ import annotations

import os
from typing import Sequence


def saver(*args, **kwargs) -> None:
    match kwargs['method']: 
        case "pipenv": 
            os.system('pipenv lock -r > requirements.txt')
        case "poetry": 
            os.system('poetry export -f requirements.txt --output requirements.txt')
    
    return None


def virtual_env_detector_naive() -> str: 
    files = [file.name for file in os.scandir()]
    if "Pipfile" in files: 
        return "pipenv"
    elif "poetry.lock" in files: 
        return "poetry"


def main(argv: Sequence[str] | None = None) -> None:
    venv_method = virtual_env_detector_naive()
    saver(method=venv_method)


if __name__ == "__main__":
    main()
