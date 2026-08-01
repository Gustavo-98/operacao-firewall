from __future__ import annotations

import math

import pygame


class InteractionHint:

    def __init__(self) -> None:

        self.font = pygame.font.SysFont(
            "consolas",
            22,
            bold=True,
        )

    def draw(
        self,
        screen: pygame.Surface,
        rect: pygame.Rect,
    ) -> None:

        offset = math.sin(
            pygame.time.get_ticks() * 0.008
        ) * 4

        text = self.font.render(
            "[E] INVESTIGAR",
            True,
            (255, 255, 255),
        )

        text_rect = text.get_rect(
            center=(
                rect.centerx,
                rect.top - 22 + offset,
            )
        )

        background = text_rect.inflate(18, 10)

        pygame.draw.rect(
            screen,
            (20, 20, 25),
            background,
            border_radius=8,
        )

        pygame.draw.rect(
            screen,
            (0, 220, 120),
            background,
            width=2,
            border_radius=8,
        )

        screen.blit(
            text,
            text_rect,
        )