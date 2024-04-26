#!/usr/bin/env python3
"""A complex types-annotated to transfer string and int/float to tuple."""

from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Return a tuble of string and float."""
    return [k, v*v]
