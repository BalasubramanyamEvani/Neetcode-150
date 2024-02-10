class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        N = len(triangle)
        # Recursion - TLE
        # def recursion(i, j):
        #     if i < N and j < len(triangle[i]):
        #         tmp = triangle[i][j]
        #         tmp = min(tmp + recursion(i + 1, j), tmp + recursion(i + 1, j + 1))
        #         return tmp
        #     return 0
        # return recursion(0, 0)
        
        # Top Down - Memoization
        memo = {}
        def recursion(i, j):
            if i < N and j < len(triangle[i]):
                if (i, j) in memo:
                    return memo[(i, j)]
                tmp = triangle[i][j]
                tmp = min(tmp + recursion(i + 1, j), tmp + recursion(i + 1, j + 1))
                memo[(i, j)] = tmp
                return memo[(i, j)]
            return 0
        return recursion(0, 0)
