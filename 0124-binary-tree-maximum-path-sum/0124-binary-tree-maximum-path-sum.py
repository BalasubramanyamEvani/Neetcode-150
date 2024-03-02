# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        ret = -math.inf
        def recursive(node):
            if not node:
                return 0
            l = recursive(node.left)
            r = recursive(node.right)
            nodemax = max([node.val, node.val + l, node.val + r]) 
            nonlocal ret
            ret = max(ret, max(nodemax, node.val + l + r))
            return nodemax
        recursive(root)
        return ret
        