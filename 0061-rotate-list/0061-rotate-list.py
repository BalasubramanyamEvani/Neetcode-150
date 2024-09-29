# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return
        listlen = 0
        curr = head
        while curr:
            listlen += 1
            curr = curr.next
        
        def reverse(l, count):
            curr = l
            prev = None
            while curr and count > 0:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp
                count -= 1
            return prev, curr
        
        k = k % listlen
        if not k:
            return head
        head, _ = reverse(head, listlen)
        tmp = head
        h1, c1 = reverse(head, k)
        h2, _ = reverse(c1, listlen - k)
        tmp.next = h2
        return h1
