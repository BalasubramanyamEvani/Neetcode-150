class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        # Recursion - TLE
        nr, nc = len(obstacleGrid), len(obstacleGrid[0])
        # def recursion(r, c):
        #     if r == 1 and c == 1 and obstacleGrid[nr - r][nc - c] == 0:
        #         return 1
        #     if r == 0 or c == 0:
        #         return 0
        #     if obstacleGrid[nr - r][nc - c] == 1:
        #         return 0
        #     return recursion(r - 1, c) + recursion(r, c - 1)
        # return recursion(nr, nc)
        
        # Top Down - Memoization
        # memo = {}
        # def recursion(r, c):
        #     if r == 1 and c == 1 and obstacleGrid[nr - r][nc - c] == 0:
        #         return 1
        #     if r == 0 or c == 0:
        #         return 0
        #     if obstacleGrid[nr - r][nc - c] == 1:
        #         return 0
        #     if (r, c) in memo:
        #         return memo[(r, c)]
        #     memo[(r, c)] = recursion(r - 1, c) + recursion(r, c - 1)
        #     return memo[(r, c)]
        # return recursion(nr, nc)
        
        # Bottom Up - Tabular
        dp = [[0] * nc for _ in range(nr)]
        dp[0][0] = 1 - obstacleGrid[-1][-1]
        for i in range(1, nc):
            if not obstacleGrid[-1][nc - i - 1]:
                dp[0][i] = dp[0][i - 1]
        for i in range(1, nr):
            if not obstacleGrid[nr - i - 1][-1]:
                dp[i][0] = dp[i - 1][0]
        for i in range(1, nr):
            for j in range(1, nc):
                if obstacleGrid[nr - i - 1][nc - j - 1] == 0:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[-1][-1]
