# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def is_identical(node1, node2):
            if (node1 and not node2) or (node2 and not node1):
                return False
            
            if not node1 and not node2:
                return True
            
            if node1.val != node2.val:
                return False
            
            return is_identical(node1.left, node2.left) and is_identical(node1.right, node2.right)

        
        def dfs(node):
            if not node:
                return
            
            if node.val == subRoot.val and is_identical(node, subRoot):
                return True
            
            return dfs(node.left) or dfs(node.right)
        
        return dfs(root)
        