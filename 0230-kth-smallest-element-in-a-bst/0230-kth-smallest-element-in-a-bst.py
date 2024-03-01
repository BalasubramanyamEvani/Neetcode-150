# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        ret = []
        def recursive(node):
            nonlocal ret
            if not node:
                return
            recursive(node.left)
            ret.append(node.val)
            recursive(node.right)
        recursive(root)
        return ret[k - 1]
