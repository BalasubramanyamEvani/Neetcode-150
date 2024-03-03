# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        list_size = self.listlen(head)
        diff = list_size - n
        if diff == 0:
            newhead = head.next
            head.next = None
            return newhead
        prevnode = None
        curr = head
        while diff != 0:
            prevnode = curr
            curr = curr.next
            diff -= 1
        prevnode.next = curr.next
        curr.next = None
        return head
        
    def listlen(self, head):
        size = 0
        while head:
            size += 1
            head = head.next
        return size
        