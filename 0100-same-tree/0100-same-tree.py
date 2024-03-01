# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def recursive(nodep, nodeq):
            if not nodep and not nodeq:
                return True
            if (nodep and not nodeq) or (not nodep and nodeq):
                return False
            if nodep.val != nodeq.val:
                return False
            l = recursive(nodep.left, nodeq.left)
            if not l:
                return False
            return recursive(nodep.right, nodeq.right)
        return recursive(p, q)
