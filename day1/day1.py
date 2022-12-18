
"""
Day 1
"""

def get_calories(filename: str) -> list[int]:
    """
    the Elves would instead like to know the total Calories carried by the
    top three Elves carrying the most Calories.
    """
    calories = []
    accumulator = 0

    data = open(filename, "r").readlines()
    data = [x.strip() for x in data]

    for line in data:
        if line == "" :
            calories.append(accumulator)
            accumulator = 0
        else :
            accumulator = accumulator + int(line)

        if line != "" :
            calories.append(accumulator)
    return calories

if __name__ == "__main__":
    get_calories('day1/input.txt')
