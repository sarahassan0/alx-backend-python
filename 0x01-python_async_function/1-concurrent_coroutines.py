#!/usr/bin/env python3
""" execute multiple coroutines at the same time with async"""

import asyncio
from typing import List
wait_random = __import__("0-basic_async_syntax").wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    @n: times to call wait_random
    @max_delay: max delay of wait_random
    Return: list of all delays
    """
    coroutines = [wait_random(max_delay) for co in range(n)]
    delays: List[float] = [await c for c in asyncio.as_completed(coroutines)]
    return delays

    # Another sloution using sorted() function

    # co = await asyncio.gather(*(wait_random(max_delay) for c in range(n)))
    # return sorted(co)
