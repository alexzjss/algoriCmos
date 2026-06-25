"""Apresentação em texto para o terminal."""

from __future__ import annotations


def format_exercise(exercise: dict) -> str:
    output = (
        f"Tópico: {exercise['topic']}\n"
        f"Dificuldade: {exercise['difficulty']}\n\n"
        f"{exercise['statement']}"
    )
    if exercise["extra"]:
        output += f"\n\nExtra:\n{exercise['extra']}"
    return output


def format_theory(theory: dict) -> str:
    pitfalls = "\n".join(f"- {item}" for item in theory["pitfalls"])
    return (
        f"Tema: {theory['title']}\n\nResumo:\n{theory['summary']}\n\n"
        f"Pegadinhas:\n{pitfalls}\n\nExemplo:\n{theory['example']}"
    )
