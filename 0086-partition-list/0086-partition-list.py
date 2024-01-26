# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        A = head
        B = x
        before = ListNode(-1)
        after = ListNode(-1)
        d1s, d1e = before, None
        d2 = after
        curr = A
        while curr:
            if curr.val < B:
                before.next = ListNode(curr.val)
                before = before.next
                d1e = before
            else:
                after.next = ListNode(curr.val)
                after = after.next
            curr = curr.next
        if d1e:
            d1e.next = d2.next
            return d1s.next
        return d2.next
