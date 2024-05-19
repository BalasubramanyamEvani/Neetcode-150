class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        graph = defaultdict(set)
        for src, room in enumerate(rooms):
            for dst in room: 
                graph[src].add(dst)
        
        visited = set()
        def dfs(node):
            if node not in visited:
                visited.add(node)
                for child in graph[node]:
                    if child not in visited:
                        dfs(child)
        dfs(0)
        return len(visited) == len(graph)
