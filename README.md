# 15_Puzzle_Multiple_Search_Algorithms

## Introduction:

Example:

Start State (Random Board):
![alt text](https://i.imgur.com/4Vriihw.png)

Goal State (Always same goal):
![alt text](https://i.imgur.com/Zn0DIbr.png)

The following program solves the the N-Puzzle Board Game problem using multiple search techniques.
Once the program has finished executing, the memory and time complexity is printed for comparison.
A-Star with a heuristic produced the best results.
Each search-file contained in this repository is a stand-alone. 
The program was created using Python 3.6

## Files:
*__Note: A Hashmap is used for all the search algorithms to avoid visiting already visited states.__*

__a_star.py:__ A standalone file that uses the A-Star Search Algorithm. The heuristics used for the algorithm are Manhattan Distance and Number of Displaced Tiles.

__bfs.py:__ A standalone file that uses the Breadth First Search Algorithm using a Min-Priority Queue

__board.py:__ A Board Class that essentially holds the contents of the board.

__constants.py:__ A constants file that holds all the constants that is used throughout the program. The program was designed to complete a 15-Puzzle, but with slight modification, it can solve any size puzzle (if given enough memory)

__globals.py:__ A globals file essentially to hold the global variables for memory usage and comparisons.

__iddfs.py:__ Iterative Deepending Depth First Search file that attempts to find the goal state using IDDFS both iteratively and recurisvely.

__main.py:__ The main driver of the program.

__node.py:__ A node class that holds the current board, the parent board (where it came from), the heuristic value of the board, and the total cost to get to that board.

## Limitations:
If a "difficult" board is passed in, none of these search algorithms will work. They will timeout after 15 seconds due to using up all the memory.
The solution to this would be to use A-Star and create subsets of the Puzzle Board and break up the board into smaller components to have "smaller" goal states. This will fix this memory usage issue/limitations. This can easily be achievable once I have more time to work on it :)

__*Output Example:*__

![alt text](https://i.imgur.com/AdNluz3.png)

