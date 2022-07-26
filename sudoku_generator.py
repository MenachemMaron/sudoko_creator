import random

NUMS = [1, 2, 3, 4, 5, 6, 7, 8, 9]
board = [
        [
            0, 0, 0, 0, 0, 0, 0, 0, 0
        ], [
            0, 0, 0, 0, 0, 0, 0, 0, 0
        ], [
            0, 0, 0, 0, 0, 0, 0, 0, 0
        ], [
            0, 0, 0, 0, 0, 0, 0, 0, 0
        ], [
            0, 0, 0, 0, 0, 0, 0, 0, 0
        ], [
            0, 0, 0, 0, 0, 0, 0, 0, 0
        ], [
            0, 0, 0, 0, 0, 0, 0, 0, 0
        ], [
            0, 0, 0, 0, 0, 0, 0, 0, 0
        ], [
            0, 0, 0, 0, 0, 0, 0, 0, 0
        ]
    ]


def add_num(current_board, num):
    count = 0
    tries = 0
    comp_num = False

    while not comp_num:
        row = random.choice(range(9))
        column = random.choice(range(9))
        if board[row][column] == 0:
            row_clear = True
            column_clear = True
            for board_row in board:
                if board_row[column] == num:
                    column_clear = False
                    tries += 1
            if num in board[row]:
                row_clear = False
                tries += 1

            # add check to see if it's in the square

            if row_clear and column_clear:
                board[row][column] = num
                print(f'assigned value at {row}:{column}')
                count += 1

        if tries > 100000:
            print('failed')
            return False, current_board

        if not count < 9:
            return True, current_board


def gen_board():
    new_board = board
    history = []

    for num in range(1, 10):
        attempt_count = 0

        attempt = add_num(new_board, num)

        while not attempt[0]:
            attempt_count += 1
            attempt = add_num(new_board, num)

            if attempt_count > 10:
                print(history)
                # new_board = history[num-2]
                #
                # attempt_count = 0
                break

        new_board = attempt[1]
        history.append(new_board.copy())

    print(new_board)
    print(history)


def main():
    gen_board()


if __name__ == '__main__':
    main()
