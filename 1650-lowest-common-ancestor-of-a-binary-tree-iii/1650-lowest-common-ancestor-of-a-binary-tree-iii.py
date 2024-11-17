"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        trace = set()
        node = p
        # store trace from node p to root
        while node:
            trace.add(node)
            node = node.parent
        node = q
        # then trace node q to root
        # and get the LCA
        while node:
            if node in trace:
                return node
            node = node.parent
        return None
