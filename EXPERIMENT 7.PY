from collections import deque

def bfs(graph, start):
    """
    Perform Breadth First Search on a graph starting from the start node.

    Args:
        graph (dict): adjacency list representation of graph {node: [neighbors]}
        start: starting node

    Returns:
        list: order of visited nodes
    """
    visited = set()
    queue = deque([start])
    order = []

    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.add(node)
            order.append(node)
            # Add unvisited neighbors to queue
            for neighbor in graph.get(node, []):
                if neighbor not in visited:
                    queue.append(neighbor)
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

    visited_order = bfs(graph, 'A')
    print("BFS Traversal Order:", visited_order)
