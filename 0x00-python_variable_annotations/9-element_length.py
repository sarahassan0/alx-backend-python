#!/usr/bin/env python3

""" element_length function"""
from typing import List, Tuple, Iterable, Sequence

tuples_list = List[Tuple[Sequence, int]]


def element_length(lst: Iterable[Sequence]) -> tuples_list:
    """ return list of tuples contains the ele and it's length """
    return [(i, len(i)) for i in lst]
