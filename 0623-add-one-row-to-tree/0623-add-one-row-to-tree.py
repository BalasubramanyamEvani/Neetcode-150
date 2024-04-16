# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        def dfs(node, d):
            if not node:
                return
            if depth == 1:
                return TreeNode(val, node, None)
            if d == depth - 1:
                node.left = TreeNode(val, node.left, None)
                node.right = TreeNode(val, None, node.right)
                return node
            node.left = dfs(node.left, d + 1)
            node.right = dfs(node.right, d + 1)
            return node
        return dfs(root, 1)
