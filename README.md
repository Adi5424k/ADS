# Maze Solver Using Pre-order Depth First Search (DFS)

This project demonstrates the use of **pre-order traversal** (Depth First Search - DFS) to solve a maze. The goal is to find a path from the start position to the end position in a given maze, where:
- `0` represents a walkable path.
- `1` represents a wall or blocked path.

### Assignment Information

This project is part of an assignment demonstrating the application of pre-order Depth First Search (DFS) traversal to solve a maze. The code was developed as part of a coursework exercise for learning tree traversal algorithms.

- **Name**: Aditya Sunil
- **USN**: 1RVU23BSC006

## Problem Description

Given a maze as a 2D grid, the program will find a valid path from a specified start point to the end point using pre-order DFS traversal. If a path is found, the solution path will be displayed; otherwise, the program will indicate that no path exists.

### Example Maze:

```plaintext
maze = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [0, 1, 1, 0, 0],
    [0, 0, 0, 0, 0]
]
```

- **Start Point**: (0, 0)
- **End Point**: (4, 4)

## How to Run

1. Clone or download the repository.
2. Open the project folder.
3. Run the `AdityaSunil_PracticalApplicationsTreeTraversals.py` script using Python.

### Command to run:

```bash
python AdityaSunil_PracticalApplicationsTreeTraversals.py
```

The program will print the solution path if one exists or notify that no path was found.

### Example Output:

```plaintext
Pre-order DFS Solution Path: [(0, 0), (1, 0), (2, 0), (2, 1), (2, 2), (3, 3), (4, 3), (4, 4)]
```

## Functions

- **`isValid(maze, visited, x, y)`**: Checks if the current position is within bounds, on a valid path (0), and not visited.
- **`preOrderMazeTraversal(maze, x, y, end, visited, path)`**: Performs the pre-order DFS traversal to find a path.
- **`solveMaze(maze, start, end)`**: Main function to initiate the DFS traversal and return the solution path if found.

