class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = {i: [] for i in range(numCourses)}
        for a, b in prerequisites:
            graph[b].append(a)
        
        visited = set()
        ret = []
        
        def dfs_cycle(vertex, trace):
            if vertex not in visited:
                visited.add(vertex)
                trace.add(vertex)
                for course in graph[vertex]:
                    if dfs_cycle(course, trace):
                        return True
                ret.append(vertex)
                trace.remove(vertex)
            if vertex in trace:
                return True
            return False
        
        for vertex in graph.keys():
            trace = set()
            if dfs_cycle(vertex, trace):
                return []
        return ret[::-1]
