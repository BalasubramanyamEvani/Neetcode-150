# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        mid_node, prev_mid_node = self.getMid(head)
        prev_mid_node.next = None
        reversed_head = self.reverse(mid_node)
        while head and reversed_head:
            if head.val != reversed_head.val:
                return False
            head = head.next
            reversed_head = reversed_head.next
        return True
    
    def getMid(self, head):
        slow = head
        prev = head
        fast = head.next
        while slow and fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        if fast:
            return slow.next, slow
        return slow, prev
    
    def reverse(self, node):
        prev = None
        curr = node
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        return prev
    