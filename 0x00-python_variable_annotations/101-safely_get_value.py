#!/usr/bin/env python3

""" safely_get_value function """

from typing import Union, Any, Mapping, TypeVar

T = TypeVar('T')
default_var = Union[T, None]
union_var = Union[Any, T]


def safely_get_value(dct: Mapping,
                     key: Any, default:
                     default_var = None) -> union_var:
    """ returns the value of the key or none """
    if key in dct:
        return dct[key]
    else:
        return default
