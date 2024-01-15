#!/usr/bin/env python3
""" task_wait_random function """
import asyncio
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
        creates and return asyncronse task
        
        @max_delay: max delay of wait_random
        Return: asyncio.Task
    """
    return asyncio.Task(wait_random(max_delay))
