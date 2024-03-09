class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        nr, nc = len(grid), len(grid[0])
        visited = set()
        count = 0
        def valid(r, c):
            return r >= 0 and r < nr and c >= 0 and c < nc
            
        def recursive(r, c):
            if not valid(r, c):
                return 0
            if (r, c) not in visited and grid[r][c] == 1:
                visited.add((r, c))
                nonlocal count
                down = recursive(r + 1, c)
                up = recursive(r - 1, c)
                right = recursive(r, c + 1)
                left = recursive(r, c - 1)
                count += 4 - (up + down + right + left)
                return 1
            return 1 if grid[r][c] == 1 else 0
        
        for r in range(nr):
            for c in range(nc):
                if grid[r][c] == 1:
                    recursive(r, c)
                    break
        return count
