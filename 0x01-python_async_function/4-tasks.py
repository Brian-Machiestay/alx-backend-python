#!/usr/bin/env python3
"""modify wait_n to task_wait_n"""


import asyncio
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """spawn wait random n times and return all floats returned"""
    tasks: List = []

    for i in range(n):
        tasks.append(wait_random(max_delay))

    allfloats: List[float] = []
    for coro in asyncio.as_completed(tasks):
        allfloats.append(await coro)
    return allfloats
