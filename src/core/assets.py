from __future__ import annotations

from pathlib import Path

import pygame


class Assets:

    _loaded = False

    @classmethod
    def load(cls) -> None:

        if cls._loaded:
            return

        base = Path("assets/images")

        # =========================
        # BACKGROUND
        # =========================

        cls.office_background = pygame.image.load(
            base / "background" / "office_background.png"
        ).convert()

        # =========================
        # PLAYER
        # =========================

        cls.player = pygame.image.load(
            base / "player" / "player.png"
        ).convert_alpha()

        # =========================
        # WORKSTATIONS
        # =========================

        cls.workstation_normal = pygame.image.load(
            base / "workstations" / "workstation_normal.png"
        ).convert_alpha()

        cls.workstation_hover = pygame.image.load(
            base / "workstations" / "workstation_hover.png"
        ).convert_alpha()

        cls.workstation_done = pygame.image.load(
            base / "workstations" / "workstation_done.png"
        ).convert_alpha()

        # =========================
        # NPC
        # =========================

        cls.jc = pygame.image.load(
            base / "npc" / "jc.png"
        ).convert_alpha()

        # =========================
        # PORTRAITS
        # =========================

        cls.jc_portrait = pygame.image.load(
            base / "portraits" / "jc_portrait.png"
        ).convert_alpha()

        # =========================
        # UI
        # =========================

        cls.logo = pygame.image.load(
            base / "logo" / "logo.png"
        ).convert_alpha()

        cls._loaded = True