class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        A = nums
        low = 0
        high = len(A) - 1
        while low <= high:
            mid = low + (high - low) // 2
            midl = A[mid - 1] if mid - 1 >= 0 else -float("infinity")
            midr = A[mid + 1] if mid + 1 < len(A) else -float("infinity")
            if A[mid] >= midl and A[mid] >= midr:
                return mid
            if A[mid] < midl:
                high = mid - 1
            else:
                low = mid + 1
        return -1
