"""
The first column is what your opponent is going to play: A for Rock, B for Paper, 
and C for Scissors. The second column--" Suddenly, the Elf is called away to 
help with someone's tent.

The second column, you reason, must be what you should play in response: 
X for Rock, Y for Paper, and Z for Scissors. Winning every time would be 
suspicious, so the responses must have been carefully chosen.

For part 2:
-----------
The second column says how the round needs to end: 
    X means you need to lose, 
    Y means you need to end the round in a draw, and 
    Z means you need to win.

The winner of the whole tournament is the player with the highest score. 
Your total score is the sum of your scores for each round. The score for 
a single round is the score for the shape you selected 
    (1 for Rock, 2 for Paper, and 3 for Scissors) 
plus the score for the outcome of the round 
    (0 if you lost, 3 if the round was a draw, and 6 if you won).
"""

WIN = "win"
LOSE = "lose"
DRAW = "draw"

OPPONENT_ROCK = "A"
OPPONENT_PAPER = "B"
OPPONENT_SCISSORS = "C"

ROCK = "X"
PAPER = "Y"
SCISSORS = "Z"

def get_winner(opponent_play: str, my_play: str) -> str:
    """
    Calculate who wins a game of roshambo
    """
    if opponent_play == OPPONENT_ROCK:
        if my_play == PAPER:
            return WIN
        if my_play == ROCK:
            return DRAW
    if opponent_play == OPPONENT_PAPER:
        if my_play == SCISSORS:
            return WIN
        if my_play == PAPER:
            return DRAW
    if opponent_play == OPPONENT_SCISSORS:
        if my_play == ROCK:
            return WIN
        if my_play == SCISSORS:
            return DRAW
    return LOSE

def calculate_score(outcome: str, played: str) -> int:
    """
    (1 for Rock, 2 for Paper, and 3 for Scissors)
        plus the score for the outcome of the round
    (0 if you lost, 3 if the round was a draw, and 6 if you won)

    """
    score = 0
    if outcome == WIN:
        score += 6
    if outcome == DRAW:
        score += 3
    if played == ROCK or played == OPPONENT_ROCK:
        score += 1
    if played == PAPER or played == OPPONENT_PAPER:
        score += 2
    if played == SCISSORS or played == OPPONENT_SCISSORS:
        score += 3
    return score

def get_total_score(filename: str) -> int:
    """
    For each line of the input, we need to determine the winner
    then calculate the score and add it to the running total
    returning the grand total at the end
    """
    data = open(filename, "r").readlines()
    data = [x.strip() for x in data]

    grand_total:int = 0

    for line in data:
        (opponent_played, i_played) = line.split(" ")
        outcome:str = get_winner(opponent_played, i_played)
        grand_total += calculate_score(outcome, i_played)

    return grand_total


def get_correct_play(opponent_play: str, required_outcome: str) -> str:
    """
    Calculate what to play to acheive the desired outcome of a game of roshambo
    X means you need to lose, 
    Y means you need to end the round in a draw, and 
    Z means you need to win.

    """
    WIN = "Z"
    LOSE = "X"
    DRAW = "Y"
    if opponent_play == OPPONENT_ROCK:
        if required_outcome == WIN:
            return PAPER
        if required_outcome == DRAW:
            return ROCK
        if required_outcome == LOSE:
            return SCISSORS
    if opponent_play == OPPONENT_PAPER:
        if required_outcome == WIN:
            return SCISSORS
        if required_outcome == DRAW:
            return PAPER
        if required_outcome == LOSE:
            return ROCK
    if opponent_play == OPPONENT_SCISSORS:
        if required_outcome == WIN:
            return ROCK
        if required_outcome == DRAW:
            return SCISSORS
        if required_outcome == LOSE:
            return PAPER


def get_total_score_part2(filename: str) -> int:
    """
    For each line of the input, we need to determine the correct play
    then calculate the score and add it to the running total
    returning the grand total at the end
    """
    data = open(filename, "r").readlines()
    data = [x.strip() for x in data]

    grand_total:int = 0

    for line in data:
        (opponent_played, outcome) = line.split(" ")
        if outcome == "X":
            required_outcome = LOSE
        if outcome == "Y":
            required_outcome = DRAW
        if outcome == "Z":
            required_outcome = WIN
        
        correct_play:str = get_correct_play(opponent_played, outcome)
        grand_total += calculate_score(required_outcome, correct_play)

    return grand_total

