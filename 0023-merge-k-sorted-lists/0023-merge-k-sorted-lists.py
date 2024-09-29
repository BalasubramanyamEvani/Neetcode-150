# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        def merge(l1, l2):
            c1, c2 = l1, l2
            ret = ListNode(-1)
            c3 = ret
            while c1 and c2:
                if c1.val < c2.val:
                    c3.next = ListNode(c1.val)
                    c1 = c1.next
                    c3 = c3.next
                else:
                    c3.next = ListNode(c2.val)
                    c2 = c2.next
                    c3 = c3.next
            while c1:
                c3.next = ListNode(c1.val)
                c1 = c1.next
                c3 = c3.next
            while c2:
                c3.next = ListNode(c2.val)
                c2 = c2.next
                c3 = c3.next
            return ret.next
        
        step = 1
        N = len(lists)
        while step < N:
            for i in range(0, N - step, step * 2):
                lists[i] =  merge(lists[i], lists[i + step])
            step *= 2
        
        return lists[0] if lists else None
        