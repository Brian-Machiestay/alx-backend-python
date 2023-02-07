#!/usr/bin/env python3
"""async generator comprehension and annotations"""


from typing import AsyncGenerator
import random
import asyncio


async def async_generator() -> AsyncGenerator[float, None]:
    """asynchronous generators and comprehension"""
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
