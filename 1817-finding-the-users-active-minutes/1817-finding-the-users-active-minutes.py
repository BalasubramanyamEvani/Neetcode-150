class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        mem = {}
        for log in logs:
            if log[0] not in mem:
                mem[log[0]] = set()
            if log[0] in mem and log[1] not in mem[log[0]]:
                mem[log[0]].add(log[1])

        res = [0 for _ in range(k)]
        for v in mem.values():
            res[len(v) - 1] += 1
        return res
