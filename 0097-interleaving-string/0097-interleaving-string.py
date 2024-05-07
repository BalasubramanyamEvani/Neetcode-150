class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        cache = {}
        N1, N2 = len(s1), len(s2)
        if len(s3) != N1 + N2:
            return False
        def dfs(p1, p2):
            if p1 == N1 and p2 == N2:
                return True
            if (p1, p2) in cache:
                return cache[(p1, p2)]
            ret = False
            if p1 < N1 and s1[p1] == s3[p1 + p2]:
                ret |= dfs(p1 + 1, p2)
            if p2 < N2 and s2[p2] == s3[p1 + p2]:
                ret |= dfs(p1, p2 + 1)
            cache[(p1, p2)] = ret
            return ret
        
        return dfs(0, 0)
