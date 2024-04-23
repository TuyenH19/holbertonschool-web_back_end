#!/usr/bin/env python3
"""A complex types-annotated function sum_list"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """Return a float from summing a list of float."""
    return sum(input_list)
