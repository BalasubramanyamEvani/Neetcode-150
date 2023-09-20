# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
#         def traverse(node):
#             if not node:
#                 return
#             traverse(node.left)
#             traverse(node.right)
#             res.append(node.val)
        
#         traverse(root)
        if not root:
            return res
        stack = deque([root])
        visited = set()
        while stack:
            curr = stack.pop()
            if curr not in visited:
                stack.append(curr)
                if curr.right:
                    stack.append(curr.right)
                visited.add(curr)
                if curr.left:
                    stack.append(curr.left)
            else:
                res.append(curr.val)
            
        return res
    