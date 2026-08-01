from __future__ import annotations

import pygame


class QuestionWindow:

    def __init__(self) -> None:

        self.title_font = pygame.font.SysFont(
            "consolas",
            30,
            bold=True,
        )

        self.font = pygame.font.SysFont(
            "consolas",
            22,
        )

        self.message_font = pygame.font.SysFont(
            "consolas",
            34,
            bold=True,
        )

        self.visible = False
        self.question = None

        self.feedback = ""
        self.feedback_color = (255, 255, 255)

    def show(self, question: dict) -> None:

        self.question = question
        self.visible = True
        self.feedback = ""

    def hide(self) -> None:

        self.visible = False
        self.question = None
        self.feedback = ""

    def show_success(self) -> None:

        self.feedback = "✔ RESPOSTA CORRETA!"
        self.feedback_color = (40, 220, 120)

    def show_error(self) -> None:

        self.feedback = "✖ RESPOSTA INCORRETA!"
        self.feedback_color = (220, 60, 60)

    def draw(self, screen: pygame.Surface) -> None:

        if not self.visible or self.question is None:
            return

        overlay = pygame.Surface(
            screen.get_size(),
            pygame.SRCALPHA,
        )

        overlay.fill((0, 0, 0, 140))

        screen.blit(overlay, (0, 0))

        window = pygame.Rect(
            160,
            90,
            960,
            500,
        )

        pygame.draw.rect(
            screen,
            (26, 30, 38),
            window,
            border_radius=14,
        )

        pygame.draw.rect(
            screen,
            (0, 220, 120),
            window,
            width=3,
            border_radius=14,
        )

        title = self.title_font.render(
            self.question["categoria"],
            True,
            (0, 220, 120),
        )

        screen.blit(title, (210, 120))

        pygame.draw.line(
            screen,
            (0, 220, 120),
            (210, 165),
            (1070, 165),
            2,
        )

        question = self.font.render(
            self.question["pergunta"],
            True,
            (255, 255, 255),
        )

        screen.blit(question, (210, 200))

        y = 280

        for i, option in enumerate(
            self.question["alternativas"],
            start=1,
        ):

            rect = pygame.Rect(
                210,
                y - 10,
                760,
                42,
            )

            pygame.draw.rect(
                screen,
                (40, 44, 54),
                rect,
                border_radius=8,
            )

            text = self.font.render(
                f"{i}. {option}",
                True,
                (255, 255, 255),
            )

            screen.blit(text, (225, y))

            y += 60

        if self.feedback:

            msg = self.message_font.render(
                self.feedback,
                True,
                self.feedback_color,
            )

            screen.blit(
                msg,
                msg.get_rect(
                    center=(640, 545),
                ),
            )