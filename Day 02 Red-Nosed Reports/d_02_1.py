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
        print(integer_row)
        dif_list = get_dif_list(integer_row)
        if report_save_checker(dif_list):
            save_reports_counter += 1
    return save_reports_counter


def get_dif_list(integers: list[int]) -> list[int]:
    dif_integers = []
    for pointer in range(len(integers) - 1):
        dif_integers.append((integers[pointer + 1] - integers[pointer]))
    return dif_integers


def report_save_checker(integer_list: list[int]) -> bool:
    integer_list_abs = [abs(number) for number in integer_list]

    # check on monotonic:
    if abs(sum(integer_list)) != sum(integer_list_abs):
        print("not monotonic")
        return False

    # check on strict monotonic:
    if 0 in integer_list:
        print("has 0")
        return False

    # check on max increasing:
    if max(integer_list_abs) > 3:
        print("to big jump")
        return False

    print("save")
    return True


integer_rows = read_rows_from_file(input_path)
print(count_save_reports(integer_rows))
