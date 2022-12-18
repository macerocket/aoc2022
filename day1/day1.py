
"""
Day 1
"""

def get_max_calories(filename: str) -> int:
    """
    Get the elf with the maximum calries from the input file
    """
    maximum = 0
    accumulator = 0

    data = open(filename, "r").readlines()
    data = [x.strip() for x in data]

    for line in data:
        if line == "" :
            if accumulator > maximum:
                maximum = accumulator
            accumulator = 0
        else :
            accumulator = accumulator + int(line)

    return maximum

if __name__ == "__main__":
    get_max_calories('day1/input.txt')
