class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        n = len(grid)
        # Store row values
        rows = {i: {} for i in range(n)}
        for i in range(n):
            for j in range(n):
                rows[i][j] = grid[i][j]
        
        # Store column values
        cols = {i: {} for i in range(n)}
        for i in range(n):
            for j in range(n):
                cols[i][j] = grid[j][i]
        
        # Compare each row with each column
        counts = 0
        for i in range(n):
            for j in range(n):
                found = True
                for k in range(n):
                    if rows[i][k] != cols[j][k]:
                        found = False
                        break
                if found:
                    counts += 1
        return counts
                