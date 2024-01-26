class Solution:
    def mySqrt(self, x: int) -> int:
        A = x
        low = 0
        high = max(A // 2, 1)
        while low <= high:
            mid = low + (high - low) // 2
            r = mid**2
            if r == A:
                return mid
            if r > A:
                high = mid - 1
            else:
                low = mid + 1
        return low - 1
