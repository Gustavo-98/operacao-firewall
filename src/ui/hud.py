from __future__ import annotations

import pygame

from src.core.constants import COLOR_TEXT


class HUD:

    HEIGHT = 80

    def __init__(self) -> None:

        self.title_font = pygame.font.SysFont(
            "consolas",
            28,
            bold=True,
        )

        self.font = pygame.font.SysFont(
            "consolas",
            22,
        )

    def draw(
        self,
        screen: pygame.Surface,
        timer: str,
        mission: str,
        score: int,
        solved: int,
        total: int,
    ) -> None:

        header = pygame.Rect(
            0,
            0,
            1280,
            self.HEIGHT,
        )

        pygame.draw.rect(
            screen,
            (20, 24, 30),
            header,
        )

        pygame.draw.line(
            screen,
            (0, 220, 120),
            (0, self.HEIGHT),
            (1280, self.HEIGHT),
            3,
        )

        title = self.title_font.render(
            "OPERAÇÃO FIREWALL",
            True,
            (0, 220, 120),
        )

        screen.blit(title, (20, 10))

        timer_surface = self.font.render(
            f"⏱ {timer}",
            True,
            COLOR_TEXT,
        )

        timer_rect = pygame.Rect(
            1070,
            10,
            170,
            30,
        )

        pygame.draw.rect(
            screen,
            (35, 40, 48),
            timer_rect,
            border_radius=8,
        )

        screen.blit(
            timer_surface,
            (
                timer_rect.x + 10,
                timer_rect.y + 4,
            ),
        )

        score_surface = self.font.render(
            f"⭐ {score}",
            True,
            COLOR_TEXT,
        )

        solved_surface = self.font.render(
            f"💻 {solved}/{total}",
            True,
            COLOR_TEXT,
        )

        mission_surface = self.font.render(
            mission,
            True,
            COLOR_TEXT,
        )

        screen.blit(score_surface, (20, 48))
        screen.blit(solved_surface, (180, 48))
        screen.blit(mission_surface, (340, 48))