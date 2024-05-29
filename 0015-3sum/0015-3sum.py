class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        N = len(nums)
        def twoSum(left, n):
            right = N - 1
            while left < right:
                if nums[left] + nums[right] > n:
                    right -= 1
                elif nums[left] + nums[right] < n:
                    left += 1
                else:
                    ret.append([-n, nums[left], nums[right]])
                    left += 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
        ret = []
        nums = sorted(nums)
        for i, num in enumerate(nums):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            twoSum(i + 1, -num)
        return ret
