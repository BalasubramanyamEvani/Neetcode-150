# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def dfs(node):
            if not node:
                return []
            if not node.left and not node.right:
                return [node.val]
            val1 = dfs(node.left)
            val2 = dfs(node.right)
            return [*val1, *val2]
        
        leaves_1 = dfs(root1)
        leaves_2 = dfs(root2)
        n1, n2 = len(leaves_1), len(leaves_2)
        if n1 != n2:
            return False
        for i in range(n1):
            if leaves_1[i] != leaves_2[i]:
                return False
        return True
