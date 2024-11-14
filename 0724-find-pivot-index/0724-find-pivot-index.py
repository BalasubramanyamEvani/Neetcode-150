class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = 0
        for num in nums:
            total += num
        n = len(nums)
        rsum = 0
        pivot = -1
        for i in range(n - 1, -1, -1):
            rsum += nums[i + 1] if i + 1 <= n - 1 else 0
            lsum = total - rsum - nums[i]
            if rsum == lsum:
                pivot = i
        return pivot
