import logging
import random
import string
import time
from typing import Union
from os import PathLike


class MisunderstoodSubmarine:
    def __init__(self, initial_depth=0, initial_forward=0, name=None):
        """
        submarine with misunderstood controls
        :param initial_depth:
        :param initial_forward:
        :param name:
        """
        self.depth = initial_depth
        self.forward_location = initial_forward

        if name is None:
            self.name = f"{''.join([random.choice(string.ascii_uppercase) for _ in range(3)])}-{random.randint(0, 1337)}"

    @property
    def distance(self) -> int:
        """
        calculate total distance
        :return:
        """
        return self.depth * self.forward_location

    def __repr__(self) -> str:
        """
        nice name for sub
        :return:
        """
        return f"Submarine {self.name} at {self.forward_location}, {self.depth} below the sea, {self.distance} away"

    def up(self, distance: int) -> None:
        """
        move up
        :param distance:
        :return:
        """
        self.depth -= distance

    def down(self, distance: int) -> None:
        """
        move down
        :param distance:
        :return:
        """
        self.depth += distance

    def forward(self, distance: int) -> None:
        """
        move forward
        :param distance:
        :return:
        """
        self.forward_location += distance

    def backwards(self, distance: int) -> None:
        """
        subs can't move back do not try
        :param distance:
        :return:
        """
        raise ValueError("Submarines can not drive backwards")
        # self.forward_location -= distance

    def move_from_input(self, input_file: Union[str, bytes, PathLike[str]]) -> None:
        """
        parses input and moves the sub
        :param input_file:
        :return:
        """
        operations = {"forward": self.forward,
                      "up": self.up,
                      "down": self.down}
        with open(input_file, "r") as i_f:
            for line in i_f:
                line: str
                direction, distance = line.split(" ")
                try:
                    operations[direction](int(distance))
                except KeyError:
                    logging.error(f"direction not implemented {direction}")
        logging.info(f"location {self.forward_location} {self.depth}")


class Submarine(MisunderstoodSubmarine):

    def __init__(self, initial_depth: int = 0, initial_forward: int = 0, initial_aim: int = 0):
        """
        better understand sub
        :param initial_depth:
        :param initial_forward:
        :param initial_aim:
        """
        super().__init__(initial_depth, initial_forward)
        self.aim = initial_aim

    def down(self, aim_change: int) -> None:
        """
        aim down
        :param aim_change:
        :return:
        """
        self.aim += aim_change

    def up(self, aim_change: int) -> None:
        """
        aim up
        :param aim_change:
        :return:
        """
        self.aim -= aim_change

    def forward(self, distance: int) -> None:
        """
        move forwards, this results in depth change according to aim,
        not safe to move sub out of the water
        :param distance:
        :return:
        """
        self.forward_location += distance
        self.depth += distance * self.aim
        if self.depth < 0:
            raise ValueError(f"negative depth of: {self.depth}  Subs can't fly!!!")
