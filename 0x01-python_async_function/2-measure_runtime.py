#!/usr/bin/env python3
"""measure the runtime of coroutines"""


import asyncio
import time


wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """measure the time when coroutines finish"""
    start: float = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    used_time: float = time.perf_counter() - start
    return (used_time / n)
