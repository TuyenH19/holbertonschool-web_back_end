#!/usr/bin/python3
"""Duck type an iterable object"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Takes a list of sequences and returns a list of tuples
    where each tuple contains a sequence from the input list and its length."""
    return [(i, len(i)) for i in lst]
