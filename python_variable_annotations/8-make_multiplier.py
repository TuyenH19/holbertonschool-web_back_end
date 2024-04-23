#!/usr/bin/env python3
"""A complex types-annotated function make_multiplier"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Takes a float multiplier as an argument and returns a function that
    multiplies a float by the multiplier."""
    def multiplier_function(x: float) -> float:
        return x * multiplier
    return multiplier_function
