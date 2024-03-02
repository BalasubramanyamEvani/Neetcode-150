# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def build(preord, inord):
            if not preord:
                return
            root = TreeNode(preord[0])
            inord_index = inord.index(root.val)
            
            root.left = build(preord[1: inord_index + 1], inord[:inord_index])
            root.right = build(preord[inord_index + 1:], inord[inord_index + 1:])
            return root
        return build(preorder, inorder)
