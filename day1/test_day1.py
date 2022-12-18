"""
Tests for day 1 AOC2022
"""

import logging
from day1 import get_max_calories

def test_get_max_calories():
    """
    Test for get_max_calories function
    """
    assert get_max_calories('day1/test_input.txt') == 9


def test_day1():
    """
    Test for getting the actual value for day 1
    """
    log = logging.getLogger( "AOC2022.day1" )
    log.debug("Answer for day 1: %s", {get_max_calories('day1/input.txt')})
