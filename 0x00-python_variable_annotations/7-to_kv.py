#!/usr/bin/env python3

""" to_kv function"""
from typing import Union, Tuple

union_var = Union[int, float]
mixed_tuple = Tuple[str, float]


def to_kv(k: str, v: union_var) -> mixed_tuple:
    """ returns a tuple """
    return (k, v**)
