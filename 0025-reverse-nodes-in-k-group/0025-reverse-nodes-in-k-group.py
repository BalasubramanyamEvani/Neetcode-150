# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def reverse(l):
            if not l:
                return
            nonlocal maxiters
            if not maxiters:
                return l
            maxiters -= 1
            prev = None
            curr = l
            tmp = l
            count = k
            while curr and count > 0:
                nextnode = curr.next
                curr.next = prev
                prev = curr
                curr = nextnode
                count -= 1
            tmp.next = reverse(curr)
            return prev
        
        listlen = 0
        curr = head
        while curr:
            listlen += 1
            curr = curr.next
        maxiters = listlen // k
        return reverse(head)
