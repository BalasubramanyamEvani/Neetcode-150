class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        l, r = 0, 0
        N = len(nums)
        prod = 1
        count = 0
        # subarrays ending at position at r
        # see from reverse
        while r < N:
            prod = prod * nums[r]
            while prod >= k and l <= r:
                # if single element > product
                # l will become r + 1 after loop
                prod = prod // nums[l]
                l += 1
            # if the last element cannot be considered in the
            # subrray
            if l <= r:
                count += r - l + 1
            r += 1
        return count
