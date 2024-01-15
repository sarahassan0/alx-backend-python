#!/usr/bin/env python3
""" measure_time function """

import asyncio
import time
wait_n = __import__("1-concurrent_coroutines").wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    measure total time that wait_n function takes
    
    @n: times to call wait_random
    @max_delay: max delay of wait_random
    Return: total_time / n
    """
    start: float = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    end: float = time.perf_counter()
    return (end - start) / n
