class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        nr, nc = len(image), len(image[0])
        visited = set()
        prev_color = image[sr][sc]
        
        def dfs(r, c, count):
            if r < 0 or r >= nr or c < 0 or c >= nc:
                return count
            if (r, c) not in visited and image[r][c] == prev_color:
                visited.add((r, c))
                count += 1
                image[r][c] = color
                count = dfs(r + 1, c, count)
                count = dfs(r - 1, c, count)
                count = dfs(r, c + 1, count)
                count = dfs(r, c - 1, count)
            return count
        
        count = dfs(sr, sc, 0)
        print(count)
        return image
