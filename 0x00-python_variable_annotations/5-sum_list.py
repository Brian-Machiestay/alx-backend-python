#!/usr/bin/env python3
"""anotated takes list of float and returns sum"""


from typing import List


def sum_list(input_list: List[float]) -> float:
    """takes a list of floats and return the float sum"""
    summ: float = 0
    for i in input_list:
        summ += i
    return (summ)
