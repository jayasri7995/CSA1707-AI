def dfs(graph, start, visited=None, order=None):
    """
    Perform Depth First Search on a graph starting from the start node.

    Args:
        graph (dict): adjacency list representation of graph {node: [neighbors]}
        start: starting node

    Returns:
        list: order of visited nodes
    """
    if visited is None:
        visited = set()
    if order is None:
        order = []

    visited.add(start)
    order.append(start)

    for neighbor in graph.get(start, []):
        if neighbor not in visited:
            dfs(graph, neighbor, visited, order)
    
    return order

# Example usage
if __name__ == "__main__":
    # Graph represented as adjacency list
    graph = {
        'A': ['B', 'C'],
        'B': ['D', 'E'],
        'C': ['F'],
        'D': [],
        'E': ['F'],
        'F': []
    }

    visited_order = dfs(graph, 'A')
    print("DFS Traversal Order:", visited_order)
