from __future__ import annotations

import json
from pathlib import Path

from src.dialogue.dialogue import Dialogue


class DialogueManager:

    def __init__(self) -> None:

        self.active = False
        self.dialogue: Dialogue | None = None

        self.page = 0

        self.char = 0.0

        self.speed = 45.0

        self.finished_page = False

        self.timer = 0.0

    def start(
        self,
        dialogue_name: str,
    ) -> None:

        path = (
            Path("assets/dialogues")
            / f"{dialogue_name}.json"
        )

        with open(
            path,
            "r",
            encoding="utf-8",
        ) as file:

            data = json.load(file)

        self.dialogue = Dialogue(
            speaker=data["speaker"],
            portrait=data["portrait"],
            pages=data["pages"],
        )

        self.active = True

        self.page = 0

        self.char = 0

        self.finished_page = False

        self.timer = 0

    def update(
        self,
        dt: float,
    ) -> None:

        if (
            not self.active
            or self.dialogue is None
        ):
            return

        if self.finished_page:
            self.timer += dt
            return

        text = self.dialogue.pages[self.page]

        self.char += self.speed * dt

        if self.char >= len(text):

            self.char = len(text)

            self.finished_page = True

    def current_text(self) -> str:

        if self.dialogue is None:
            return ""

        return self.dialogue.pages[self.page][
            : int(self.char)
        ]

    @property
    def show_continue(self) -> bool:

        if not self.finished_page:
            return False

        return int(self.timer * 2) % 2 == 0

    def next(self) -> None:

        if not self.active:
            return

        if not self.finished_page:

            self.char = len(
                self.dialogue.pages[self.page]
            )

            self.finished_page = True

            return

        self.page += 1

        if (
            self.dialogue is not None
            and self.page < len(self.dialogue.pages)
        ):

            self.char = 0

            self.finished_page = False

            self.timer = 0

            return

        self.close()

    def close(self) -> None:

        self.active = False

        self.dialogue = None

        self.page = 0

        self.char = 0

        self.finished_page = False

        self.timer = 0