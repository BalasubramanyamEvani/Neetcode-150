# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        l3 = ListNode(-1)
        curr = l3
        while list1 and list2:
            if list1.val < list2.val:
                curr.next = ListNode(list1.val)
                list1 = list1.next
            else:
                curr.next = ListNode(list2.val)
                list2 = list2.next
            curr = curr.next
        while list1:
            curr.next = ListNode(list1.val)
            curr = curr.next
            list1 = list1.next
        while list2:
            curr.next = ListNode(list2.val)
            curr = curr.next
            list2 = list2.next
        return l3.next
