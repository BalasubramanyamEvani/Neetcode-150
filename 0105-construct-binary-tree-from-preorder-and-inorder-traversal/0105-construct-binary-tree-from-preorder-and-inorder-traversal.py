# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def dfs(preorder, inorder):
            if not preorder:
                return
            subroot_val = preorder[0]
            subroot = TreeNode(subroot_val)
            i = 0
            while i < len(inorder) and inorder[i] != subroot_val:
                i += 1
            # num_elements_in_left_subtree = i
            # left subtree
            subroot.left = dfs(preorder[1:i + 1], inorder[:i])
            # right subtree
            subroot.right = dfs(preorder[i + 1:], inorder[i + 1:])
            return subroot
        
        return dfs(preorder, inorder)
