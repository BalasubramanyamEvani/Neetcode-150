class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        nodes = {i: [0, 0] for i in range(1, n + 1)}
        for a, b in trust:
            nodes[b][0] += 1
            nodes[a][1] += 1
        for k, v in nodes.items():
            if v[0] == n - 1 and v[1] == 0:
                return k
        return -1
