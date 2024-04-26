class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        nr, nc = len(grid), len(grid[0])
        dp = [[math.inf] * nc for _ in range(nr)]
        
        for i in range(nc):
            dp[0][i] = grid[0][i]
        
        for i in range(1, nr):
            for j in range(nc):
                for k in range(nc):
                    if j != k:
                        dp[i][j] = min(dp[i][j], grid[i][j] + dp[i - 1][k])
        
        ret = math.inf
        for i in range(nc):
            ret = min(ret, dp[-1][i])
        
        return ret
