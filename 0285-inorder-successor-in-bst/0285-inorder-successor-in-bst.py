# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:
        def getRightMin(node):
            curr = node
            while curr.left:
                curr = curr.left
            return curr
        
        ancestorMax = None
        def findNode(node):
            nonlocal ancestorMax
            if not node:
                return None
            if node.val == p.val:
                return p
            if node.val < p.val:
                return findNode(node.right)
            ancestorMax = node
            return findNode(node.left)

        n = findNode(root)
        if n.right:
            return getRightMin(n.right)
        return ancestorMax

            