import heapq

# Distance matrix (symmetric)
dist_matrix = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

def heuristic(current_city, unvisited, dist_matrix):
    """
    Admissible heuristic for TSP: sum of minimum distances from each unvisited city
    """
    h = 0
    for city in unvisited:
        min_dist = min(dist_matrix[city][k] for k in range(len(dist_matrix)) if k != city)
        h += min_dist
    return h

def tsp_a_star(dist_matrix):
    n = len(dist_matrix)
    start = 0
    unvisited = set(range(1, n))
    
    # Priority queue: (f = g + h, g, path, current_city, unvisited)
    heap = []
    initial_h = heuristic(start, unvisited, dist_matrix)
    heapq.heappush(heap, (initial_h, 0, [start], start, unvisited))
    
    while heap:
        f, g, path, current_city, unvisited = heapq.heappop(heap)
        
        if not unvisited:
            # return to start city
            path.append(start)
            g += dist_matrix[current_city][start]
            return path, g
        
        for next_city in unvisited:
            new_g = g + dist_matrix[current_city][next_city]
            new_unvisited = unvisited - {next_city}
            new_path = path + [next_city]
            h = heuristic(next_city, new_unvisited, dist_matrix)
            heapq.heappush(heap, (new_g + h, new_g, new_path, next_city, new_unvisited))
    
    return None, None

if __name__ == "__main__":
    path, cost = tsp_a_star(dist_matrix)
    print("Optimal path (A*):", path)
    print("Minimum cost:", cost)
