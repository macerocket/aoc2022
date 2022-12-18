
"""
Day 1
"""
import pandas as pd

def get_length(filename: str) -> int:
    """
    Get the length of the input
    """
    aoc_df = pd.read_csv(filename)
    return len(aoc_df)

if __name__ == "__main__":
    get_length('day1/input.txt')
