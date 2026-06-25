"""Normalização e resolução de filtros informados no terminal."""

from __future__ import annotations

import unicodedata


def normalize(value: str) -> str:
    """Remove variações de caixa, acentos e separadores comuns."""
    value = unicodedata.normalize("NFKD", value).encode("ascii", "ignore").decode("ascii")
    return value.lower().strip().replace("_", "-").replace(" ", "-")


def resolve_topic(value: str, topics: list[dict]) -> str | None:
    needle = normalize(value)
    for topic in topics:
        candidates = [topic["id"], topic["label"], *topic["aliases"]]
        if needle in {normalize(candidate) for candidate in candidates}:
            return topic["id"]
    return None


def normalize_difficulty(value: str) -> str | None:
    aliases = {
        "iniciante": "iniciante",
        "beginner": "iniciante",
        "intermediario": "intermediario",
        "intermediate": "intermediario",
        "avancado": "avancado",
        "advanced": "avancado",
    }
    return aliases.get(normalize(value))


def available_topics(topics: list[dict]) -> list[dict]:
    return sorted(topics, key=lambda item: item["label"])
