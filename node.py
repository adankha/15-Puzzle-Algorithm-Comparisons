"""
The following node class holds certain information of the board state(s) for each algorithm..
"""


class Node:

    __slots__ = ['current_board', 'parent_board', 'heuristic_value', 'total_cost']

    def __init__(self, cb, pb, hv, tc):
        """
        :param cb: current board
        :param pb: parent board
        :param hv: heuristic value
        :param tc: total cost
        """
        self.current_board = cb
        self.parent_board = pb
        self.heuristic_value = hv
        self.total_cost = tc
