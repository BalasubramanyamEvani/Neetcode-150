# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        count = 0
        def recursive(node):
            nonlocal count
            if not node:
                return
            if node.val >= low and node.val <= high:
                count += node.val
            if node.val <= high:
                recursive(node.right)   
            if node.val >= low:
                recursive(node.left)
        recursive(root)
        return count
