#!/usr/bin/python3
"""A complex types-annotated to transfer string and int/float to tuple"""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[Union[str, float]]:
    """Return a tuble of string and float."""
    return [k, v ** 2]
