class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        nr, nc = len(grid), len(grid[0])
        dp = [[0] * nc for _ in range(nr)]
        dp[-1][-1] = grid[-1][-1]
        
        for i in range(nc - 2, -1, -1):
            dp[-1][i] = dp[-1][i + 1] + grid[-1][i]
        
        for i in range(nr - 2, -1, -1):
            dp[i][-1] = dp[i + 1][-1] + grid[i][-1]
        
        for i in range(nr - 2, -1, -1):
            for j in range(nc - 2, -1, -1):
                dp[i][j] = grid[i][j] + min(dp[i][j + 1], dp[i + 1][j])
        
        return dp[0][0]
                