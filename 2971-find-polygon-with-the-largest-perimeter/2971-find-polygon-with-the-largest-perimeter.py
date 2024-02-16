class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums = sorted(nums)
        N = len(nums)
        psum = [0 for _ in range(N)]
        psum[0] = 0
        for i in range(1, N):
            psum[i] = psum[i - 1] + nums[i - 1]
        for i in range(N - 1, 1, -1):
            if psum[i] > nums[i]:
                return psum[i] + nums[i]
        return -1
