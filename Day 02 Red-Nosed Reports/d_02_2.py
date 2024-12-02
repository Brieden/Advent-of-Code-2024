from typing import List, Tuple

# input_path = "Day 02 Red-Nosed Reports/input_example.txt"
input_path = "Day 02 Red-Nosed Reports/input_my_puzzle.txt"


def read_rows_from_file(path: str) -> list[list[int]]:
    """Reads a file with integer rows separated by whitespace."""
    with open(path) as input_file:
        raw_string = input_file.read()
    list_rows = []
    for line in raw_string.split("\n"):
        if line:
            list_rows.append([int(number) for number in line.split()])
    return list_rows


def count_save_reports(integer_rows: list[list[int]]) -> int:
    """Counts the number of reports that are saved.
    Save is defined as a full list of monotonic de- or increasing by 1, 2, or 3"""
    save_reports_counter = 0
    for integer_row in integer_rows:
        if report_save_checker(integer_row):
            save_reports_counter += 1
    return save_reports_counter


def make_permutations(integers: list[int]) -> list[list[int]]:
    permutations = [integers]
    for position in range(len(integers)):
        permutations.append(integers[:position] + integers[position + 1 :])
    return permutations


def get_dif_list(integers: list[int]) -> list[int]:
    dif_integers = []
    for pointer in range(len(integers) - 1):
        dif_integers.append((integers[pointer + 1] - integers[pointer]))
    return dif_integers


def report_save_checker(integer_list: list[int]) -> bool:

    permutations = make_permutations(integer_list)
    for permutation in permutations:
        dif_list = get_dif_list(permutation)
        dif_list_abs = [abs(number) for number in dif_list]
        # check on monotonic:
        if abs(sum(dif_list)) != sum(dif_list_abs):
            print("not monotonic")
            continue

        # check on strict monotonic:
        if 0 in dif_list:
            print("has 0")
            continue

        # check on max increasing:
        if max(dif_list_abs) > 3:
            print("to big jump")
            continue

        print("save")
        return True


integer_rows = read_rows_from_file(input_path)
print(count_save_reports(integer_rows))
