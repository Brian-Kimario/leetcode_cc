from collections import deque, defaultdict

class Solution(object):
    def validPath(self, n, edges, source, destination):
        
        # Base case: if source and destination are the same, a path always exists
        if source == destination:
            return True
            
        # Build the adjacency list for the bi-directional graph
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
            
        # Initialize BFS queue with the source node
        queue = deque([source])
        
        # Track visited nodes to avoid infinite loops
        visited = {source}
        
        # Standard BFS traversal
        while queue:
            node = queue.popleft()
            
            # Check all connected neighbors
            for neighbor in graph[node]:
                # If we reach the target destination, return True immediately
                if neighbor == destination:
                    return True
                
                # If the neighbor hasn't been visited yet, add it to our queue
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
                    
        # If the queue runs empty and we haven't found the destination, no path exists
        return False
