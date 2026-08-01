import pygame

from src.core.config import Config
from src.scenes.menu_scene import MenuScene
from src.scenes.scene_manager import SceneManager


class Game:
    """Classe principal do jogo."""

    def __init__(self) -> None:
        pygame.init()

        self.screen = pygame.display.set_mode(
            (Config.SCREEN_WIDTH, Config.SCREEN_HEIGHT)
        )

        pygame.display.set_caption(Config.TITLE)

        self.clock = pygame.time.Clock()
        self.running = True

        self.scene_manager = SceneManager()
        self.scene_manager.change(
            MenuScene(self.scene_manager)
        )

    def run(self) -> None:

        while self.running:

            dt = self.clock.tick(Config.FPS) / 1000

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    self.running = False

                self.scene_manager.handle_event(event)

            self.scene_manager.update(dt)
            self.scene_manager.draw(self.screen)

            pygame.display.flip()

        pygame.quit()