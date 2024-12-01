from typing import List, Tuple

input_path = "Day 01 Historian Hysteria/input_example.txt"
#input_path = "Day 01 Historian Hysteria/input_my_puzzle.txt"


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


def calculate_sum_of_differences(list_left: list[int], list_right: list[int]) -> int:
    """Calculates the sum of absolute differences between two columns."""
    sum_of_difference = 0
    for left, right in zip(list_left, list_right):
        sum_of_difference += abs(left - right)
    return sum_of_difference


def sort_2_int_columns(
    list_left: list[int], list_right: list[int]
) -> tuple[list[int], list[int]]:
    """Sorts the columns together by their first column."""
    list_left.sort()
    list_right.sort()
    return list_left, list_right

int_columns = read_2_int_columns_textfile(input_path)

sorted_columns = sort_2_int_columns(*int_columns)

print(calculate_sum_of_differences(*sorted_columns))
