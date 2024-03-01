# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ret = -math.inf
        def recursive(node):
            nonlocal ret
            if not node:
                return 0
            l = recursive(node.left)
            r = recursive(node.right)
            diameter = l + r
            ret = max(ret, diameter)
            return 1 + max(l, r)
        recursive(root)
        return ret
