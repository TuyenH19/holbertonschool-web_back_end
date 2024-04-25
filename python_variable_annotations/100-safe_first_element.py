#!/usr/bin/env python3
""" 
Augment the following code with the correct duck-typed annotations:
    The types of the elements of the input are not know
    def safe_first_element(lst):
        if lst:
            return lst[0]
        else:
            return None
"""
from typing import Sequence, Any, Optional


def safe_first_element(lst: Sequence[Any]) -> Optional[Any]:
    """ Duck typing - first element of a sequence """
    if lst:
        return lst[0]
    else:
        return None
