from Submarine import MisunderstoodSubmarine, Submarine

if __name__ == '__main__':
    # 2_1
    print(f"day 2 ex 1")
    example_sub = MisunderstoodSubmarine()
    example_sub.move_from_input("./example_2_1.txt")
    print(example_sub)
    exercise_sub = MisunderstoodSubmarine()
    exercise_sub.move_from_input("./input_2_1.txt")
    print(exercise_sub)
    # 2_2
    print(f"day 2 ex 2")
    example_sub_2 = Submarine()
    example_sub_2.move_from_input("./example_2_2.txt")
    print(example_sub_2)
    exercise_sub_2 = Submarine()
    exercise_sub_2.move_from_input("./input_2_2.txt")
    print(exercise_sub_2)
