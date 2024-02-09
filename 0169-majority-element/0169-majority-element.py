class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        N = len(nums)
        n = N // 2 + N % 2
        mem = {}
        for num in nums:
            mem[num] = mem.get(num, 0) + 1
            if mem[num] == n:
                return num
        return -1
