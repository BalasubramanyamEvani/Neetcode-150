# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        list_size = self.listlen(head)
        diff = list_size - n
        dummy = ListNode(-1)
        dummy.next = head
        prev = None
        curr = head
        while diff != 0:
            prev = curr
            curr = curr.next
            diff -= 1
        if prev is not None:
            prev.next = curr.next
        if prev is None:
            return dummy.next.next
        curr.next = None
        return dummy.next
        
    def listlen(self, head):
        size = 0
        while head:
            size += 1
            head = head.next
        return size
        