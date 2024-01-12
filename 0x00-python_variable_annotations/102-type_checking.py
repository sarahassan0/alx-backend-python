#!/usr/bin/env python3

""" zoom_array function """

from typing import List, Tuple


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """ the function "zooms in" on each element in the input tuple by
        repeating it a factor number of times """
    zoomed_in: List = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in
