from __future__ import annotations
from src.entities.jc import JC

import pygame

from src.core.assets import Assets
from src.core.constants import (
    COLOR_GAME_BACKGROUND,
    GAME_DURATION,
)
from src.dialogue.dialogue_box import DialogueBox
from src.dialogue.dialogue_manager import DialogueManager
from src.dialogue.dialogues import JC_INTRO
from src.entities.player import Player
from src.entities.workstation import Workstation
from src.gameplay.question_manager import QuestionManager
from src.scenes.result_scene import ResultScene
from src.scenes.scene import Scene
from src.systems.game_timer import GameTimer
from src.ui.hud import HUD
from src.ui.interaction_hint import InteractionHint
from src.ui.question_window import QuestionWindow


class GameScene(Scene):

    FEEDBACK_TIME = 1000

    def __init__(self, scene_manager) -> None:

        Assets.load()

        self.scene_manager = scene_manager

        self.background = pygame.transform.scale(
            Assets.office_background,
            (1280, 720),
        )

        self.player = Player()

        self.jc = JC(
            560,
            40,
        )

        self.near_jc = False
        self.timer = GameTimer(GAME_DURATION)

        self.hud = HUD()
        self.hint = InteractionHint()
        self.question = QuestionWindow()

        self.question_manager = QuestionManager()

        self.dialogue_manager = DialogueManager()
        self.dialogue_box = DialogueBox()

        self.score = 0
        self.solved = 0
        self.total = 8

        positions = [
            (120, 120),
            (360, 120),
            (600, 120),
            (840, 120),
            (120, 400),
            (360, 400),
            (600, 400),
            (840, 400),
        ]

        self.workstations = []

        for i, (x, y) in enumerate(positions):

            self.workstations.append(
                Workstation(
                    x,
                    y,
                    i,
                )
            )

        self.nearby = None
        self.active_workstation = None
        self.feedback_until = 0
    
    def handle_event(
        self,
        event: pygame.event.Event,
    ) -> None:

        if self.dialogue_manager.active:

            if (
                event.type == pygame.KEYDOWN
                and event.key == pygame.K_RETURN
            ):

                self.dialogue_manager.next()

                if not self.dialogue_manager.active:

                    self.player.enabled = True
                    self.timer.start()

            return

        if event.type != pygame.KEYDOWN:
            return

        if (
            event.key == pygame.K_e
            and self.near_jc
        ):

            self.player.enabled = False

            self.dialogue_manager.start(
                "jc_intro"
            )

            return

        if (
            self.question.visible
            and pygame.time.get_ticks() < self.feedback_until
        ):
            return

        if event.key == pygame.K_ESCAPE:

            self.question.hide()

            self.active_workstation = None

            self.player.enabled = True

            return

        if (
            event.key == pygame.K_e
            and self.nearby is not None
            and not self.nearby.completed
            and not self.question.visible
        ):

            self.active_workstation = self.nearby

            self.question.show(
                self.question_manager.get(
                    self.active_workstation.challenge_id
                )
            )

            self.player.enabled = False

            return

        if not self.question.visible:
            return

        if event.key not in (
            pygame.K_1,
            pygame.K_2,
            pygame.K_3,
        ):
            return

        resposta = {
            pygame.K_1: 0,
            pygame.K_2: 1,
            pygame.K_3: 2,
        }[event.key]

        correta = self.question.question["correta"]

        if (
            resposta == correta
            and self.active_workstation is not None
        ):

            if not self.active_workstation.completed:

                self.active_workstation.completed = True

                self.score += 100
                self.solved += 1

            self.question.show_success()

        else:

            self.timer.remaining = max(
                0,
                self.timer.remaining - 30,
            )

            self.question.show_error()

        self.feedback_until = (
            pygame.time.get_ticks()
            + self.FEEDBACK_TIME
        )
    def update(
        self,
        dt: float,
    ) -> None:

        self.dialogue_manager.update(
            dt,
        )

        if self.dialogue_manager.active:
            return

        obstacles = [
            workstation.collider
            for workstation in self.workstations
        ]

        self.player.update(
            dt,
            obstacles,
        )
        self.near_jc = self.jc.update(
            self.player.rect,
        )
        self.timer.update(
            dt,
        )

        if (
            self.question.visible
            and self.feedback_until > 0
            and pygame.time.get_ticks()
            >= self.feedback_until
        ):

            self.question.hide()

            self.active_workstation = None

            self.player.enabled = True

            self.feedback_until = 0

        if (
            self.timer.remaining <= 0
            or self.solved == self.total
        ):

            self.scene_manager.change(
                ResultScene(
                    self.scene_manager,
                    self.score,
                    self.solved,
                    self.total,
                )
            )

            return

        if self.question.visible:
            return

        self.nearby = None

        for workstation in self.workstations:

            workstation.update(
                self.player.rect,
            )

            if (
                not workstation.completed
                and workstation.hover
            ):

                self.nearby = workstation

                break

    def draw(
        self,
        screen: pygame.Surface,
    ) -> None:

        screen.fill(
            COLOR_GAME_BACKGROUND,
        )

        screen.blit(
            self.background,
            (0, 0),
        )

        for workstation in self.workstations:

            workstation.draw(
                screen,
            )

        self.player.draw(
            screen,
        )

        if (
            (
            self.nearby is not None
            or self.near_jc
            )
            and not self.question.visible
            and not self.dialogue_manager.active
        ):

            if self.near_jc:

               self.hint.draw(
                screen,
                self.jc.rect,
            )

        elif self.nearby is not None:

            self.hint.draw(
                screen,
                self.nearby.rect,
            )

            if not self.dialogue_manager.active:

                self.hud.draw(
                screen,
                self.timer.formatted,
                "Resolva os incidentes",
                self.score,
                self.solved,
                self.total,
            )

        self.question.draw(
            screen,
        )

        self.dialogue_box.draw(
            screen,
            self.dialogue_manager,
        )