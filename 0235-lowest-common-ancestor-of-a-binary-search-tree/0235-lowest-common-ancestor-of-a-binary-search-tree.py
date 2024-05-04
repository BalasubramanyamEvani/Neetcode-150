# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def lca(node):
            nonlocal p, q
            if not node:
                return None
            if node.val == p or node.val == q:
                return node
            if p.val < node.val and q.val < node.val:
                return lca(node.left)
            elif p.val > node.val and q.val > node.val:
                return lca(node.right)
            return node
        return lca(root)
