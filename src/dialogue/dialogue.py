from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True)
class Dialogue:

    speaker: str

    portrait: str

    pages: list[str]