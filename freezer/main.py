from __future__ import annotations

import os
from typing import Sequence


def saver() -> None:
    os.system('pipenv lock -r > requirements.txt')
    return None


def main(argv: Sequence[str] | None = None) -> None:
    saver()


if __name__ == "__main__":
    main()
