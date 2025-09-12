# Graph representing regions and adjacency
# Each key is a region, values are adjacent regions
graph = {
    'A': ['B', 'C', 'D'],
    'B': ['A', 'C', 'E'],
    'C': ['A', 'B', 'D', 'E'],
    'D': ['A', 'C', 'E'],
    'E': ['B', 'C', 'D']
}

colors = ['Red', 'Green', 'Blue']  # Available colors

def is_safe(region, color, assignment, graph):
    """
    Check if we can assign 'color' to 'region' without conflict
    """
    for neighbor in graph[region]:
        if assignment.get(neighbor) == color:
            return False
    return True

def map_coloring(graph, colors, assignment={}, regions=None):
    """
    Backtracking map coloring algorithm
    """
    if regions is None:
        regions = list(graph.keys())

    # All regions colored → solution found
    if not regions:
        return assignment

    region = regions[0]
    for color in colors:
        if is_safe(region, color, assignment, graph):
            assignment[region] = color
            result = map_coloring(graph, colors, assignment, regions[1:])
            if result:
                return result
            # Backtrack
            del assignment[region]
    
    return None  # No solution found

if __name__ == "__main__":
    solution = map_coloring(graph, colors)
    if solution:
        print("Map coloring solution:")
        for region in sorted(solution):
            print(f"Region {region}: {solution[region]}")
    else:
        print("No solution found with given colors.")
