# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def dfs(node, csum):
            if not node:
                return 0
            csum = csum * 10 + node.val
            if not node.left and not node.right:
                return csum
            l = dfs(node.left, csum)
            r = dfs(node.right, csum)
            return l + r
        
        return dfs(root, 0)
            