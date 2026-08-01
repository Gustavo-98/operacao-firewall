from __future__ import annotations

import pygame

from src.entities.computer import Computer


class OfficeMap:

    def __init__(self):

        self.floor = pygame.Rect(
            50,
            90,
            1180,
            580,
        )

        self.desks = [

            pygame.Rect(110, 120, 100, 70),
            pygame.Rect(330, 120, 100, 70),
            pygame.Rect(550, 120, 100, 70),
            pygame.Rect(770, 120, 100, 70),

            pygame.Rect(110, 480, 100, 70),
            pygame.Rect(330, 480, 100, 70),
            pygame.Rect(550, 480, 100, 70),
            pygame.Rect(770, 480, 100, 70),

        ]

        self.computers = [

            Computer(140, 140, 0),
            Computer(360, 140, 1),
            Computer(580, 140, 2),
            Computer(800, 140, 3),

            Computer(140, 500, 4),
            Computer(360, 500, 5),
            Computer(580, 500, 6),
            Computer(800, 500, 7),

        ]

    def draw(self, screen):

        pygame.draw.rect(
            screen,
            (70, 70, 78),
            self.floor,
            border_radius=10,
        )

        for desk in self.desks:

            pygame.draw.rect(
                screen,
                (135, 92, 58),
                desk,
                border_radius=5,
            )

            pygame.draw.rect(
                screen,
                (180, 130, 90),
                (
                    desk.x,
                    desk.y,
                    desk.width,
                    10,
                ),
                border_radius=5,
            )

        for computer in self.computers:
            computer.draw(screen)