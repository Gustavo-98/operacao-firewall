from __future__ import annotations

import pygame

from src.core.config import Config
from src.scenes.scene import Scene


class ResultScene(Scene):

    def __init__(
        self,
        scene_manager,
        score: int,
        solved: int,
        total: int,
    ) -> None:

        self.scene_manager = scene_manager

        self.score = score
        self.solved = solved
        self.total = total

        self.title_font = pygame.font.SysFont(
            "consolas",
            52,
            bold=True,
        )

        self.font = pygame.font.SysFont(
            "consolas",
            28,
        )

    def handle_event(self, event):

        if (
            event.type == pygame.KEYDOWN
            and event.key == pygame.K_RETURN
        ):
            from src.scenes.menu_scene import MenuScene

            self.scene_manager.change(
                MenuScene(self.scene_manager)
            )

    def update(self, dt):
        pass

    def draw(self, screen):

        screen.fill((18, 22, 28))

        if self.score >= 700:
            nota = "A"
        elif self.score >= 500:
            nota = "B"
        elif self.score >= 300:
            nota = "C"
        else:
            nota = "D"

        y = 120

        def write(text, font=None):

            nonlocal y

            if font is None:
                font = self.font

            surf = font.render(
                text,
                True,
                (255, 255, 255),
            )

            screen.blit(
                surf,
                surf.get_rect(center=(640, y)),
            )

            y += 55

        write(
            "RELATÓRIO FINAL",
            self.title_font,
        )

        y += 30

        write(f"Pontuação: {self.score}")

        write(
            f"Incidentes resolvidos: {self.solved}/{self.total}"
        )

        write(f"Nota: {nota}")

        y += 40

        write("Pressione ENTER para voltar ao menu")