"""
Tests for day 2 AOC2022
"""

from day2 import WIN, LOSE, DRAW, ROCK, PAPER, SCISSORS, get_winner, \
    calculate_score, get_total_score, get_correct_play, get_total_score_part2

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
    assert calculate_score(WIN, ROCK) == 7
    assert calculate_score(DRAW, PAPER) == 5
    assert calculate_score(LOSE, SCISSORS) == 3

def test_get_correct_play():
    """
    Test the get_correct_play function
    A for Rock, B for Paper, and C for Scissors
    X for Rock, Y for Paper, and Z for Scissors

    X means you need to lose, 
    Y means you need to end the round in a draw, and 
    Z means you need to win
    """
    assert get_correct_play("A", "X") == "Z"
    assert get_correct_play("A", "Z") == "Y"
    assert get_correct_play("B", "Z") == "Z"
    assert get_correct_play("C", "X") == "Y"

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

def test_day2_part2(capsys):
    """
    Test for getting the actual value for day 2 part 2
    """
    with capsys.disabled():
        print(f"Answer for day 2 part 2: {get_total_score_part2('day2/input.txt')}")

