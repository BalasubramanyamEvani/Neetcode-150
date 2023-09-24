class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        nr, nc = len(grid), len(grid[0])
        res = 0
        visited = set()
        
        def dfs(r, c, count):
            if r < 0 or r >= nr or c < 0 or c >= nc:
                return count
            if grid[r][c] == 1 and (r, c) not in visited:
                visited.add((r, c))
                count += 1
                count = dfs(r + 1, c, count)
                count = dfs(r - 1, c, count)
                count = dfs(r, c + 1, count)
                count = dfs(r, c - 1, count)
            
            return count
        
        for r in range(nr):
            for c in range(nc):
                if grid[r][c] == 1 and (r, c) not in visited:
                    res = max(res, dfs(r, c, 0))
        
        return res
