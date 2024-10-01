# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        def reverse(l, count):
            prev = None
            curr = l
            tmp = l
            while curr and count > 0:
                nextnode = curr.next
                curr.next = prev
                prev = curr
                curr = nextnode
                count -= 1
            if prev:
                return prev, l, curr
            return l, l, curr
        l = left - 1
        prev = None
        curr = head
        while curr and l > 0:
            prev = curr
            curr = curr.next
            l -= 1
        newhead, oldhead, rem = reverse(curr, right - left + 1)
        oldhead.next = rem
        if prev:
            prev.next = newhead
            return head
        return newhead
