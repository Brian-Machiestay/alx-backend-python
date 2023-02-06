#!/usr/bin/env python3
""" python async function"""


import asyncio
import random


async def wait_random(max_delay=10):
    """waits for a random delay"""
    rand_wait = random.uniform(0, max_delay)
    await asyncio.sleep(rand_wait)
    return (rand_wait)
