# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def recursive(node, currmin, currmax):
            if not node:
                return True
            if not (node.val > currmin and node.val < currmax):
                return False
            return recursive(node.left, currmin, node.val) and recursive(node.right, node.val, currmax)
        return recursive(root, -math.inf, math.inf)