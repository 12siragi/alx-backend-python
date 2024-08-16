#!/usr/bin/env python3
"""Function that returns a multiplier function."""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Returns a function that multiplies a float by a given multiplier."""


    def multiplier_function(number: float) -> float:
        """Multiplies a float by the multiplier."""
        return multiplier * number

    return multiplier_function
