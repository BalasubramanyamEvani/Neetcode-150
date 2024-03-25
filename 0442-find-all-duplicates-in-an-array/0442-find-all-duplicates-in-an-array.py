class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for num in nums:
            index = abs(num) - 1
            nums[index] = -nums[index]
        ret = []
        for num in nums:
            index = abs(num) - 1
            if nums[index] > 0:
                ret.append(abs(num))
                nums[index] = -nums[index]
        return ret
