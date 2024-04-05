class Solution:
    def countServers(self, n: int, logs: List[List[int]], x: int, queries: List[int]) -> List[int]:
        # sort logs in ascending order based on time
        logs = sorted(logs, key=lambda x: (x[1]))
        # sort qeuries in ascending order
        # makes it easier to query stuff now since there are overlaps
        queries = [[query, index] for index, query in enumerate(queries)]
        queries = sorted(queries, key=lambda x: (x[0]))
        # sliding window
        l, r = 0, 0
        servers = n
        N = len(logs)
        mem = {}
        ret = [0 for _ in range(len(queries))]
        # iterate over queries
        # fixing left and right pointers
        for query, index in queries:
            start, end = query - x, query
            # right pointer adds list of servers
            # based on end limit
            while r < N and logs[r][1] <= end:
                server_id = logs[r][0]
                if server_id not in mem:
                    mem[server_id] = 0
                    servers -= 1
                mem[server_id] += 1
                r += 1
            # left pointer removes list of servers
            # based on start limit
            while l <= r and l < N and logs[l][1] < start:
                server_id = logs[l][0]
                mem[server_id] -= 1
                if mem[server_id] == 0:
                    del mem[server_id]
                    servers += 1
                l += 1
            ret[index] = servers
        return ret
