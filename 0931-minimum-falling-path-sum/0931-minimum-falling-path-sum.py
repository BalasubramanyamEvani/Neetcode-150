class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        nr, nc = len(matrix), len(matrix[0])
        dp = [[math.inf] * nc for _ in range(nr)]
        
        for i in range(nc):
            dp[0][i] = matrix[0][i]
        
        for i in range(1, nr):
            for j in range(nc):                    
                dp[i][j] = min(dp[i][j], matrix[i][j] + dp[i - 1][j])
                if j - 1 >= 0:
                    dp[i][j] = min(dp[i][j], matrix[i][j] + dp[i - 1][j - 1])
                if j + 1 < nc:
                    dp[i][j] = min(dp[i][j], matrix[i][j] + dp[i - 1][j + 1])

        ret = math.inf
        for i in range(nc):
            ret = min(ret, dp[-1][i])
        
        return ret
