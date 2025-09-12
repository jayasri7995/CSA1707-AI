import itertools

# Distance matrix (symmetric)
# Example: 4 cities (0,1,2,3)
dist_matrix = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

def tsp_brute_force(dist_matrix):
    n = len(dist_matrix)
    cities = list(range(n))
    min_path = None
    min_cost = float('inf')

    # Generate all possible permutations (excluding starting city 0 for simplicity)
    for perm in itertools.permutations(cities[1:]):
        path = (0,) + perm + (0,)  # start and end at city 0
        cost = sum(dist_matrix[path[i]][path[i+1]] for i in range(n))
        if cost < min_cost:
            min_cost = cost
            min_path = path

    return min_path, min_cost

if __name__ == "__main__":
    path, cost = tsp_brute_force(dist_matrix)
    print("Optimal path:", path)
    print("Minimum cost:", cost)
