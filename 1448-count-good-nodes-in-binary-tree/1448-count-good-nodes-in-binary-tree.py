# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, currmax):
            if not node:
                return 0
            counts = 0
            if node.val >= currmax:
                counts += 1
            currmax = max(node.val, currmax)
            counts += dfs(node.left, currmax)
            counts += dfs(node.right, currmax)
            return counts
        return dfs(root, -math.inf)
