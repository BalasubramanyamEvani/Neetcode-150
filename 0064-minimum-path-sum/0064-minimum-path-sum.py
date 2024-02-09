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
        
        # Top Down DP - Memoization
        nr, nc = len(grid), len(grid[0])
        memo = {}
        def traverse(r, c):
            if r == 0 or c == 0:
                return math.inf
            if r == 1 and c == 1:
                return grid[nr - r][nc - c]
            if (r, c) in memo:
                return memo[(r, c)]
            right = grid[nr - r][nc - c] + traverse(r, c - 1)
            down = grid[nr - r][nc - c] + traverse(r - 1, c)
            memo[(r, c)] = min(right, down)
            return memo[(r, c)]
        return traverse(nr, nc)
