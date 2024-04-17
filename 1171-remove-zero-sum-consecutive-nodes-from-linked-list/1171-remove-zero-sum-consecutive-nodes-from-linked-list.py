# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1)
        dummy.next = head
        curr1 = dummy.next
        currsum = 0
        # handle scenario like [0]
        mem = {
            0: dummy
        }
        # algorithm is to see when the prefix sum
        # occurs again. because the nodes in between the
        # repeating prefix Sums did equal amount of +x, -x
        while curr1:
            currsum += curr1.val
            if currsum in mem:
                # delete in between nodes
                h1 = mem[currsum].next
                tmp = currsum
                while h1 != curr1:
                    tmp += h1.val
                    del mem[tmp]
                    h1 = h1.next
                # join the prev node to next node
                mem[currsum].next = curr1.next
            else:
                mem[currsum] = curr1
            curr1 = curr1.next
        return dummy.next
