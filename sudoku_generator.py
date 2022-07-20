import random

NUMS = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def gen_board():
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

    temp_nums = NUMS
    for i in range(1, 10):
        current_num = random.choice(temp_nums)
        temp_nums.remove(current_num)
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
                    if board_row[column] == current_num:
                        column_clear = False
                        tries += 1
                if current_num in board[row]:
                    row_clear = False
                    tries += 1

                # add check to see if it's in the square

                if row_clear and column_clear:
                    board[row][column] = current_num
                    count += 1
                    row_clear = False
                    column_clear = False

            if tries > 100000:
                print('failed')
                break

            if not count < 9:
                comp_num = True

    print(board)
    # print(board_history)


def main():
    gen_board()


if __name__ == '__main__':
    main()
