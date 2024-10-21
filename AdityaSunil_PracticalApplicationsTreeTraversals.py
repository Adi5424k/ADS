def isValid(maze, visited, x, y):
    rows, cols = len(maze), len(maze[0])
    return 0 <= x < rows and 0 <= y < cols and maze[x][y] == 0 and not visited[x][y]


def preOrderMazeTraversal(maze, x, y, end, visited, path):
    if (x, y) == end:
        path.append((x, y))
        return True

    visited[x][y] = True
    path.append((x, y))
    
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if isValid(maze, visited, nx, ny):
            if preOrderMazeTraversal(maze, nx, ny, end, visited, path):
                return True
    path.pop()
    return False


def solveMaze(maze, start, end):
    rows, cols = len(maze), len(maze[0])
    visited = [[False for _ in range(cols)] for _ in range(rows)]
    path = []
    if preOrderMazeTraversal(maze, start[0], start[1], end, visited, path):
        return path
    else:
        return "No path found"


maze1 = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [0, 1, 1, 0, 0],
    [0, 0, 0, 0, 0]
]

start = (0, 0)
end = (4, 4)

print("Pre-order DFS Solution Path:", solveMaze(maze1, start, end))
