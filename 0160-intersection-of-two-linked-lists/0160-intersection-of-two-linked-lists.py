# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        A = headA
        B = headB
        
        def llen(head):
            curr = head
            ret = 0
            while curr:
                ret += 1
                curr = curr.next
            return ret
        
        alen = llen(A)
        blen = llen(B)
        diff = abs(alen - blen)

        shorter, longer = A, B
        if alen > blen:
            shorter, longer = longer, shorter
        
        while diff > 0:
            longer = longer.next
            diff -= 1

        while longer and shorter:
            if longer == shorter:
                return longer
            longer = longer.next
            shorter = shorter.next
        
        return None