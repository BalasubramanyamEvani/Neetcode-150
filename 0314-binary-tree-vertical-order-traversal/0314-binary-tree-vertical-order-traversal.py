# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # if no root return empty array
        if not root:
            return []
        # while doing Bfs I will fill up a 2d matrix
        # for the final traversal
        
        # nr will store the number of rows in the matrix
        # minc, maxc will determine the number of columns required
        nr, minc, maxc = 0, 0, 0
        # normal BFS stuff
        q = deque()
        # each item while traversing will store the 
        # row and column information, root will start at 0, 0
        # first number is row, second is column
        q.append((0, 0, root))
        bfs = []
        while q:
            r, c, node = q.popleft()
            bfs.append((r, c, node.val))
            nr = max(nr, r)
            minc = min(minc, c)
            maxc = max(maxc, c)
            if node.left:
                # when we go left decrease column
                q.append((r + 1, c - 1, node.left))
            if node.right:
                # when we go right increas column
                q.append((r + 1, c + 1, node.right))
        # now calculate the range to get the final number of
        # columns
        nc = maxc - minc + 1
        # number of rows will be + 1
        nr = nr + 1
        # offset to negative column [-4, 4] -> [0, 8]
        col_offset = -minc 
        # build the matrix
        ret = [[None] * nc for _ in range(nr)]
        for item in bfs:
            r, c, val = item
            if not ret[r][c + col_offset]:
                ret[r][c + col_offset] = []
            ret[r][c + col_offset].append(val)
        # traverse the matrix column wise
        res = []
        for i in range(nc):
            tmp = []
            for j in range(nr):
                if ret[j][i]:
                    tmp.extend(ret[j][i])
            res.append(tmp)
        # return the result
        return res
