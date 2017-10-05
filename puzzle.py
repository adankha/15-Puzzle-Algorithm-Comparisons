import copy as cp
import time
import os
import psutil

try:
    import psutil  # for computing memory usage
except ImportError:  # try to install requests module if not present
    print ("Trying to Install required module: psutil\n")
    os.system('sudo python -m pip install psutil')
import psutil


# BFS implementation
def breadth_first_search(iInitialState, iEndState):
    node = str(iInitialState)
    final = str(iEndState)

    if node == final:
        return node

    frontier = [[node]]
    explored = []
    actionPath = []
    actionFrontier = []

    while frontier:
        solutionPath = frontier[0]  # Set the solution path to first element in frontier
        frontier.pop(0)  # pop it from the frontier
        lastNode = str(solutionPath[-1])

        if len(actionFrontier):
            actionPath = actionFrontier[0]
            actionFrontier.pop(0)

        if lastNode in explored:  # if last node is already present in the explored then continue
            continue  # Repeated states check

        for currentState,actionMove in possibleStates(lastNode).items():
            if currentState in explored:  # if currentState is already in explored fringe, do not add it again
                continue  # repeated state check
            frontier.append(solutionPath + [currentState])
            actionFrontier.append(actionPath + [actionMove])

        explored.append(lastNode)

        process = psutil.Process(os.getpid())
        memory = process.memory_info().rss / 1000000

        if memory > 200:
            print ("Memory limit exceeded")
            print ("Depth explored till now:", len(frontier))
            return None

        if len(frontier) == 0:  # empty frontier means no solution, sanity check
            print ("Depth explored: ", len(solutionPath))
            return None

        if lastNode == final:
            print ("Depth of Solution: ", len(solutionPath))
            return actionPath


# find possbile states
def possibleStates(iCurrentState):
    oPossibleStates = {};
    state = eval(iCurrentState)
    zeroIndex = [[ix, iy] for ix, row in enumerate(state) for iy, i in enumerate(row) if i == 0]
    iX = zeroIndex[0][0]
    iY = zeroIndex[0][1]

    minIndex = 0
    maxIndex = 3

    if iX > minIndex:  # move pieces up and append to possible states
        state[iX][iY], state[iX - 1][iY] = state[iX - 1][iY], state[iX][iY]
        tmp = cp.deepcopy(state)
        sequenceActionPair = {repr(tmp):"UP"}
        oPossibleStates.update(sequenceActionPair)
        # revert back to original state
        state[iX][iY], state[iX - 1][iY] = state[iX - 1][iY], state[iX][iY]

    if iX < maxIndex:  # move pieces down and append to possible states
        state[iX][iY], state[iX + 1][iY] = state[iX + 1][iY], state[iX][iY]
        tmp = cp.deepcopy(state)
        sequenceActionPair = {repr(tmp): "DOWN"}
        oPossibleStates.update(sequenceActionPair)
        # revert back to original state
        state[iX][iY], state[iX + 1][iY] = state[iX + 1][iY], state[iX][iY]

    if iY > minIndex:  # move pieces left and append to possible states
        state[iX][iY], state[iX][iY - 1] = state[iX][iY - 1], state[iX][iY]
        tmp = cp.deepcopy(state)
        sequenceActionPair = {repr(tmp): "LEFT"} #the other tile will be moved
        oPossibleStates.update(sequenceActionPair)
        # revert back to original state
        state[iX][iY], state[iX][iY - 1] = state[iX][iY - 1], state[iX][iY]

    if iY < maxIndex:  # move pieces right and append to possible states
        state[iX][iY], state[iX][iY + 1] = state[iX][iY + 1], state[iX][iY]
        tmp = cp.deepcopy(state)
        sequenceActionPair = {repr(tmp): "RIGHT"} #the other tile will be moved
        oPossibleStates.update(sequenceActionPair)
        # revert back to original state
        state[iX][iY], state[iX][iY + 1] = state[iX][iY + 1], state[iX][iY]

    return oPossibleStates


# main function
if __name__ == '__main__':

    startTime = time.time()

    initialState = [[1, 2, 3, 4],
                [5, 6, 7, 8],
                [13, 9, 12, 15],
                [0, 11, 10, 14]]

    endState = [[1, 2, 3, 4],
                [5, 6, 7, 8],
                [9, 10, 11, 12],
                [13, 14, 15, 0]]

    path = breadth_first_search(initialState, endState)
    time = time.time() - startTime
    if path == None:
        print ("Solution does not exist")
    else:
        for i in range(0, len(path) - 1):
            print (path[i])
        print (path[len(path) - 1])
    print ("Number of seconds to solve: ", time)
    process = psutil.Process(os.getpid())
    memory = process.memory_info().rss
    print ("Memory used:(in MB)", memory / 1000000)