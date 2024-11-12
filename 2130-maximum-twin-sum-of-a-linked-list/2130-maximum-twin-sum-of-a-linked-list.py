# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        def reverse(node):
            prev = None
            curr = node
            while curr:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp
            return prev
        
        slow, fast = head, head
        prev = None
        while slow and fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        
        tail = reverse(slow)
        prev.next = None
        
        maxval = -math.inf
        while head != tail:
            n1, n2 = head.val, tail.val
            maxval = max(maxval, n1 + n2)
            head = head.next
            tail = tail.next
        
        return maxval
