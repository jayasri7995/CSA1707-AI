from collections import deque

# State is represented as (M_left, C_left, Boat_side)
# Boat_side = 0 means left bank, 1 means right bank
# M_left, C_left = number of missionaries and cannibals on left side

def is_valid(state):
    M_left, C_left, _ = state
    M_right = 3 - M_left
    C_right = 3 - C_left

    # Missionaries cannot be outnumbered by cannibals on either side
    if (M_left > 0 and C_left > M_left):
        return False
    if (M_right > 0 and C_right > M_right):
        return False

    # All values must be within range
    if not (0 <= M_left <= 3 and 0 <= C_left <= 3):
        return False

    return True

def get_successors(state):
    M_left, C_left, boat = state
    successors = []
    moves = [(1,0),(2,0),(0,1),(0,2),(1,1)]  # possible moves (M,C)

    for m,c in moves:
        if boat == 0:  # boat on left side
            new_state = (M_left - m, C_left - c, 1)
        else:          # boat on right side
            new_state = (M_left + m, C_left + c, 0)

        if is_valid(new_state):
            successors.append(new_state)

    return successors

def bfs(start, goal):
    queue = deque()
    queue.append((start, [start]))
    visited = set()
    visited.add(start)

    while queue:
        state, path = queue.popleft()

        if state == goal:
            return path

        for succ in get_successors(state):
            if succ not in visited:
                visited.add(succ)
                queue.append((succ, path + [succ]))

    return None

if __name__ == "__main__":
    start = (3,3,0)   # 3 missionaries, 3 cannibals, boat on left
    goal  = (0,0,1)   # all crossed to right side

    solution = bfs(start, goal)

    if solution:
        print("Solution found in", len(solution)-1, "moves:\n")
        for step, state in enumerate(solution):
            print(f"Step {step}: Missionaries left={state[0]}, Cannibals left={state[1]}, Boat={'Left' if state[2]==0 else 'Right'}")
    else:
        print("No solution found.")
