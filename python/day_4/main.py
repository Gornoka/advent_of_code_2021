import Bingo

if __name__ == '__main__':
    boards, draw_order = Bingo.load_board("exercise_4_1.txt")
    boards_finished = False

    for n in draw_order:
        for b in boards:
            b_finished = b.evaluate_board(n)
            boards_finished = boards_finished or b_finished
        if boards_finished:
            break
    for b in boards:
        if b.finished:
            print(f"the winner is {b}")
            pass
    print("exercise 2")
    finished_boards = 0
    boards, draw_order = Bingo.load_board("exercise_4_1.txt")
    n_boards = len(boards)
    for n in draw_order:
        for b in boards:
            if b.finished:
                continue
            b_finished = b.evaluate_board(n)
            if b_finished:
                finished_boards += 1
                if finished_boards ==n_boards:
                    print(f"the looser is {b}")


