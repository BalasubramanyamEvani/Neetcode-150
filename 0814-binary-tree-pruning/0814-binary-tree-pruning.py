# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def recursive(node):
            if not node:
                return 0
            v1 = recursive(node.left)
            if not v1:
                node.left = None
            v2 = recursive(node.right)
            if not v2:
                node.right = None
            return v1 or v2 or node.val == 1
        val = recursive(root)
        return root if val else None
