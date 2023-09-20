# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        # def traverse(node):
        #     if not node:
        #         return
        #     res.append(node.val)
        #     traverse(node.left)
        #     traverse(node.right)
        # traverse(root)
        # return res
        stack = deque()
        curr = root
        while curr != None or stack:
            while curr != None:
                stack.append(curr)
                res.append(curr.val)
                curr = curr.left
            
            curr = stack.pop()
            curr = curr.right
        
        return res
            