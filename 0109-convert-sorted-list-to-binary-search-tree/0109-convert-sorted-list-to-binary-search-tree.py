# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        def middle(l):
            slow = l
            fast = l
            prev = None
            while slow and fast and fast.next:
                prev = slow
                slow = slow.next
                fast = fast.next.next
            if prev:
                prev.next = None
            return slow
        
        def divide(h):
            if not h:
                return
            # find middle
            mid = middle(h)
            # creae new root
            root = TreeNode(mid.val)
            # left and right subtree
            left = h if h != mid else None
            right = mid.next
            # divide
            root.left = divide(left)
            root.right = divide(right)
            return root
        
        return divide(head)
            