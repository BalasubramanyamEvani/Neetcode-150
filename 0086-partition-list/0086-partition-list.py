# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        before = ListNode(-1)
        after = ListNode(-1)
        
        curr = head
        curr1, curr2 = before, after
        while curr:
            if curr.val < x:
                curr1.next = ListNode(curr.val)
                curr1 = curr1.next
            else:
                curr2.next = ListNode(curr.val)
                curr2 = curr2.next
            curr = curr.next
        
        # last elt of before list
        curr = before.next
        while curr and curr.next:
            curr = curr.next
        # connect before and after
        if curr:
            curr.next = after.next
            return before.next
        return after.next
