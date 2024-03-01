# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def recursive(curr, itr):
            if itr == 0:
                return curr
            prev = None
            nonlocal k
            count = k
            tmp = curr
            while count > 0 and curr:
                nextnode = curr.next
                curr.next = prev
                prev = curr
                curr = nextnode
                count -= 1
            tmp.next = recursive(curr, itr - 1)
            return prev
        tmp = head
        listlen = 0
        while tmp:
            listlen += 1
            tmp = tmp.next
        itr = listlen // k
        h = recursive(head, itr)
        return h
