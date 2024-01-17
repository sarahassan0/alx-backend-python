#!/usr/bin/env python3
""" async_comprehension function """

import asyncio
import random
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """ collect random numbers using async_generator, and return them"""

    return [i async for i in async_generator()]
