"""
day 2 exercise
"""
try:
    from .Submarine import Submarine, MisunderstoodSubmarine
except ImportError:
    from Submarine import Submarine, MisunderstoodSubmarine
if __name__ == '__main__':
    # 2_1
    print("day 2 ex 1")
    example_sub = MisunderstoodSubmarine()
    example_sub.move_from_input("./example_2_1.txt")
    print(example_sub)
    exercise_sub = MisunderstoodSubmarine()
    exercise_sub.move_from_input("./input_2_1.txt")
    print(exercise_sub)
    # 2_2
    print("day 2 ex 2")
    example_sub_2 = Submarine()
    example_sub_2.move_from_input("./example_2_2.txt")
    print(example_sub_2)
    exercise_sub_2 = Submarine()
    exercise_sub_2.move_from_input("./input_2_2.txt")
    print(exercise_sub_2)
