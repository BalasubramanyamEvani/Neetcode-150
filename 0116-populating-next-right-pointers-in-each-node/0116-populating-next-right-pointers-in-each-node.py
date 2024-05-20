"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return
        q = deque([(0, root)])
        cache = {}
        while q:
            level, node = q.popleft()
            if level not in cache:
                cache[level] = []
            if cache[level]:
                cache[level][-1].next = node
            cache[level].append(node)
            for child in [node.left, node.right]:
                if child:
                    q.append((level + 1, child))
        return root
