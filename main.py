'''
    A brute force 9x9 sudoku solver using backtracking algorithm
    This algorithm assumes there is only one possible solution to given board
    if not it prints all solutions
    if you want to print just one solution update solve function as:

    def solve(b):
    pos = find_next_blank_position(b)
    if pos == None:
        print_result(b)
        return True
    for val in range(1, 10):
        if validation(pos, val, b):
            fill_blank(pos, val, b)
            if solve(b):
                return True
            else:
                make_blank(pos, b)

    return False
'''


# Board Definitions:
BOARD0 = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]
]

BOARDX = [
    [1, 2, 3, 4, 5, 6, 7, 8, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 2],
    [0, 0, 0, 0, 0, 0, 0, 0, 3],
    [0, 0, 0, 0, 0, 0, 0, 0, 4],
    [0, 0, 0, 0, 0, 0, 0, 0, 5],
    [0, 0, 0, 0, 0, 0, 0, 0, 6],
    [0, 0, 0, 0, 0, 0, 0, 0, 7],
    [0, 0, 0, 0, 0, 0, 0, 0, 9]
]


BOARD = [
    [2, 7, 4, 0, 9, 1, 0, 0, 5],
    [1, 0, 0, 5, 0, 0, 0, 9, 0],
    [6, 0, 0, 0, 0, 3, 2, 8, 0],
    [0, 0, 1, 9, 0, 0, 0, 0, 8],
    [0, 0, 5, 1, 0, 0, 6, 0, 0],
    [7, 0, 0, 0, 8, 0, 0, 0, 3],
    [4, 0, 2, 0, 0, 0, 0, 0, 9],
    [0, 0, 0, 0, 0, 0, 0, 7, 0],
    [8, 0, 0, 3, 4, 9, 0, 0, 0]
]

BOARDZ = [
     [0, 0, 5, 3, 0, 0, 0, 0, 0],
     [8, 0, 0, 0, 0, 0, 0, 2, 0],
     [0, 7, 0, 0, 1, 0, 5, 0, 0],
     [4, 0, 0, 0, 0, 5, 3, 0, 0],
     [0, 1, 0, 0, 7, 0, 0, 0, 6],
     [0, 0, 3, 2, 0, 0, 0, 8, 0],
     [0, 6, 0, 5, 0, 0, 0, 0, 9],
     [0, 0, 4, 0, 0, 0, 0, 3, 0],
     [0, 0, 0, 0, 0, 9, 7, 0, 0]
]

def print_result(b):
    for r in range(9):
        if r % 3 == 0 and r != 0:
            print('- - - - - - - - - -')
        for c in range(9):
            if c % 3 == 0 and c!= 0:
                print('|', end="")
            print(str(b[r][c]) + ' ', end="")
        print()


def find_next_blank_position(b):
    for r in range(9):
        for c in range(9):
            if(b[r][c]==0):
                return (r,c)
    return None # no empty square


def validation(pos, val, b):
    # validation of the rows
    for item in range(9):
        if b[pos[0]][item] == val and item != pos[1]:
            return False

    #validation of columns
    for item in range(9):
        if b[item][pos[1]] == val and item != pos[0]:
            return False

    #validation of boxes
    # box array = [
    #     [0,0],
    #     [0,1],
    #     [0,2],
    #     [1,0],
    #     [1,1],
    #     [1,2],
    #     [2,0],
    #     [2,1],
    #     [2,2]
    # ]

    #box's row and column position in box array with integer division
    box_r = (pos[0] // 3)
    box_c = (pos[1] // 3)

    for r in range(3*box_r, 3*box_r + 3):
        for c in range(3*box_c, 3*box_c + 3):
            if b[r][c] == val and pos != (r,c):
                return False

    # all criteria passed then the val is valid:
    return True

def fill_blank(pos, val, b):
    b[pos[0]][pos[1]] = val

def make_blank(pos, b):
    b[pos[0]][pos[1]] = 0

def solve(b):
    pos = find_next_blank_position(b)
    if pos == None:
        print_result(b)
        return True
    for val in range(1, 10):
        if validation(pos, val, b):
            fill_blank(pos, val, b)
            solve(b)

            make_blank(pos, b)
    # this false triggers backtracking and makes above else condition valid to make the previos filled square blank
    return False
