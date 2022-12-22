"""
Tests for day 2 AOC2022
"""

from day2 import WIN, LOSE, DRAW, ROCK, PAPER, SCISSORS, get_winner, \
    calculate_score, get_total_score

def test_get_winner():
    """
    Test for get_winner function
    """
    assert get_winner("A", "X") == DRAW
    assert get_winner("A", "Y") == WIN
    assert get_winner("A", "Z") == LOSE

def test_calculate_score():
    """
    Test for calculate_score function
    """
    assert(calculate_score(WIN, ROCK) == 7)
    assert(calculate_score(DRAW, PAPER) == 5)
    assert(calculate_score(LOSE, SCISSORS) == 3)

def test_get_summary():
    """
    test reading from input file and caculating all games
    """
    assert get_total_score('day2/test_input.txt') == 15

def test_day2_part1(capsys):
    """
    Test for getting the actual value for day 2 part 1
    """
    with capsys.disabled():
        print(f"Answer for day 2 part1: {get_total_score('day2/input.txt')}")
