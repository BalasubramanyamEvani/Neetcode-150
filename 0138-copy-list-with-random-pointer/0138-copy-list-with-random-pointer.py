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
        mem1, mem2, mem3 = {}, {}, {}
        curr = head
        i = 0
        while curr:
            mem1[curr] = i
            i += 1
            curr = curr.next
        curr = head
        while curr:
            mem2[mem1[curr]] = mem1[curr.random] if curr.random else -1
            curr = curr.next
        dummy = Node(-1)
        curr1 = dummy
        curr2 = head
        while curr2:
            curr1.next = Node(curr2.val, None, None)
            curr1 = curr1.next
            curr2 = curr2.next
        curr = dummy.next
        if not curr:
            return None
        i = 0
        while curr:
            mem3[i] = curr
            curr = curr.next
            i += 1
        curr = dummy.next
        i = 0
        while curr:
            curr.random = mem3[mem2[i]] if mem2[i] >= 0 else None
            curr = curr.next
            i += 1
        return dummy.next
