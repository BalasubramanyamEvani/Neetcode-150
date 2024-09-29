# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        prev = None
        found = False
        while curr:
            if curr.next and curr.val == curr.next.val:
                currval = curr.val
                while curr.next and curr.next.val == currval:
                    curr = curr.next
                if prev:
                    prev.next = curr.next
            else:
                found = True
                if not prev:
                    head = curr
                prev = curr
            curr = curr.next
        return head if found else None