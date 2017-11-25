"""
Breadth First Search approach to finding the goal state of the puzzle.
"""

from copy import copy, deepcopy
from sys import getsizeof
from board import *
import globals
import psutil
import time
import os
from heapq import *


def move_up(parent_h, parent_board, curr_board, z_coord, pq, visited):
    """
    :param visited: hashmap to hold visited states
    :param pq: priority queue used to append new states (if necessary)
    :param parent_h: Holds the parent heuristic value
    :param parent_board: Holds the parent board
    :param curr_board: Holds the current child board being evaluate
    :param z_coord: Holds the coordinates of where the blank position is
    :return:
    """

    if z_coord[0] - 1 >= 0:

        tmp = curr_board[z_coord[0] - 1][z_coord[1]]
        curr_board[z_coord[0] - 1][z_coord[1]] = curr_board[z_coord[0]][z_coord[1]]
        curr_board[z_coord[0]][z_coord[1]] = tmp
        cb_as_list = transform_to_string_list(curr_board)

        check_hm(Board(cb_as_list),
                 ' '.join(str(num) for row in parent_board for num in row),
                 parent_h, pq, visited)


def move_down(parent_h, parent_board, curr_board, z_coord, pq, visited):

    if z_coord[0] + 1 < EDGE_LENGTH:
        tmp = curr_board[z_coord[0] + 1][z_coord[1]]
        curr_board[z_coord[0] + 1][z_coord[1]] = curr_board[z_coord[0]][z_coord[1]]
        curr_board[z_coord[0]][z_coord[1]] = tmp
        cb_as_list = transform_to_string_list(curr_board)

        check_hm(Board(cb_as_list),
                 ' '.join(str(num) for row in parent_board for num in row),
                 parent_h, pq, visited)


def move_left(parent_h, parent_board, curr_board, z_coord, pq, visited):

    if z_coord[1] - 1 >= 0:

        tmp = curr_board[z_coord[0]][z_coord[1] - 1]
        curr_board[z_coord[0]][z_coord[1] - 1] = curr_board[z_coord[0]][z_coord[1]]
        curr_board[z_coord[0]][z_coord[1]] = tmp
        cb_as_list = transform_to_string_list(curr_board)

        check_hm(Board(cb_as_list),
                 ' '.join(str(num) for row in parent_board for num in row),
                 parent_h, pq, visited)


def move_right(parent_h, parent_board, curr_board, z_coord, pq, visited):

    if z_coord[1] + 1 < EDGE_LENGTH:

        tmp = curr_board[z_coord[0]][z_coord[1] + 1]
        curr_board[z_coord[0]][z_coord[1] + 1] = curr_board[z_coord[0]][z_coord[1]]
        curr_board[z_coord[0]][z_coord[1]] = tmp
        cb_as_list = transform_to_string_list(curr_board)

        check_hm(Board(cb_as_list),
                 ' '.join(str(num) for row in parent_board for num in row),
                 parent_h, pq, visited)


def check_hm(b, parent, ph, pq, visited):
    """
    Checks to see if the new board (after moving up, down, left, or right) has already been visited.
    If it has not, add to priority queue.
    """

    h = 0
    child = ' '.join(str(e) for e in b.board_as_string_list)

    if child not in visited.keys():
        pq.append((h, b.board_as_string_list))
        visited[child] = [h, h + ph, parent]


def get_path(board, visited):

    if board == 'NULL':
        return
    else:
        get_path(visited[board][2], visited)
        b = Board(board.split(' '))
        b.print_board()
        print('')


def bfs(start_board):
    """
    :param start_board: Start board holds the current board
    :return: Returns true or false (if a solution was found within 15 seconds
    """
    pq = []
    visited = {}

    b = Board(start_board)
    h = 0

    cb_as_list = b.board_as_string_list
    visited[' '.join(str(e) for e in cb_as_list)] = [h, h, 'NULL']

    pq.append((h, cb_as_list))

    curr_max = 0

    curr_time = time.time()

    while len(pq) != 0:

        if (time.time() - curr_time) * 1000 > 30000:
            print('Sorry... We did not find a solution within 30 seconds... Terminating the program.')
            break
        node = pq.pop(0)
        if getsizeof(pq) > curr_max:
            curr_max = getsizeof(pq)

        # node[0] == 0 or (use for next project, put that or cond in if cond
        if node[1] == GOAL_STATE_15_AS_ILIST or node[1] == GOAL_STATE_15_AS_SLIST:
            get_path(GOAL_STATE_15, visited)
            print('*** Solution Found Using BFS!                       ***')
            print('*** The Solution Path has been printed out for you. ***')

            process = psutil.Process(os.getpid())
            memory = process.memory_info().rss
            memory_bfs = memory / 1000000

            globals.memory_bfs = memory_bfs
            print('BFS Size Tree Reached: ', curr_max / 1048576)
            visited.clear()
            return True

        # GET BOARD AS MATRIX
        curr_board = transform_to_matrix(node[1])

        # Find num zeros coordinates
        z_coord = find_zero(curr_board)

        # node[0] holds the parent's heuristic,
        # curr_board holds the parent board [in a matrix]
        # deepcopy(curr_board) is used for the child board
        # z_coord is the position of the 0
        move_up(node[0], curr_board, deepcopy(curr_board), z_coord, pq, visited)
        move_down(node[0], curr_board, deepcopy(curr_board), z_coord, pq, visited)
        move_left(node[0], curr_board, deepcopy(curr_board), z_coord, pq, visited)
        move_right(node[0], curr_board, deepcopy(curr_board), z_coord, pq, visited)

    return False
