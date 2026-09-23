"""Refactor helpers."""

from typing import Iterable, List


def normalise(values: Iterable[str]) -> List[str]:
    """Strip whitespace and drop empty entries."""
    return [v.strip() for v in values if v and v.strip()]


def describe() -> str:
    return "Refactor utilities"
