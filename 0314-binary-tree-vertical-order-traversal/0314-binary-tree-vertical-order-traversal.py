# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        nr, minc, maxc = 0, 0, 0
        q = deque()
        q.append((0, 0, root))
        bfs = []
        while q:
            r, c, node = q.popleft()
            bfs.append((r, c, node.val))
            nr = max(nr, r)
            minc = min(minc, c)
            maxc = max(maxc, c)
            if node.left:
                q.append((r + 1, c - 1, node.left))
            if node.right:
                q.append((r + 1, c + 1, node.right))
        
        nc = maxc - minc + 1
        nr = nr + 1
        col_offset = -minc 
        ret = [[None] * nc for _ in range(nr)]
        for item in bfs:
            r, c, val = item
            if not ret[r][c + col_offset]:
                ret[r][c + col_offset] = []
            ret[r][c + col_offset].append(val)

        res = []
        for i in range(nc):
            tmp = []
            for j in range(nr):
                if ret[j][i]:
                    tmp.extend(ret[j][i])
            res.append(tmp)
        return res

            