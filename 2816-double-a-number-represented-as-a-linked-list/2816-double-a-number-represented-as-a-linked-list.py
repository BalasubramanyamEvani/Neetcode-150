# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverse(node):
            prev = None
            curr = node
            while curr:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp
            return prev
        
        head = reverse(head)
        multiplier = 2
        curr = head
        carry = 0
        prev = None
        while curr:
            num = curr.val * 2 + carry
            curr.val = num % 10
            carry = num // 10
            prev = curr
            curr = curr.next
        if carry:
            prev.next = ListNode(carry)
        return reverse(head)
        