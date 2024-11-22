class Solution:
    def countAlternatingSubarrays(self, nums: List[int]) -> int:
        N = len(nums)
        if N == 1:
            return 1
        l, r = 0, 1
        counts = 0
        while r <= N - 1:
            if nums[r] == nums[r - 1]:
                n = r - l
                counts += n * (n + 1) // 2
                l = r
            r += 1
        n = r - l
        counts +=  n * (n + 1) // 2
        return counts
