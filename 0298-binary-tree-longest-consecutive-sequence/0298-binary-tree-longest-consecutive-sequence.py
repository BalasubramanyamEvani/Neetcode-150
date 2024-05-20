# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        def dfs(curr, parent, length):
            if not curr:
                return length
            length = length + 1 if parent and curr.val == parent.val + 1 else 1
            l = dfs(curr.left, curr, length)
            r = dfs(curr.right, curr, length)
            return max(length, max(l, r))
        
        return dfs(root, None, 0)
