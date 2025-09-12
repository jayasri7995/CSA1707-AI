import heapq
from collections import deque

# ----- Helpers -----
GOAL = (1,2,3,4,5,6,7,8,0)  # 0 represents the blank

# Manhattan distance heuristic
def manhattan(state):
    dist = 0
    for idx, val in enumerate(state):
        if val == 0:
            continue
        goal_idx = val - 1
        cur_r, cur_c = divmod(idx, 3)
        goal_r, goal_c = divmod(goal_idx, 3)
        dist += abs(cur_r - goal_r) + abs(cur_c - goal_c)
    return dist

# Generate neighbor states by sliding the blank (0)
def neighbors(state):
    idx0 = state.index(0)
    r, c = divmod(idx0, 3)
    nbrs = []
    moves = []
    if r > 0: moves.append((-1, 0, 'Up'))
    if r < 2: moves.append((1, 0, 'Down'))
    if c > 0: moves.append((0, -1, 'Left'))
    if c < 2: moves.append((0, 1, 'Right'))
    for dr, dc, action in moves:
        nr, nc = r + dr, c + dc
        nidx = nr * 3 + nc
        new_list = list(state)
        new_list[idx0], new_list[nidx] = new_list[nidx], new_list[idx0]
        nbrs.append((tuple(new_list), action))
    return nbrs

# Check solvability: count inversions (blank ignored)
def is_solvable(state):
    arr = [x for x in state if x != 0]
    inv = 0
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] > arr[j]:
                inv += 1
    return inv % 2 == 0

# ----- A* Search -----
def a_star(start):
    if start == GOAL:
        return [], 0, 0  # no moves needed

    if not is_solvable(start):
        return None, None, None

    open_heap = []
    g_score = {start: 0}
    f_score = manhattan(start)
    heapq.heappush(open_heap, (f_score, 0, start))  # (f, tie-breaker, state)
    came_from = {}
    move_from = {}
    closed = set()
    expansions = 0

    tie = 0
    while open_heap:
        _, _, current = heapq.heappop(open_heap)

        if current in closed:
            continue
        closed.add(current)

        expansions += 1

        if current == GOAL:
            # reconstruct path
            path_actions = deque()
            node = current
            while node in came_from:
                path_actions.appendleft(move_from[node])
                node = came_from[node]
            return list(path_actions), g_score[current], expansions

        for nbr, action in neighbors(current):
            tentative_g = g_score[current] + 1
            if nbr in closed and tentative_g >= g_score.get(nbr, float('inf')):
                continue
            if tentative_g < g_score.get(nbr, float('inf')):
                came_from[nbr] = current
                move_from[nbr] = action
                g_score[nbr] = tentative_g
                f = tentative_g + manhattan(nbr)
                tie += 1
                heapq.heappush(open_heap, (f, tie, nbr))

    return None, None, expansions

# ----- Pretty print state -----
def print_state(state):
    for i in range(0, 9, 3):
        print(' '.join(str(x) if x != 0 else '.' for x in state[i:i+3]))
    print()

# ----- Example usage -----
if __name__ == "__main__":
    # Example start states (you can change to test other puzzles)
    # solvable example (takes some steps)
    start = (1, 2, 3,
             4, 0, 6,
             7, 5, 8)

    # another harder example:
    # start = (7,2,4,5,0,6,8,3,1)

    print("Start state:")
    print_state(start)
    if not is_solvable(start):
        print("This puzzle is NOT solvable.")
    else:
        actions, moves, expanded = a_star(start)
        if actions is None:
            print("No solution found.")
        else:
            print(f"Solution found in {moves} moves. Nodes expanded: {expanded}")
            print("Moves:", actions)
            # show states step by step
            state = start
            print("\nStep-by-step:")
            print_state(state)
            for i, act in enumerate(actions, 1):
                # apply action to get next state
                for nbr, action in neighbors(state):
                    if action == act:
                        state = nbr
                        break
                print(f"Step {i}: {act}")
                print_state(state)
