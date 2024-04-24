class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        leaves = []
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        for node in graph.keys():
            if len(graph[node]) == 1:
                leaves.append(node)
        # pruning from leaves because these nodes
        # are the peripherals of the tree
        q = deque(leaves)
        remain = len(graph)
        while remain > 2:
            remain -= len(q)
            # all leaves currently in queue
            batchlen = len(q)
            # prune it and add immediate connections (there'll be
            # only one) to the queue
            for _ in range(batchlen):
                leaf = q.popleft()
                only_connection = graph[leaf][0]
                graph[only_connection].remove(leaf)
                if len(graph[only_connection]) == 1:
                    q.append(only_connection)

        return list(q) if q else [0]
