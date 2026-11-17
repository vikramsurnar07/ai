from collections import deque

def bfs(grid, start, goal):
    rows = len(grid)
    cols = len(grid[0])

    queue = deque([start])
    visited = set()
    visited.add(start)

    parent = {}
    parent[start] = None

    directions = [
        (0, 1),   # Right
        (1, 0),   # Down
        (0, -1),  # Left
        (-1, 0)   # Up
    ]

    while queue:
        current = queue.popleft()
        if current == goal:
            break

        row, col = current
        for dr, dc in directions:
            new_row = row + dr
            new_col = col + dc
            new_position = (new_row, new_col)

            if (0 <= new_row < rows and
                0 <= new_col < cols and
                grid[new_row][new_col] != '#' and
                new_position not in visited):
                visited.add(new_position)
                parent[new_position] = current
                queue.append(new_position)

    if goal not in visited:
        return None

    path = []
    current = goal
    while current is not None:
        path.append(current)
        current = parent[current]
    path.reverse()
    return path

grid = [
    ['S', '.', '.', '#', '.'],
    ['.', '#', '.', '#', '.'],
    ['.', '#', '.', '.', '.'],
    ['.', '.', '#', '#', '.'],
    ['#', '.', '.', '.', 'G']
]

start = (0, 0)
goal = (4, 4)

path = bfs(grid, start, goal)

if path:
    print("Shortest Path Found!")
    print("Number of Steps:", len(path) - 1)
    print()

    result = [row[:] for row in grid]
    for row, col in path:
        if result[row][col] not in ['S', 'G']:
            result[row][col] = '*'

    print("Robot Path:")
    for row in result:
        print("  ".join(row))

    print("\nPath Coordinates:")
    for position in path:
        print(position)
else:
    print("No path exists.")
