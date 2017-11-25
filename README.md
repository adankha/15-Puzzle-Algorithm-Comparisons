# 15_Puzzle_Multiple_Search_Algorithms

## Introduction:
The following program solves the the N-Puzzle Board Game problem using multiple search techniques.
Once the program has finished executing, the memory and time complexity is printed for comparison.
A-Star with a heuristic produced the best results.
Each search-file contained in this repository is a stand-alone. 
The program was created using Python 3.6

## Files:
** Note: A Hashmap is used for all the search algorithms to avoid visiting already visited states. **

###### a_star.py:
A standalone file that uses the A-Star Search Algorithm. The heuristics used for the algorithm are Manhattan Distance and Number of Displaced Tiles.

###### bfs.py:
A standalone file that uses the Breadth First Search Algorithm using a Min-Priority Queue

###### board.py:
A Board Class that essentially holds the contents of the board.

###### constants.py:
A constants file that holds all the constants that is used throughout the program. The program was designed to complete a 15-Puzzle, but with slight modification, it can solve any size puzzle (if given enough memory)

###### globals.py:
A globals file essentially to hold the global variables for memory usage and comparisons.

###### iddfs.py:
Iterative Deepending Depth First Search file that attempts to find the goal state using IDDFS both iteratively and recurisvely.

###### main.py:
The main driver of the program.

###### node.py:
A node class that holds the current board, the parent board (where it came from), the heuristic value of the board, and the total cost to get to that board.

## Limitations:
If a "difficult" board is passed in, none of these search algorithms will work. They will timeout after 15 seconds.
The solution to this would be to use A-Star and create subsets of the Puzzle Board and break up the board into smaller components and have "smaller" goal states to fix this issue. This can easily be achievable once I have more time to work on it :)

