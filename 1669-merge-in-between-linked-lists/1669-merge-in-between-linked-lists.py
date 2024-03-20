# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        p1 = list1
        p2 = None
        curr = list1
        i = 0
        while curr:
            tmp = curr.next
            if i + 1 == a:
                curr.next = None
            if i == b + 1:
                p2 = curr
                break
            curr = tmp
            i += 1

        curr = p1
        while curr.next:
            curr = curr.next
        curr.next = list2
        curr = list2
        while curr.next:
            curr = curr.next
        curr.next = p2
        return p1
        