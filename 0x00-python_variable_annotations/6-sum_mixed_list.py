#!/usr/bin/env python3
"""sum of a mixed list"""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """takes a mixed list of inputs and returns a float"""
    summ: float = 0.0
    for i in mxd_lst:
        summ += i
    return (summ)
