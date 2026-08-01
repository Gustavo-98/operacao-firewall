from __future__ import annotations

import pygame

from src.core.config import Config
from src.scenes.game_scene import GameScene
from src.scenes.scene import Scene
from src.ui.button import Button


class MenuScene(Scene):

    def __init__(self, scene_manager) -> None:

        self.scene_manager = scene_manager

        self.title_font = pygame.font.SysFont(
            "consolas",
            60,
            bold=True,
        )

        self.button_font = pygame.font.SysFont(
            "consolas",
            32,
        )

        self.buttons = [
            Button(
                "Iniciar Operação",
                self.button_font,
                (640, 300),
            ),
            Button(
                "Sair",
                self.button_font,
                (640, 360),
            ),
        ]

        self.selected = 0
        self.buttons[0].selected = True

    def handle_event(self, event):

        if event.type != pygame.KEYDOWN:
            return

        if event.key == pygame.K_DOWN:

            self.buttons[self.selected].selected = False
            self.selected = (self.selected + 1) % len(self.buttons)
            self.buttons[self.selected].selected = True

        elif event.key == pygame.K_UP:

            self.buttons[self.selected].selected = False
            self.selected = (self.selected - 1) % len(self.buttons)
            self.buttons[self.selected].selected = True

        elif event.key == pygame.K_RETURN:

            if self.selected == 0:
                self.scene_manager.change(
                    GameScene(self.scene_manager)
                )

            else:
                pygame.event.post(
                    pygame.event.Event(pygame.QUIT)
                )

    def update(self, dt):
        pass

    def draw(self, screen):

        screen.fill(Config.BACKGROUND_COLOR)

        title = self.title_font.render(
            "OPERAÇÃO FIREWALL",
            True,
            (0, 220, 120),
        )

        screen.blit(
            title,
            title.get_rect(center=(640, 160)),
        )

        for button in self.buttons:
            button.draw(screen)