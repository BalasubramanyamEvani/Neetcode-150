class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {}
        # construct DAG graph prereq -> course
        for a, b in prerequisites:
            if a not in graph:
                graph[a] = []
            if b not in graph:
                graph[b] = []
            graph[b].append(a)
        
        def dfs_cycle(vertex, trace):
            if vertex not in visited:
                trace.add(vertex)
                visited.add(vertex)
                for course in graph[vertex]:
                    if dfs_cycle(course, trace):
                        return True
                trace.remove(vertex)
            if vertex in trace:
                return True
            return False
        
        visited = set()
        for vertex in graph.keys():
            trace = set()
            if dfs_cycle(vertex, trace):
                return False
        return True
