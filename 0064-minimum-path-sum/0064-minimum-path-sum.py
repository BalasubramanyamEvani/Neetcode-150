class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        # Recursion - TLE
        # nr, nc = len(grid), len(grid[0])
        # def traverse(r, c):
        #     if r == 0 or c == 0:
        #         return math.inf
        #     if r == 1 and c == 1:
        #         return grid[nr - r][nc - c]
        #     right = grid[nr - r][nc - c] + traverse(r, c - 1)
        #     down = grid[nr - r][nc - c] + traverse(r - 1, c)
        #     return min(right, down)
        # return traverse(nr, nc)
        
        # Top Down DP - Memoization - Passes
        # nr, nc = len(grid), len(grid[0])
        # memo = {}
        # def traverse(r, c):
        #     if r == 0 or c == 0:
        #         return math.inf
        #     if r == 1 and c == 1:
        #         return grid[nr - r][nc - c]
        #     if (r, c) in memo:
        #         return memo[(r, c)]
        #     right = grid[nr - r][nc - c] + traverse(r, c - 1)
        #     down = grid[nr - r][nc - c] + traverse(r - 1, c)
        #     memo[(r, c)] = min(right, down)
        #     return memo[(r, c)]
        # return traverse(nr, nc)
        
        # Bottom Up DP - Tabular
        nr, nc = len(grid), len(grid[0])
        dp = [[0] * nc for _ in range(nr)]
        dp[0][0] = grid[-1][-1]
        for i in range(1, nc):
            dp[0][i] = grid[-1][nc - i - 1] + dp[0][i - 1]
        for i in range(1, nr):
            dp[i][0] = grid[nr - i - 1][-1] + dp[i - 1][0]
        for i in range(1, nr):
            for j in range(1, nc):
                dp[i][j] =  min(grid[nr - i - 1][nc - j - 1] + dp[i - 1][j], grid[nr - i - 1][nc - j - 1] + dp[i][j - 1])
        print(dp)
        return dp[-1][-1]
