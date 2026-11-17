import heapq

goal = (1, 2, 3,
        4, 5, 6,
        7, 8, 0)

def heuristic(state):
    distance = 0
    for i in range(9):
        if state[i] != 0:
            goal_index = goal.index(state[i])
            current_x = i // 3
            current_y = i % 3
            goal_x = goal_index // 3
            goal_y = goal_index % 3
            distance += abs(current_x - goal_x) + abs(current_y - goal_y)
    return distance

def generate_states(state):
    states = []
    index = state.index(0)
    x = index // 3
    y = index % 3

    moves = [
        (-1, 0),
        (1, 0),
        (0, -1),
        (0, 1)
    ]

    for dx, dy in moves:
        new_x = x + dx
        new_y = y + dy

        if 0 <= new_x < 3 and 0 <= new_y < 3:
            new_index = new_x * 3 + new_y
            new_state = list(state)
            new_state[index], new_state[new_index] = new_state[new_index], new_state[index]
            states.append(tuple(new_state))

    return states

def a_star(start):
    priority_queue = []
    heapq.heappush(priority_queue, (0, start))
    visited = set()
    parent = {}
    cost = {start: 0}

    while priority_queue:
        current = heapq.heappop(priority_queue)[1]

        if current == goal:
            path = []
            while current in parent:
                path.append(current)
                current = parent[current]
            path.append(start)
            return path[::-1]

        visited.add(current)

        for child in generate_states(current):
            if child not in visited:
                new_cost = cost[current] + 1
                if child not in cost or new_cost < cost[child]:
                    cost[child] = new_cost
                    priority = new_cost + heuristic(child)
                    heapq.heappush(priority_queue, (priority, child))
                    parent[child] = current

initial_state = (
    1, 2, 3,
    4, 0, 6,
    7, 5, 8
)

solution = a_star(initial_state)

print("Solution Path:")
for state in solution:
    print()
    for i in range(0, 9, 3):
        print(state[i:i+3])
