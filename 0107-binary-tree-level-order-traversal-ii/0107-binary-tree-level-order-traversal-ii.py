# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return
        q = deque([(0, root)])
        result, tmp = deque(), []
        prev = 0
        while q:
            level, node = q.popleft()
            for child in [node.left, node.right]:
                if child:
                    q.append((level + 1, child))
            if level != prev:
                prev = level
                result.appendleft(tmp)
                tmp = []
            tmp.append(node.val)
        if tmp:
            result.appendleft(tmp)
        return result
