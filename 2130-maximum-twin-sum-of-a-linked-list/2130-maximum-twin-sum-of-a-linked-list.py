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
        
        def copy(node):
            new_head = ListNode(-1)
            ret = new_head
            curr = node
            while curr:
                new_head.next = ListNode(curr.val)
                curr = curr.next
                new_head = new_head.next
            return ret.next
        
        new_head = copy(head)
        tail = reverse(head)
        
        maxval = -math.inf
        while new_head != tail:
            n1, n2 = new_head.val, tail.val
            maxval = max(maxval, n1 + n2)
            new_head = new_head.next
            tail = tail.next
        
        return maxval
