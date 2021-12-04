from os import PathLike
from typing import Union
import re


class Board:
    regex_split = re.compile("[\s\\n]+")

    def __init__(self, in_strs: list[str]):
        rows = []
        for line in in_strs:
            rows.append([int(x) for x in self.regex_split.split(line)])
        self.rows = rows
        self.field_size = 5
        self.marks = []
        for _ in range(self.field_size):
            self.marks.append([False] * self.field_size)
        self.finished = False
        self.numbers = []

    def evaluate_board(self, drawn_number):
        self.numbers.append(drawn_number)
        for i_r, row in enumerate(self.rows):
            try:
                index = row.index(drawn_number)
                self.marks[i_r][index] = True
            except ValueError:
                continue
        self.finished = self.__check_row() or self.__check_column()
        return self.finished

    def __check_row(self):
        for row in self.marks:
            row_true = True
            for e in row:
                row_true = e & row_true
            if row_true:
                return True
        return False

    def __check_column(self):
        for i_column in range(self.field_size):
            column = []
            for row in self.marks:
                column.append(row[i_column])
            column_true = True
            for e in column:
                column_true = e & column_true
            if column_true:
                return True
        return False

    def get_score(self):
        if self.finished:
            base_score = 0
            for i in range(self.field_size):
                for j in range(self.field_size):
                    if not self.marks[i][j]:
                        base_score += self.rows[i][j]

            return base_score *self.numbers[-1]
        else:
            return 0

    def __repr__(self):

        b_string = "\n".join([str(r) for r in self.rows])
        m_string = "\n".join([str(r) for r in self.marks])
        return f"Board:\n{b_string}\n{m_string}\npoints: {self.get_score()}"


def load_board(filename: Union[str, PathLike]):
    with open(filename, "r", encoding="ascii") as in_file:
        draw_order: str = next(in_file)
        draw_order: list[int] = [int(x) for x in draw_order.split(",")]
        boards = []
        in_strings = []
        for line in in_file:
            if line.rstrip() == "":
                if len(in_strings) == 5:
                    boards.append(Board(in_strings))
                in_strings = []
            else:
                in_strings.append(line.rstrip().lstrip())
        boards.append(Board(in_strings))
    return boards, draw_order
