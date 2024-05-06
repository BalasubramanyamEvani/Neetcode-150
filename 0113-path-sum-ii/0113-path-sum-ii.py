# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        
        ret = []
        if not root:
            return ret
        
        def dfs(node, tmp, currsum):
            currsum += node.val
            tmp.append(node.val)
            if currsum == targetSum and not node.left and not node.right:
                ret.append(tmp[:])
            for child in [node.left, node.right]:
                if child:
                    dfs(child, tmp, currsum)
                    tmp.pop()
        
        dfs(root, [], 0)
        return ret
