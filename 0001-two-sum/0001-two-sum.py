class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mem = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in mem:
                return mem[diff], i
            else:
                mem[num] = i
        return -1