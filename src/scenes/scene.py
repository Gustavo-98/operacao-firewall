from __future__ import annotations

from abc import ABC, abstractmethod

import pygame


class Scene(ABC):
    """Classe base para todas as cenas do jogo."""

    @abstractmethod
    def handle_event(self, event: pygame.event.Event) -> None:
        """Processa um evento do pygame."""

    @abstractmethod
    def update(self, dt: float) -> None:
        """Atualiza a lógica da cena."""

    @abstractmethod
    def draw(self, screen: pygame.Surface) -> None:
        """Desenha a cena na tela."""