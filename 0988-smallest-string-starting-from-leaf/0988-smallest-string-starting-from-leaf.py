# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        # pass string since immutable
        # hence copy by value if using list of deque
        # it will be copy by reference and cause issues
        # by going back up to root
        def dfs(node, tmp):
            if not node:
                return ""
            currstring = chr(ord("a") + node.val) + tmp
            if not node.left and not node.right:
                return currstring
            l = dfs(node.left, currstring)
            r = dfs(node.right, currstring)
            if l == "":
                return r
            if r == "":
                return l
            return l if l < r else r
        
        return dfs(root, "")
        