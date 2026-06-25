"""Ponto de entrada do gerador de exercícios de C."""

from __future__ import annotations

import argparse
from pathlib import Path

from src.filters import available_topics, normalize_difficulty, resolve_topic
from src.formatter import format_exercise, format_theory
from src.generator import ExerciseGenerator


BASE_DIR = Path(__file__).resolve().parent


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Gera exercícios de Programação em C e análise de algoritmos."
    )
    parser.add_argument("--topic", help="Conteúdo desejado (ex.: arrays, ponteiros).")
    parser.add_argument(
        "--difficulty",
        help="Dificuldade: iniciante, intermediário ou avançado.",
    )
    parser.add_argument("--count", type=int, default=1, help="Quantidade de exercícios.")
    parser.add_argument("--theory", metavar="TOPIC", help="Mostra uma revisão teórica do tema.")
    parser.add_argument("--list-topics", action="store_true", help="Lista os tópicos disponíveis.")
    return parser


def main() -> int:
    args = build_parser().parse_args()
    generator = ExerciseGenerator(BASE_DIR / "data")

    if args.list_topics:
        print("Tópicos disponíveis:")
        for topic in available_topics(generator.topics):
            print(f"- {topic['label']} ({', '.join(topic['aliases'])})")
        return 0

    if args.theory:
        topic_id = resolve_topic(args.theory, generator.topics)
        if not topic_id:
            print(f"Tema não encontrado: {args.theory}. Use --list-topics para consultar as opções.")
            return 2
        print(format_theory(generator.get_theory(topic_id)))
        return 0

    if args.count < 1:
        print("--count deve ser maior que zero.")
        return 2

    topic_id = resolve_topic(args.topic, generator.topics) if args.topic else None
    if args.topic and not topic_id:
        print(f"Tópico não encontrado: {args.topic}. Use --list-topics para consultar as opções.")
        return 2

    difficulty = normalize_difficulty(args.difficulty) if args.difficulty else None
    if args.difficulty and not difficulty:
        print("Dificuldade inválida. Use: iniciante, intermediário ou avançado.")
        return 2

    try:
        exercises = generator.generate(count=args.count, topic=topic_id, difficulty=difficulty)
    except ValueError as error:
        print(error)
        return 2

    print("\n\n".join(format_exercise(exercise) for exercise in exercises))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
