from __future__ import annotations

import pygame


class Button:
    def __init__(self, text: str, font: pygame.font.Font, center: tuple[int, int]):
        self.text = text
        self.font = font
        self.center = center
        self.selected = False

    def draw(self, screen: pygame.Surface) -> None:
        color = (0, 220, 120) if self.selected else (220, 220, 220)

        surface = self.font.render(self.text, True, color)
        rect = surface.get_rect(center=self.center)

        screen.blit(surface, rect)