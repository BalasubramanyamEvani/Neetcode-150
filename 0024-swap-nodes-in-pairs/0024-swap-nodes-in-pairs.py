# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverse(l):
            if not l:
                return
            prev = None
            curr = l
            tmp = l
            count = 2
            while curr and count > 0:
                nextnode = curr.next
                curr.next = prev
                prev = curr
                curr = nextnode
                count -= 1
            tmp.next = reverse(curr)
            return prev
        return reverse(head)