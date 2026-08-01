from __future__ import annotations

import json
import random
from pathlib import Path


class QuestionManager:

    def __init__(self) -> None:

        file = Path("assets/data/questions.json")

        with open(file, "r", encoding="utf-8") as f:
            questions = json.load(f)

        random.shuffle(questions)

        self.questions = questions[:8]

    def get(self, index: int) -> dict:

        return self.questions[index]