class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        nr, nc = len(mat), len(mat[0])
        def valid(r, c):
            return 0 <= r < nr and 0 <= c < nc
        
        ret = defaultdict(deque)
        q = deque()
        q.append((0, 0, 0))
        visited = set()
        visited.add((0, 0))
        while q:
            level, r, c = q.popleft()
            if level % 2 == 0:
                ret[level].appendleft(mat[r][c])
            else:
                ret[level].append(mat[r][c])
            
            if (r, c + 1) not in visited and valid(r, c + 1):
                visited.add((r, c + 1))
                q.append((level + 1, r, c + 1))
            
            if (r + 1, c) not in visited and valid(r + 1, c):
                visited.add((r + 1, c))
                q.append((level + 1, r + 1, c))
        
        res = []
        for i in range(len(ret)):
            res.extend(ret[i])
        return res
