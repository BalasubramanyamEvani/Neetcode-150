# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        l3 = ListNode(-1)
        curr = l3
        while l1 or l2:
            num1 = l1.val if l1 else 0
            num2 = l2.val if l2 else 0
            sum_val = num1 + num2 + carry
            rem = sum_val % 10
            carry = sum_val // 10
            curr.next = ListNode(rem)
            curr = curr.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        if carry > 0:
            curr.next = ListNode(carry)
            carry = 0
        return l3.next
