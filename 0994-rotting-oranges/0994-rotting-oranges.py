class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        visited = set()
        q = deque()
        fresh = 0
        nr, nc = len(grid), len(grid[0])
        # multi source BFS from here
        for i in range(nr):
            for j in range(nc):
                if grid[i][j] == 2:
                    visited.add((i, j))
                    q.append((i, j))
                elif grid[i][j] == 1:
                    fresh += 1
        
        if fresh == 0:
            return 0
        
        # add function while doing BFS
        def add(r, c):
            nonlocal fresh
            if r >= 0 and r < nr and c >= 0 and c < nc and grid[r][c] == 1 and (r, c) not in visited:
                q.append((r, c))
                visited.add((r, c))
                fresh -= 1

        minutes = -1
        while q:
            batchlen = len(q)
            for _ in range(batchlen):
                r, c = q.popleft()
                add(r + 1, c)
                add(r - 1, c)
                add(r, c + 1)
                add(r, c - 1)
            minutes += 1
        return minutes if fresh == 0 else -1
