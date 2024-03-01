# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        mem = {}
        q = deque()
        q.append((root, 0))
        maxlevel = 0
        while q:
            node, level = q.popleft()
            maxlevel = max(maxlevel, level)
            if level in mem:
                mem[level].append(node.val)
            else:
                mem[level] = [node.val]
            if node.right:
                q.append((node.right, level + 1))
            if node.left:
                q.append((node.left, level + 1))
        ret = []
        for i in range(maxlevel + 1):
            ret.append(mem[i][0])
        return ret
