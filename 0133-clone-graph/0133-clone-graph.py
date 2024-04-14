"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, src: Optional['Node']) -> Optional['Node']:
        if not src:
            return None
        # do BFS
        q = deque()
        visited = set()
        q.append(src)
        visited = {}
        # clone src node
        visited[src] = Node(src.val, [])
        # we need to return list of nodes connected the traversed
        # node, so do normal BFS and make connections for only
        # node dequeued from the q and not the children that way
        # there will be no duplications
        while q:
            original = q.popleft()
            for neighbor in original.neighbors:
                if neighbor not in visited:
                    # bfs
                    visited[neighbor] = Node(neighbor.val, [])
                    q.append(neighbor)
                visited[original].neighbors.append(visited[neighbor])
        return visited[src]
