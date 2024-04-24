# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getLonelyNodes(self, root: Optional[TreeNode]) -> List[int]:
        lonely_nodes = []
        def dfs(node):
            if not node:
                return False
            if not node.left and not node.right:
                return True
            f1 = dfs(node.left)
            f2 = dfs(node.right)
            if f1 and not f2:
                lonely_nodes.append(node.left.val)
            elif f2 and not f1:
                lonely_nodes.append(node.right.val)
            return f1 or f2
        
        dfs(root)
        return lonely_nodes
