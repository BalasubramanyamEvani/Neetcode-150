# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        res = {}
        def traverse(node, level):
            if not node:
                return
            if level in res:
                res[level].append(node.val)
            else:
                res[level] = [node.val]
                
            traverse(node.left, level + 1)
            traverse(node.right, level + 1)
        
        traverse(root, 0)
        
#         q = deque([(root, 0)])
#         res = {}
#         while q:
#             node, level = q.popleft()
            
#             if level in res:
#                 res[level].append(node.val)
#             else:
#                 res[level] = [node.val]
            
#             if node.left:
#                 q.append((node.left, level + 1))
            
#             if node.right:
#                 q.append((node.right, level + 1))
        
        ret = []
        for k, v in res.items():
            ret.append(v)
        return ret
        