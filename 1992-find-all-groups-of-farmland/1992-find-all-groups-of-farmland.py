class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        nr, nc = len(land), len(land[0])
        groups = []
        
        visited = defaultdict(bool)
        def dfs(r, c, group):
            if r < 0 or r >= nr or c < 0 or c >= nc:
                return
            if not visited[(r, c)] and land[r][c] == 1:
                visited[(r, c)] = True
                group[0], group[1] = min(group[0], r), min(group[1], c)
                group[2], group[3] = max(group[2], r), max(group[3], c)
                dfs(r + 1, c, group)
                dfs(r - 1, c, group)
                dfs(r, c + 1, group)
                dfs(r, c - 1, group)
        
        for r in range(nr):
            for c in range(nc):
                if not visited[(r, c)] and land[r][c] == 1:
                    group = [r, c, r, c]
                    dfs(r, c, group)
                    groups.append(group)
        
        return groups
