class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        A = weights
        B = days
        def shippingTime(w):
            days = 0
            c = 0
            for i, num in enumerate(A):
                c += num
                if c > w:
                    days += 1
                    c = num
            return (days + 1) <= B, days + 1
        
        low = max(A)
        high = sum(A)
        while low <= high:
            mid = low + (high - low) // 2
            t, _ = shippingTime(mid)
            if t:
                high = mid - 1
            else:
                low = mid + 1
        return low
