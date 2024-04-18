class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        nr, nc = len(grid), len(grid[0])
        visited = set()
        # 1 represents there is a blockage
        # 0 represents there is no blockage
        def dfs(r, c):
            if r < 0 or r >= nr or c < 0 or c >= nc:
                return 0
            if (r, c) not in visited and grid[r][c] == 1:
                visited.add((r, c))
                nonlocal ret
                bottom = dfs(r + 1, c)
                top = dfs(r - 1, c)
                right = dfs(r, c + 1)
                left = dfs(r, c - 1)
                ret += 4 - bottom - top - right - left
                return 1
            if grid[r][c] == 0:
                return 0
            return 1
        
        ret = 0
        for r in range(nr):
            for c in range(nc):
                if grid[r][c] == 1:
                    dfs(r, c)
                    break
        return ret
