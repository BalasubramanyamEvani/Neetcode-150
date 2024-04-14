# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        def dfs(node, csum):
            if not node:
                return csum
            
            if node.left and not node.left.left and not node.left.right:
                csum += node.left.val
            
            csum = dfs(node.left, csum)
            csum = dfs(node.right, csum)
            return csum
        
        return dfs(root, 0)
        