class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        nr, nc = len(image), len(image[0])
        visited = set()
        prev_color = image[sr][sc]
        
        def dfs(r, c):
            if r < 0 or r >= nr or c < 0 or c >= nc:
                return 
            if (r, c) not in visited and image[r][c] == prev_color:
                visited.add((r, c))
                image[r][c] = color
                dfs(r + 1, c)
                dfs(r - 1, c)
                dfs(r, c + 1)
                dfs(r, c - 1)
        
        dfs(sr, sc)
        return image
