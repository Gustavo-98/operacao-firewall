from __future__ import annotations

from src.scenes.scene import Scene


class SceneManager:
    """Gerencia a cena atualmente ativa."""

    def __init__(self) -> None:
        self._current: Scene | None = None

    @property
    def current(self) -> Scene | None:
        return self._current

    def change(self, scene: Scene) -> None:
        """Troca a cena ativa."""
        self._current = scene

    def handle_event(self, event) -> None:
        if self._current is not None:
            self._current.handle_event(event)

    def update(self, dt: float) -> None:
        if self._current is not None:
            self._current.update(dt)

    def draw(self, screen) -> None:
        if self._current is not None:
            self._current.draw(screen)