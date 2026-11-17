# Missionaries and Cannibals using DFS

visited = set()

def is_valid(m_left, c_left):
    m_right = 3 - m_left
    c_right = 3 - c_left

    if m_left < 0 or c_left < 0 or m_left > 3 or c_left > 3:
        return False
    if m_left > 0 and c_left > m_left:
        return False
    if m_right > 0 and c_right > m_right:
        return False
    return True

def dfs(state, path):
    if state == (0, 0, 0):
        path.append(state)
        return True

    visited.add(state)
    path.append(state)

    m_left, c_left, boat = state
    moves = [(2, 0), (0, 2), (1, 1), (1, 0), (0, 1)]

    for m, c in moves:
        if boat == 1:
            new = (m_left - m, c_left - c, 0)
        else:
            new = (m_left + m, c_left + c, 1)

        if is_valid(new[0], new[1]) and new not in visited:
            if dfs(new, path):
                return True

    path.pop()
    return False

path = []
dfs((3, 3, 1), path)

print("Solution Path:\n")
for state in path:
    print(state)
