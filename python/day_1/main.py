import logging


def parse_input(filename):
    """
    parses input txt file to list of int
    :param filename:
    :return:
    """
    input_list: list[int] = []
    with open(filename, "r") as i_f:
        for line in i_f:
            try:
                input_list.append(int(line))
            except ValueError:
                logging.error(f"could not parse line as int, line {line}")
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
    for ii in range(len(input_list)):
        if ii != 0:
            if input_list[ii] > input_list[ii - 1]:
                result += 1
    return result


def solve_1_2(input_file="input_1_2.txt"):
    """
    solves day 1 ex 2
    :return:
    """
    windows = create_sliding_window(parse_input(input_file))
    result = 0
    for ii in range(len(windows)):
        if ii != 0:
            if windows[ii] > windows[ii - 1]:
                result += 1
    return result


if __name__ == '__main__':
    print(f"example1 : {solve_1_1(input_file='example_1_1.txt')}")
    print(f"exercise1: {solve_1_1(input_file='input_1_1.txt')}")
    print(f"example2 : {solve_1_2(input_file='example_1_2.txt')}")
    print(f"exercise2: {solve_1_2(input_file='input_1_2.txt')}")
