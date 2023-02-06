#!/usr/bin/env python3
"""take an int and return a task"""


import asyncio
from typing import Callable, Any


wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> Any:
    """return an asyncio task"""
    return asyncio.create_task(wait_random(max_delay))
