class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        def calcMidSum(low, mid, high):
            maxlsum = -inf
            lsum = 0
            for i in range(mid, low - 1, -1):
                lsum += nums[i]
                maxlsum = max(lsum, maxlsum)
            
            maxrsum = -inf
            rsum = 0
            for i in range(mid + 1, high + 1):
                rsum += nums[i]
                maxrsum = max(rsum, maxrsum)
            
            return max(max(maxlsum, maxrsum), maxrsum + maxlsum)
                
        
        def dividefn(low, high):
            if low == high:
                return nums[low]
            mid = low + (high - low) // 2
            lsum = dividefn(low, mid)
            rsum = dividefn(mid + 1, high)
            midsum = calcMidSum(low, mid, high)
            
            return max(max(lsum, rsum), midsum)
        
        return dividefn(0, len(nums) - 1)