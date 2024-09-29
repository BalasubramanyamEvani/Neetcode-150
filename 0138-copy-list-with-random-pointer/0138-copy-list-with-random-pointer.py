"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return
        # interleave
        curr = head
        while curr:
            tmp = curr.next
            curr.next = Node(curr.val)
            curr.next.next = tmp
            curr = tmp
        # copy random pointers
        curr = head
        while curr:
            curr.next.random = curr.random.next if curr.random else None
            curr = curr.next.next
        original, copy = head, head.next
        ret = head.next
        while original:
            original.next = original.next.next
            copy.next = copy.next.next if copy.next else None
            copy = copy.next
            original = original.next
        return ret