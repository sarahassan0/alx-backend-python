#!/usr/bin/env python3
""" task_wait_n function"""

import asyncio
from typing import List
task_wait_random = __import__("3-tasks").task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    task_wait_n
    @n: times to call wait_random
    @max_delay: max delay of wait_random
    Return: list of all delays
    """

    coroutines = [task_wait_random(max_delay) for co in range(n)]
    delays: List[float] = [await c for c in asyncio.as_completed(coroutines)]
    return delays
