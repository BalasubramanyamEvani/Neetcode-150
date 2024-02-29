# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        def middlePoint(node):
            fast = node.next
            slow = node
            while slow and fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            ret = slow.next
            if ret:
                slow.next.prev = None
                slow.next = None
            return ret
            
        def reverse(node):
            prev = None
            curr = node
            while curr:
                nextnode = curr.next
                curr.next = prev
                prev = curr
                curr = nextnode
            return prev
        
        h1, h2 = head, middlePoint(head)
        h2 = reverse(h2)
        while h1 and h2:
            n1, n2 = h1.next, h2.next
            h1.next = h2
            h2.next = n1
            h1, h2 = n1, n2
