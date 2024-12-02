class Solution:
    def averageValue(self, nums: List[int]) -> int:
        avg = 0
        count = 0
        for num in nums:
            if num & 1 == 0 and num % 3 == 0:
                avg += num
                count += 1
        return avg // count if count else 0
