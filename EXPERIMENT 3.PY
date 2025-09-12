from collections import deque

# Function to print states clearly
def print_state(state):
    print(f"Jug1: {state[0]} | Jug2: {state[1]}")

# BFS to solve water jug problem
def water_jug_bfs(cap1, cap2, target):
    visited = set()
    queue = deque()
    
    # Start from both jugs empty
    start = (0, 0)
    queue.append((start, []))
    visited.add(start)
    
    while queue:
        (jug1, jug2), path = queue.popleft()

        # If we reached target
        if jug1 == target or jug2 == target:
            print("Solution found in", len(path), "steps:\n")
            for step, state in enumerate(path + [(jug1, jug2)], 1):
                print(f"Step {step} -> Jug1: {state[0]}, Jug2: {state[1]}")
            return True

        # Generate all possible next moves
        moves = []
        # 1. Fill jug1
        moves.append((cap1, jug2))
        # 2. Fill jug2
        moves.append((jug1, cap2))
        # 3. Empty jug1
        moves.append((0, jug2))
        # 4. Empty jug2
        moves.append((jug1, 0))
        # 5. Pour jug1 -> jug2
        pour = min(jug1, cap2 - jug2)
        moves.append((jug1 - pour, jug2 + pour))
        # 6. Pour jug2 -> jug1
        pour = min(jug2, cap1 - jug1)
        moves.append((jug1 + pour, jug2 - pour))

        for m in moves:
            if m not in visited:
                visited.add(m)
                queue.append((m, path + [(jug1, jug2)]))
    
    print("No solution found.")
    return False


# Example usage
if __name__ == "__main__":
    cap1 = 4   # Jug 1 capacity
    cap2 = 3   # Jug 2 capacity
    target = 2 # Target amount to measure
    
    water_jug_bfs(cap1, cap2, target)
