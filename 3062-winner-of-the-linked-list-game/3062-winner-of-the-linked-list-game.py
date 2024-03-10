# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def gameResult(self, head: Optional[ListNode]) -> str:
        odd = 0
        even = 0
        curr = head
        while curr:
            evennum = curr.val
            oddnum = curr.next.val
            if oddnum > evennum:
                odd += 1
            elif evennum > oddnum:
                even += 1
            curr = curr.next.next
        if odd == even:
            return "Tie"
        return "Odd" if odd > even else "Even"
