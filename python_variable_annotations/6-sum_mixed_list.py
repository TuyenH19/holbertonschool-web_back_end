#!/usr/bin/env python3
"""A complex types-annotated function mixed_list"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Return a float from summing a list of int and float."""
    return sum(mxd_lst)
