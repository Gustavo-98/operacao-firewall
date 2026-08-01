from __future__ import annotations


class GameTimer:
    """Controla o tempo restante da partida."""

    def __init__(self, duration: float = 300.0) -> None:
        self.duration = duration
        self.remaining = duration
        self.running = False

    def start(self) -> None:
        self.running = True

    def stop(self) -> None:
        self.running = False

    def reset(self) -> None:
        self.remaining = self.duration
        self.running = False

    def update(self, dt: float) -> None:
        if not self.running:
            return

        self.remaining -= dt

        if self.remaining < 0:
            self.remaining = 0

    @property
    def finished(self) -> bool:
        return self.remaining <= 0

    @property
    def minutes(self) -> int:
        return int(self.remaining) // 60

    @property
    def seconds(self) -> int:
        return int(self.remaining) % 60

    @property
    def formatted(self) -> str:
        return f"{self.minutes:02}:{self.seconds:02}"