#!/usr/bin/env python3
"""Complex types module"""

from typing import List


def sum_list(input_list: List[float],) -> float:
    summation: float = 0
    for i in input_list:
        summation += i
    return summation
