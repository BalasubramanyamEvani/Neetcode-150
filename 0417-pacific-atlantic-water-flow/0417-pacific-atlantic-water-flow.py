class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        nr, nc = len(heights), len(heights[0])
        reached_pacific = set()
        reached_atlantic = set()
        # DFS
        def dfs(r, c, visited, prev):
            if r < 0 or r >= nr or c < 0 or c >= nc:
                return
            if heights[r][c] >= prev and (r, c) not in visited:
                visited.add((r, c))
                dfs(r + 1, c, visited, heights[r][c])
                dfs(r - 1, c, visited, heights[r][c])
                dfs(r, c + 1, visited, heights[r][c])
                dfs(r, c - 1, visited, heights[r][c])
        # DFS from left and right
        for i in range(0, nr):
            dfs(i, 0, reached_pacific, -math.inf)
            dfs(i, nc -1, reached_atlantic, -math.inf)
        # DFS from top and bottom
        for i in range(0, nc):
            dfs(0, i, reached_pacific, -math.inf)
            dfs(nr - 1, i, reached_atlantic, -math.inf)
        # reached atlantic intersection reached pacific
        # i.e. reached both
        return reached_atlantic.intersection(reached_pacific)
