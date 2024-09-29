# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head
        listlen = 0
        curr = head
        while curr:
            listlen += 1
            curr = curr.next
        k = k % listlen
        if not k:
            return head
        idx = listlen - k
        prev = None
        curr = head
        while idx:
            prev = curr
            curr = curr.next
            idx -= 1
        prev.next = None
        newhead = curr
        while curr.next:
            curr = curr.next
        curr.next = head
        return newhead