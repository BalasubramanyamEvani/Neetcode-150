class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # simple recursion - TLE
#         def traverse(m, n):
#             if m == 0 or n == 0:
#                 return 0
#             if m == 1 and n == 1:
#                 return 1
#             return traverse(m - 1, n) + traverse(m, n - 1)
        
#         return traverse(m, n)
        # with DP memoization
        memo = {}
        def traverse(m, n):
                if m == 0 or n == 0:
                    return 0
                if m == 1 and n == 1:
                    return 1
                if (m, n) in memo:
                    return memo[(m, n)]
                memo[(m, n)] = traverse(m - 1, n) + traverse(m, n - 1)
                return memo[(m, n)]
        return traverse(m, n)
