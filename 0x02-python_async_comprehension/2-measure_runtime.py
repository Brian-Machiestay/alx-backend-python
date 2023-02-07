#!/usr/bin/env python3
"""measure the running time of asynchronous functions"""


import time
import asyncio
from typing import List


async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """measure the running time of async functions"""
    lst_com: List = []
    for i in range(4):
        lst_com.append(async_comprehension())
    start: float = time.perf_counter()
    await asyncio.gather(*lst_com)
    return time.perf_counter() - start
