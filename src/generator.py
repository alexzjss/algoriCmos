"""Leitura dos dados JSON e composição de exercícios aleatórios."""

from __future__ import annotations

import json
import random
from pathlib import Path
from typing import Any


class ExerciseGenerator:
    def __init__(self, data_dir: Path, rng: random.Random | None = None) -> None:
        self.rng = rng or random.Random()
        self.templates = self._load(data_dir / "templates.json")
        self.topics = self._load(data_dir / "topics.json")
        self.difficulties = self._load(data_dir / "difficulties.json")
        self.topic_map = {topic["id"]: topic for topic in self.topics}
        self.difficulty_map = {item["id"]: item for item in self.difficulties}

    @staticmethod
    def _load(path: Path) -> Any:
        with path.open(encoding="utf-8") as file:
            return json.load(file)

    def generate(self, count: int = 1, topic: str | None = None, difficulty: str | None = None) -> list[dict]:
        choices = [
            template
            for template in self.templates
            if (topic is None or template["topic"] == topic)
            and (difficulty is None or template["difficulty"] == difficulty)
        ]
        if not choices:
            raise ValueError("Não há templates para essa combinação de tópico e dificuldade.")
        return [self._make_exercise(self.rng.choice(choices)) for _ in range(count)]

    def _make_exercise(self, template: dict) -> dict:
        values = {
            name: self.rng.choice(options)
            for name, options in template.get("variables", {}).items()
        }
        return {
            "topic": self.topic_map[template["topic"]]["label"],
            "difficulty": self.difficulty_map[template["difficulty"]]["label"],
            "statement": template["template"].format(**values),
            "extra": template.get("extra", "").format(**values),
        }

    def get_theory(self, topic_id: str) -> dict:
        return self.topic_map[topic_id]["theory"]
