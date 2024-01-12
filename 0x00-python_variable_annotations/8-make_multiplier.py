#!/usr/bin/env python3

""" make_multiplier function """
from typing import Callable

maltiply_func = Callable[[float], float]


def make_multiplier(multiplier: float) -> maltiply_func:
    """ returns a function that multiplies a float by multiplier """
    return lambda n: n * multiplier
