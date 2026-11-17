from collections import deque

# Grid: D = Dirty, C = Clean, X = Obstacle
grid = [
    ['D', 'D', 'X', 'D'],
    ['C', 'D', 'C', 'X'],
    ['D', 'X', 'D', 'D'],
    ['C', 'C', 'D', 'C']
]

ROWS = len(grid)
COLS = len(grid[0])
start = (0, 0)

# Internal state model
visited = [[False] * COLS for _ in range(ROWS)]
obstacles = set()
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def is_valid(x, y):
    return 0 <= x < ROWS and 0 <= y < COLS

def vacuum_agent(start):
    queue = deque([start])

    while queue:
        x, y = queue.popleft()

        if visited[x][y]:
            continue

        visited[x][y] = True

        if grid[x][y] == 'X':
            obstacles.add((x, y))
            continue

        print(f"Moved to ({x}, {y})")

        if grid[x][y] == 'D':
            print(f"Cleaning cell ({x}, {y})")
            grid[x][y] = 'C'

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if is_valid(nx, ny):
                if grid[nx][ny] == 'X':
                    obstacles.add((nx, ny))
                elif not visited[nx][ny]:
                    queue.append((nx, ny))

vacuum_agent(start)

print("\nFinal Grid:")
for row in grid:
    print(row)

print("\nObstacles Found:", obstacles)
