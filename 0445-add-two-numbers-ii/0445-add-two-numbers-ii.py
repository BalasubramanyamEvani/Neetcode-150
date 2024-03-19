# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def reverse(node):
            prev = None
            curr = node
            while curr:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp
            return prev
            
        l1 = reverse(l1)
        l2 = reverse(l2)
        dummy = ListNode(-1)
        c1, c2, c3 = l1, l2, dummy
        carry = 0
        while c1 or c2:
            tmp = 0
            if c1:
                tmp += c1.val
                c1 = c1.next
            if c2:
                tmp += c2.val
                c2 = c2.next
            tmp += carry
            rem = tmp % 10
            carry = tmp // 10
            c3.next = ListNode(rem)
            c3 = c3.next
        if carry > 0:
            c3.next = ListNode(carry)
        return reverse(dummy.next)
