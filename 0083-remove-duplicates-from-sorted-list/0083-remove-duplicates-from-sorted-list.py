# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        prev = None
        while curr:
            if not prev:
                prev = curr
            elif prev.val != curr.val:
                prev.next = curr
                prev = curr
            curr = curr.next
        if prev:
            prev.next = None
        return head
                