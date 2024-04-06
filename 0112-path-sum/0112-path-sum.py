# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(node, currsum):
            if not node:
                return False
            if not node.left and not node.right:
                currsum = currsum + node.val
                return currsum == targetSum
            return dfs(node.left, currsum + node.val) or dfs(node.right, currsum + node.val)
        
        return dfs(root, 0) if root else False
