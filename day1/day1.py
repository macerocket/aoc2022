
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
        if line != "" :
            accumulator = accumulator + int(line)
        else :
            calories.append(accumulator)
            accumulator = 0

    # If the last line was not empty, push the last accumulated
    # calorie count onto the array
    if len(data) > 0 and line != "" :
        calories.append(accumulator)

    return calories

if __name__ == "__main__":
    get_calories('day1/input.txt')
