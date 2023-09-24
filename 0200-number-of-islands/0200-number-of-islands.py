class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        nr, nc = len(grid), len(grid[0])
        visited = set()
        def dfs(r, c):
            if r < 0 or r >= nr or c < 0 or c >= nc:
                return
            if grid[r][c] == "1" and (r, c) not in visited:
                visited.add((r, c))
                dfs(r + 1, c)
                dfs(r - 1, c)
                dfs(r, c + 1)
                dfs(r, c - 1)
        
        res = 0
        for r in range(nr):
            for c in range(nc):
                if grid[r][c] == "1" and (r, c) not in visited:
                    res += 1
                    dfs(r, c)
        
        return res
