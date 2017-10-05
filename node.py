# Not used until later projects =)


class Node:

    current_board = [[]]
    parent_board = [[]]
    heuristic_value = 0
    total_cost = 0

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
