# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        res = {}
        q = deque([(root, 0)])
        while q:
            node, level = q.popleft()
            if level in res:
                if level % 2 != 0:
                    res[level].appendleft(node.val)
                else:
                    res[level].append(node.val)
            else:
                res[level] = deque([node.val])
            
            if node.left:
                q.append((node.left, level + 1))
            
            if node.right:
                q.append((node.right, level + 1))
            
        ret = []
        for k, v in res.items():
            ret.append(v)
        return ret
