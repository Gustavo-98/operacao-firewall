from __future__ import annotations

import pygame

from src.core.assets import Assets


class Workstation:

    WIDTH = 160
    HEIGHT = 160

    def __init__(
        self,
        x: int,
        y: int,
        challenge_id: int,
    ) -> None:

        Assets.load()

        self.challenge_id = challenge_id

        self.completed = False
        self.hover = False

        self.image_normal = pygame.transform.scale(
            Assets.workstation_normal,
            (self.WIDTH, self.HEIGHT),
        )

        self.image_hover = pygame.transform.scale(
            Assets.workstation_hover,
            (self.WIDTH, self.HEIGHT),
        )

        self.image_done = pygame.transform.scale(
            Assets.workstation_done,
            (self.WIDTH, self.HEIGHT),
        )

        self.rect = pygame.Rect(
            x,
            y,
            self.WIDTH,
            self.HEIGHT,
        )

        # Área para interação (tecla E)
        self.interaction_rect = self.rect.inflate(
            80,
            80,
        )

        # Apenas a mesa bloqueia o jogador.
        # O monitor fica livre para passar atrás.
        self.collider = pygame.Rect(
            x + 18,
            y + 110,
            124,
            26,
        )

    def update(
        self,
        player_rect: pygame.Rect,
    ) -> None:

        self.hover = player_rect.colliderect(
            self.interaction_rect
        )

    def draw(
        self,
        screen: pygame.Surface,
    ) -> None:

        if self.completed:
            image = self.image_done

        elif self.hover:
            image = self.image_hover

        else:
            image = self.image_normal

        screen.blit(
            image,
            self.rect,
        )