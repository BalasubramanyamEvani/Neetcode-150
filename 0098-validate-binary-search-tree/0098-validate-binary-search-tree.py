# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validate(root, min_limit, max_limit):
            if not root:
                return True
            
            if root.val <= min_limit or root.val >= max_limit:
                return False
            
            return validate(root.left, min_limit, root.val) and validate(root.right, root.val, max_limit)
        
        return validate(root, -math.inf, math.inf)