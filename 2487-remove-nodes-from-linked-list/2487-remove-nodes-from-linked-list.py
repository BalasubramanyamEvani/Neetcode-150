# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverse(node):
            prev = None
            curr = node
            while curr:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp
            return prev
            
        if not head:
            return
        
        head = reverse(head)
        curr = head
        prev = None
        currmax = -math.inf
        while curr:
            if curr.val >= currmax:
                currmax = curr.val
                prev = curr
            elif prev:
                prev.next = curr.next
            curr = curr.next
        return reverse(head)
