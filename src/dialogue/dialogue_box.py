from __future__ import annotations

import pygame

from src.core.assets import Assets
from src.dialogue.dialogue_manager import DialogueManager


class DialogueBox:

    WIDTH = 1180
    HEIGHT = 180

    def __init__(self) -> None:

        Assets.load()

        self.font_name = pygame.font.SysFont(
            "consolas",
            28,
            bold=True,
        )

        self.font_text = pygame.font.SysFont(
            "consolas",
            24,
        )

        self.font_hint = pygame.font.SysFont(
            "consolas",
            20,
            bold=True,
        )

    def wrap_text(
        self,
        text: str,
        font: pygame.font.Font,
        width: int,
    ) -> list[str]:

        words = text.split()

        lines = []

        current = ""

        for word in words:

            test = (
                word
                if current == ""
                else current + " " + word
            )

            if font.size(test)[0] <= width:

                current = test

            else:

                lines.append(current)

                current = word

        if current:

            lines.append(current)

        return lines

    def draw(
        self,
        screen: pygame.Surface,
        manager: DialogueManager,
    ) -> None:

        if (
            not manager.active
            or manager.dialogue is None
        ):
            return

        overlay = pygame.Surface(
            screen.get_size(),
            pygame.SRCALPHA,
        )

        overlay.fill(
            (0, 0, 0, 140),
        )

        screen.blit(
            overlay,
            (0, 0),
        )

        x = 50
        y = screen.get_height() - 210

        box = pygame.Surface(
            (self.WIDTH, self.HEIGHT),
            pygame.SRCALPHA,
        )

        box.fill(
            (18, 22, 30, 240),
        )

        pygame.draw.rect(
            box,
            (0, 220, 170),
            box.get_rect(),
            3,
            8,
        )

        screen.blit(
            box,
            (x, y),
        )

        portrait = pygame.transform.scale(
            Assets.jc_portrait,
            (110, 110),
        )

        screen.blit(
            portrait,
            (x + 20, y + 20),
        )

        pygame.draw.line(
            screen,
            (70, 70, 70),
            (x + 150, y + 15),
            (x + 150, y + 165),
            2,
        )

        title = self.font_name.render(
            manager.dialogue.speaker,
            True,
            (0, 255, 180),
        )

        screen.blit(
            title,
            (x + 175, y + 18),
        )

        lines = self.wrap_text(
            manager.current_text(),
            self.font_text,
            920,
        )

        yy = y + 60

        for line in lines:

            txt = self.font_text.render(
                line,
                True,
                (240, 240, 240),
            )

            screen.blit(
                txt,
                (x + 175, yy),
            )

            yy += 30

        if manager.show_continue:

            hint = self.font_hint.render(
                "[ENTER] Continuar",
                True,
                (0, 220, 255),
            )

            screen.blit(
                hint,
                (
                    x + 930,
                    y + 145,
                ),
            )