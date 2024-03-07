class Solution:
    def minArea(self, image: List[List[str]], x: int, y: int) -> int:
        nr, nc = len(image), len(image[0])
        visited = set()
        minr, maxr = math.inf, -math.inf
        minc, maxc = math.inf, -math.inf
        
        def recursive(r, c):
            if r < 0 or r >= nr or c < 0 or c >= nc:
                return
            if image[r][c] == "1" and (r, c) not in visited:
                visited.add((r, c))
                
                nonlocal minr, maxr, minc, maxc
                minr = min(minr, r)
                maxr = max(maxr, r)
                minc = min(minc, c)
                maxc = max(maxc, c)
                
                recursive(r - 1, c)
                recursive(r + 1, c)
                recursive(r, c + 1)
                recursive(r, c - 1)
        
        recursive(x, y)
        width = maxc - minc + 1
        height = maxr - minr + 1
        return width * height
                