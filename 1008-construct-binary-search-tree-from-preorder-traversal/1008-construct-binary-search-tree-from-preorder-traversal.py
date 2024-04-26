# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        N = len(preorder)
        def dfs(i, low, high):
            if low > high:
                return None
            root = TreeNode(preorder[i])
            # find left and right subtrees
            i = low + 1
            while i <= high and root.val > preorder[i]:
                i += 1
            # left subtree
            root.left = dfs(low + 1, low + 1, i - 1)
            # right subtree
            root.right = dfs(i, i, high)
            return root
        
        # first arg is root positions
        return dfs(0, 0, N - 1)
