from __future__ import annotations

import pygame

from src.core.assets import Assets
from src.core.constants import PLAYER_SPEED


class Player:

    SPEED = PLAYER_SPEED

    MIN_X = 50
    MAX_X = 1230

    MIN_Y = 90
    MAX_Y = 670

    SIZE = 112

    def __init__(self) -> None:

        Assets.load()

        self.image = pygame.transform.scale(
            Assets.player,
            (self.SIZE, self.SIZE),
        )

        self.x = 600.0
        self.y = 560.0

        self.enabled = True

        self.rect = pygame.Rect(
            int(self.x),
            int(self.y),
            self.SIZE,
            self.SIZE,
        )

    def update(
        self,
        dt: float,
        obstacles: list[pygame.Rect] | None = None,
    ) -> None:

        if not self.enabled:
            return

        dx = 0.0
        dy = 0.0

        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]:
            dy -= self.SPEED * dt

        if keys[pygame.K_s]:
            dy += self.SPEED * dt

        if keys[pygame.K_a]:
            dx -= self.SPEED * dt

        if keys[pygame.K_d]:
            dx += self.SPEED * dt

        # Movimento horizontal
        self.x += dx

        self.rect.topleft = (
            int(self.x),
            int(self.y),
        )

        if obstacles:
            for obstacle in obstacles:
                if self.rect.colliderect(obstacle):

                    if dx > 0:
                        self.rect.right = obstacle.left

                    elif dx < 0:
                        self.rect.left = obstacle.right

                    self.x = self.rect.x

        # Movimento vertical
        self.y += dy

        self.rect.topleft = (
            int(self.x),
            int(self.y),
        )

        if obstacles:
            for obstacle in obstacles:
                if self.rect.colliderect(obstacle):

                    if dy > 0:
                        self.rect.bottom = obstacle.top

                    elif dy < 0:
                        self.rect.top = obstacle.bottom

                    self.y = self.rect.y

        self.x = max(
            self.MIN_X,
            min(
                self.x,
                self.MAX_X - self.SIZE,
            ),
        )

        self.y = max(
            self.MIN_Y,
            min(
                self.y,
                self.MAX_Y - self.SIZE,
            ),
        )

        self.rect.topleft = (
            int(self.x),
            int(self.y),
        )

    def draw(
        self,
        screen: pygame.Surface,
    ) -> None:

        screen.blit(
            self.image,
            self.rect,
        )