"""
The following python file works with iterative deepening depth first search algorithm..
"""


import os
import time
import psutil
import globals
from board import *
from copy import deepcopy


def move_board(direction, node, visited):
    """
    :param direction:
    :param node:
    :param visited:
    :return:
    """

    cb_as_list = node[0]
    parent_board = node[1]
    z_coord = node[2]
    curr_board = deepcopy(parent_board)
    passed = False

    if direction == "UP" and z_coord[0] - 1 >= 0:
        passed = True
        tmp = curr_board[z_coord[0] - 1][z_coord[1]]
        curr_board[z_coord[0] - 1][z_coord[1]] = curr_board[z_coord[0]][z_coord[1]]
        curr_board[z_coord[0]][z_coord[1]] = tmp
        cb_as_list = transform_to_string_list(curr_board)

    elif direction == "DOWN" and z_coord[0] + 1 < EDGE_LENGTH:
        passed = True
        tmp = curr_board[z_coord[0] + 1][z_coord[1]]
        curr_board[z_coord[0] + 1][z_coord[1]] = curr_board[z_coord[0]][z_coord[1]]
        curr_board[z_coord[0]][z_coord[1]] = tmp
        cb_as_list = transform_to_string_list(curr_board)

    elif direction == "LEFT" and z_coord[1] - 1 >= 0:
        passed = True
        tmp = curr_board[z_coord[0]][z_coord[1] - 1]
        curr_board[z_coord[0]][z_coord[1] - 1] = curr_board[z_coord[0]][z_coord[1]]
        curr_board[z_coord[0]][z_coord[1]] = tmp
        cb_as_list = transform_to_string_list(curr_board)

    elif direction == "RIGHT" and z_coord[1] + 1 < EDGE_LENGTH:
        passed = True
        tmp = curr_board[z_coord[0]][z_coord[1] + 1]
        curr_board[z_coord[0]][z_coord[1] + 1] = curr_board[z_coord[0]][z_coord[1]]
        curr_board[z_coord[0]][z_coord[1]] = tmp
        cb_as_list = transform_to_string_list(curr_board)

    del curr_board[:]
    del curr_board

    # If it passed through one of the if-elif conditions, check to see if the board has been visited.
    # If it has not passed through one of the if-elif conditions, then return NULL.
    # If it has not been visited, return the board as string (to use in search), else return NULL
    if passed:
        result = check_hm(Board(cb_as_list), ' '.join(str(num) for row in parent_board for num in row), visited)
    else:
        return 'NULL'

    if result:
        return cb_as_list
    else:
        return 'NULL'


def check_hm(b, parent, visited):
    """
    :param b:
    :param parent:
    :param visited:
    :return:
    """

    child = ' '.join(str(e) for e in b.board_as_string_list)
    if child not in visited.keys():
        visited[child] = parent
        return True
    return False


def get_path(board, visited):
    """
    :param board:
    :param visited:
    :return:
    """

    if board == 'NULL':
        return
    else:
        get_path(visited[board], visited)
        b = Board(board.split(' '))
        b.print_board()
        print('')


def iddfs(start_board):
    """
    :param start_board:
    :return:
    """

    visited = {}
    curr_time = time.time()
    depth = 0

    while True:

        if (time.time() - curr_time) * 1000 > 15000:
            print('Sorry... We did not find a solution within 15 seconds using IDDFS... Terminating the program.')
            break

        b = Board(start_board)
        cb_as_list = b.board_as_string_list
        visited[' '.join(str(e) for e in cb_as_list)] = 'NULL'

        if dls(start_board, depth, visited):
            get_path(GOAL_STATE_15, visited)
            print('*** Solution Found using IDDFS!                     ***')
            print('*** The Solution Path has been printed out for you. ***')
            return True

        depth += 1
        visited.clear()

    return False


def dls(current_board, depth, visited):
    """
    :param current_board:
    :param depth:
    :param visited:
    :return:
    """

    b = Board(current_board)

    cb_as_list = b.board_as_string_list

    if cb_as_list == GOAL_STATE_15_AS_ILIST or cb_as_list == GOAL_STATE_15_AS_SLIST:
        return True

    if depth <= 0:
        return False

    # GET BOARD AS MATRIX
    curr_board = transform_to_matrix(cb_as_list)

    # Find num zeros coordinates
    z_coord = find_zero(curr_board)

    up_result = move_board("UP", [cb_as_list, curr_board, z_coord], visited)
    down_result = move_board("DOWN", [cb_as_list, curr_board, z_coord], visited)
    left_result = move_board("LEFT", [cb_as_list, curr_board, z_coord], visited)
    right_result = move_board("RIGHT", [cb_as_list, curr_board, z_coord], visited)

    process = psutil.Process(os.getpid())
    memory = process.memory_info().rss
    memory_iddfs = memory / 1000000
    globals.memory_iddfs = memory_iddfs

    if up_result != "NULL":
        if dls(up_result, depth - 1, visited):
            return True
    if down_result != "NULL":
        if dls(down_result, depth - 1, visited):
            return True
    if left_result != 'NULL':
        if dls(left_result, depth - 1, visited):
            return True
    if right_result != 'NULL':
        if dls(right_result, depth - 1, visited):
            return True

    return False


def nr_iddfs(start_board):
    """
    :param start_board:
    :return:
    """

    curr_time = time.time()
    visited = {}
    overall_depth = 0

    while True:

        if (time.time() - curr_time) * 1000 > 15000:
            print('Sorry... We did not find a solution within 15 seconds using NR_IDDFS... Terminating the program.')
            break

        visited.clear()

        b = Board(start_board)
        cb_as_list = b.board_as_string_list

        visited[' '.join(str(e) for e in cb_as_list)] = 'NULL'
        lifo_pq = [(cb_as_list, 0)]

        while len(lifo_pq) > 0:

            curr_board = lifo_pq.pop()

            if curr_board[0] == GOAL_STATE_15_AS_ILIST or curr_board[0] == GOAL_STATE_15_AS_SLIST:
                get_path(GOAL_STATE_15, visited)
                print('*** Solution Found using NR_IDDFS!                     ***')
                print('*** The Solution Path has been printed out for you.    ***')

                process = psutil.Process(os.getpid())
                memory = process.memory_info().rss
                memory_nr_iddfs = memory / 1000000
                globals.memory_nr_iddfs = memory_nr_iddfs

                return True

            if curr_board[1] < overall_depth:

                # GET BOARD AS MATRIX
                board_as_matrix = transform_to_matrix(curr_board[0])
                # Find num zeros coordinates
                z_coord = find_zero(board_as_matrix)

                up_result = move_board("UP", [curr_board[0], board_as_matrix, z_coord], visited)
                down_result = move_board("DOWN", [curr_board[0], board_as_matrix, z_coord], visited)
                left_result = move_board("LEFT", [curr_board[0], board_as_matrix, z_coord], visited)
                right_result = move_board("RIGHT", [curr_board[0], board_as_matrix, z_coord], visited)

                if right_result != 'NULL':
                    lifo_pq.append((right_result, curr_board[1] + 1))
                if left_result != 'NULL':
                    lifo_pq.append((left_result, curr_board[1] + 1))
                if down_result != "NULL":
                    lifo_pq.append((down_result, curr_board[1] + 1))
                if up_result != "NULL":
                    lifo_pq.append((up_result, curr_board[1] + 1))

        overall_depth = overall_depth + 1

    return False
