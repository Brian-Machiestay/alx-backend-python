#!/usr/bin/env python3
"""annonated function to_kv"""


from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """annotated function to kv"""
    return ((k, v * v))
