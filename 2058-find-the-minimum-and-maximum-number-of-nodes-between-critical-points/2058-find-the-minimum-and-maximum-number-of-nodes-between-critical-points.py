# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        arr = []
        curr = head
        while curr:
            arr.append(curr.val)
            curr = curr.next
        N = len(arr)
        indices = []
        for i in range(1, N - 1):
            if arr[i] > arr[i - 1] and arr[i] > arr[i + 1]:
                indices.append(i)
            elif arr[i] < arr[i - 1] and arr[i] < arr[i + 1]:
                indices.append(i)
        n = len(indices)
        if n < 2:
            return -1, -1
        max_dist = indices[-1] - indices[0]
        min_dist = math.inf
        for i in range(1, n):
            min_dist = min(min_dist, indices[i] - indices[i - 1])
        return min_dist, max_dist
        