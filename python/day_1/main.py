"""
day 1 exercise
"""
import logging
from typing import Union
from os import PathLike

logger = logging.getLogger(__name__)


def parse_input(filename: Union[str, bytes, PathLike[str]]) -> list[int]:
    """
    parses input txt file to list of int
    :param filename: str or file other way to open a file with the open statement
    :return:
    """
    input_list: list[int] = []
    with open(filename, "r", encoding="ascii") as i_f:
        for line in i_f:
            try:
                input_list.append(int(line))
            except ValueError:
                logger.error("could not parse line as int, line %s", line)
    return input_list


def create_sliding_window(in_list: list[int]) -> list[int]:
    """
    creates sliding windows from input list, reduces list length by 2 ( first 2 entries are not computable)
    :param in_list:
    :return:
    """
    windows = []
    for i in range(len(in_list) - 2):
        windows.append(sum(in_list[i:i + 3]))
    return windows


def solve_1_1(input_file="input_1_1.txt") -> int:
    """
    solves day 1 ex 1
    :return:
    """
    input_list = parse_input(input_file)
    result = 0

    for i in range(len(input_list)):
        if i != 0:
            if input_list[i] > input_list[i - 1]:
                result += 1
    return result


def solve_1_2(input_file="input_1_2.txt") -> int:
    """
    solves day 1 ex 2
    :return:
    """
    windows = create_sliding_window(parse_input(input_file))
    result = 0
    for i in range(len(windows)):
        if i != 0:
            if windows[i] > windows[i - 1]:
                result += 1
    return result


if __name__ == '__main__':
    print(f"example1 : {solve_1_1(input_file='example_1_1.txt')}")
    print(f"exercise1: {solve_1_1(input_file='input_1_1.txt')}")
    print(f"example2 : {solve_1_2(input_file='example_1_2.txt')}")
    print(f"exercise2: {solve_1_2(input_file='input_1_2.txt')}")
