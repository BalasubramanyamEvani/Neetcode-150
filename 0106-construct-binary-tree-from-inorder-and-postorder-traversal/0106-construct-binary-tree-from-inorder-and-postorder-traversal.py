# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        def dfs(inorder, postorder):
            if not inorder:
                return
            subroot_val = postorder[-1]
            subroot = TreeNode(subroot_val)
            i = 0
            while i < len(inorder) and inorder[i] != subroot_val:
                i += 1
            # num elements in left subtree = i
            # left subtree
            subroot.left = dfs(inorder[:i], postorder[:i])
            # right subtree
            subroot.right = dfs(inorder[i + 1:], postorder[i:len(inorder) - 1])
            
            return subroot
            
        return dfs(inorder, postorder) 