from dataclasses import dataclass


@dataclass(frozen=True)
class Config:
    """Configurações globais do jogo."""

    TITLE: str = "Operação Firewall"

    SCREEN_WIDTH: int = 1280
    SCREEN_HEIGHT: int = 720

    FPS: int = 60

    BACKGROUND_COLOR = (18, 22, 32)