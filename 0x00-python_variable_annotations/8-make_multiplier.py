#!/usr/bin/env python3
"""make multiplier annotated function"""


from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """make an annotated multiplier function that returns another"""
    return (lambda x: x * multiplier)
