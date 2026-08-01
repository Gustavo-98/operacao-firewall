from __future__ import annotations

import pygame

from src.core.assets import Assets


class JC:

    WIDTH = 96
    HEIGHT = 96

    def __init__(
        self,
        x: int,
        y: int,
    ) -> None:

        Assets.load()

        self.image = pygame.transform.scale(
            Assets.jc,
            (
                self.WIDTH,
                self.HEIGHT,
            ),
        )

        self.rect = pygame.Rect(
            x,
            y,
            self.WIDTH,
            self.HEIGHT,
        )

        self.interaction = self.rect.inflate(
            70,
            70,
        )

    def update(
        self,
        player_rect: pygame.Rect,
    ) -> bool:

        return player_rect.colliderect(
            self.interaction
        )

    def draw(
        self,
        screen: pygame.Surface,
    ) -> None:

        screen.blit(
            self.image,
            self.rect,
        )