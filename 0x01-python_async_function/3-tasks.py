#!/usr/bin/env python3
"""take an int and return an asyncio task using received value"""


import asyncio
from typing import Any


wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> Any:
    """return an asyncio task using received max delay value"""
    return asyncio.create_task(wait_random(max_delay))
