class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        visited = set()
        graph = {}
        for edge in edges:
            n1, n2 = edge
            if n1 not in graph:
                graph[n1] = set()
            if n2 not in graph:
                graph[n2] = set()
            graph[n1].add(n2)
            graph[n2].add(n1)
            
        def traverse(n):
            if n not in visited:
                visited.add(n)
                if n == destination:
                    return True
                children = graph[n]
                for child in children:
                    if child not in visited:
                        found = traverse(child)
                        if found:
                            return True
            return False
        return traverse(source)
