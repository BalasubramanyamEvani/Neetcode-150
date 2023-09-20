# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
#         def traverse_recursive(node):
#             if not node:
#                 return
#             traverse_recursive(node.left)
#             res.append(node.val)
#             traverse_recursive(node.right)
        
        stack = deque()
        curr = root
        while curr != None or stack:
            while curr != None:
                stack.append(curr)
                curr = curr.left
            
            curr = stack.pop()
            res.append(curr.val)
            curr = curr.right 
            
        return res
