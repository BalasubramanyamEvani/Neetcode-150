# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def is_same(p, q):
            if not p and not q:
                return True
            if (p and not q) or (not p and q):
                return False
            if p.val != q.val:
                return False
            l = is_same(p.left, q.left)
            if not l:
                return False
            return is_same(p.right, q.right)
        
        def recursive(node):
            nonlocal subRoot
            if not node and subRoot:
                return False
            if not node and not subRoot:
                return True
            if node.val == subRoot.val and is_same(node, subRoot):
                return True
            return recursive(node.left) or recursive(node.right)
        
        return recursive(root)