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
        memo = {}
        def recursion(r, c):
            if r == 1 and c == 1 and obstacleGrid[nr - r][nc - c] == 0:
                return 1
            if r == 0 or c == 0:
                return 0
            if obstacleGrid[nr - r][nc - c] == 1:
                return 0
            if (r, c) in memo:
                return memo[(r, c)]
            memo[(r, c)] = recursion(r - 1, c) + recursion(r, c - 1)
            return memo[(r, c)]
        return recursion(nr, nc)
