class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A = nums1
        B = nums2
        
        N = len(A) + len(B)
        if len(B) < len(A):
            A, B = B, A
        half = N // 2
        low = 0
        high = len(A) - 1 # A here is the smallest length array
        flag = True if N % 2 == 0 else False
        while True:
            i = low + (high - low) // 2
            j = half - i - 2 # half - (i + 1) - 1 [0 based indexing]
            A_left = A[i] if i >= 0 else -math.inf
            A_right = A[i + 1] if i + 1 < len(A) else math.inf
            B_left = B[j] if j >= 0 else -math.inf
            B_right = B[j + 1] if j + 1 < len(B) else math.inf
            # correct partition
            if A_left <= B_right and B_left <= A_right:
                if flag:
                    return (max(A_left, B_left) + min(A_right, B_right)) / 2
                return min(B_right, A_right)
            if A_left > B_right:
                high = i - 1
            else:
                low = i + 1
