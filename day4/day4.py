import fileinput
from copy import deepcopy


def main():
    boards = []
    draws = list(map(int, list(fileinput.input())[0].rstrip().split(",")))

    count = 5

    for line in fileinput.input():
        if line != '\n':
            line = line.rstrip().split(" ")
            for i in range(line.count("")):
                line.remove("")

            if len(line) == 5:
                line = list(map(int, line))
                if count == 5:
                    boards.append(list())
                boards[-1].append(line)
                count -= 1
                if count == 0:
                    count = 5
    bingo(draws, boards)


def bingo(draws, boards):
    for d in draws:
        for b in range(len(boards)):
            if b > len(boards) - 1:
                break
            check_board(boards, d, b)


def check_board(boards, d, b):
    for ln in range(len(boards[b])):
        if boards[b][ln].count(d) != 0:
            boards[b][ln][boards[b][ln].index(d)] = "x"
            if "".join(map(str, boards[b][ln])) == "xxxxx":
                print("bingo horizantal at value",
                      d, "in board", boards[b])
                print_sum(deepcopy(boards[b]), d)
                boards[b] = []
                return

    bingo_str = []
    for ln in range(len(boards[b])):
        for c in range(len(boards[b])):
            bingo_str.append(boards[b][c][ln])
        if bingo_str.count(d) != 0:
            boards[b][bingo_str.index(d)][ln] = "x"
            bingo_str[bingo_str.index(d)] = "x"
        if "".join(map(str, bingo_str)) == "xxxxx":
            print("bingo vertical at value",
                  d, "in board", boards[b])
            print_sum(deepcopy(boards[b]), d)
            boards[b] = []
            return
        bingo_str = []


def print_sum(board, d):
    total = 0
    board = list(map(turn_int, board))
    for i in range(len(board)):
        total += sum(board[i])
    print("the sum of the rest of the board time draw is", total*d)


def turn_int(board):
    for i in range(len(board)):
        if type(board[i]) == str:
            board[i] = 0
    return board


if __name__ == "__main__":
    main()
