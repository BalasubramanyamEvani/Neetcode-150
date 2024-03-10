# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def frequenciesOfElements(self, head: Optional[ListNode]) -> Optional[ListNode]:
        mem = {}
        dummy = ListNode(-1)
        curr = head
        currd = dummy
        while curr:
            mem[curr.val] = mem.get(curr.val, 0) + 1
            curr = curr.next
        for v in mem.values():
            currd.next = ListNode(v)
            currd = currd.next
        return dummy.next
