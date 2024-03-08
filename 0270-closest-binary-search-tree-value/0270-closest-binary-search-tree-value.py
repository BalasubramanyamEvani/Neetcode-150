# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        closestval = root.val
        currmin = math.inf
        def recursive(node):
            if not node:
                return
            nonlocal closestval, currmin
            diff = node.val - target
            if abs(diff) < currmin or (abs(diff) == currmin and node.val < closestval):
                closestval = node.val
                currmin = abs(diff)
            if diff > 0:
                recursive(node.left)
            elif diff < 0:
                recursive(node.right)
            
        recursive(root)
        return closestval
