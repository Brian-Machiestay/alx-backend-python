#!/usr/bin/env python3
"""redeclare a function with annotations"""


from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """redeclare a function with annotations"""
    return [(i, len(i)) for i in lst]
