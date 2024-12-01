from typing import List, Tuple
from collections import Counter

# input_path = "Day 01 Historian Hysteria/input_example.txt"
input_path = "Day 01 Historian Hysteria/input_my_puzzle.txt"


def read_2_int_columns_textfile(path: str) -> tuple[list[int], list[int]]:
    """Reads a file with two integer columns separated by whitespace."""
    with open(path) as input_file:
        raw_string = input_file.read()
    list_left, list_right = [], []

    for line in raw_string.split("\n"):
        if line:
            first_str, second_str = line.split("   ")
            first_int, second_int = int(first_str), int(second_str)
            list_left.append(first_int)
            list_right.append(second_int)
    return list_left, list_right


def calculate_weighted_sum(column_data: Tuple[List[int], List[int]]) -> int:
    """Calculates the weighted sum of occurrences of integers in two columns."""
    counts_left = Counter(column_data[0])
    counts_right = Counter(column_data[1])

    weighted_sum = sum(
        counts_left[key] * counts_right[key] * key
        for key in counts_left.keys() & counts_right.keys()
    )
    return weighted_sum


int_columns = read_2_int_columns_textfile(input_path)

print(calculate_weighted_sum(int_columns))
