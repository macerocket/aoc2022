"""
Tests for day 1 AOC2022
"""

from day1 import get_calories

def test_get_max_calories():
    """
    Test for get_max_calories function
    """
    assert sorted(get_calories('day1/test_input.txt'))[-1] == 9


def test_day1_part1(capsys):
    """
    Test for getting the actual value for day 1 part 1
    """
    with capsys.disabled():
        print(f"Answer for day 1 part1: {sorted(get_calories('day1/input.txt'))[-1]}")

def test_day1_part2(capsys):
    """
    Print the sum of the top 3 calorie carriers
    """
    calories = sorted(get_calories('day1/input.txt'))
    top_three = calories[-1] + calories[-2] + calories[-3]

    with capsys.disabled():
        print(f"Answer for day 1 part 2: {top_three}")
