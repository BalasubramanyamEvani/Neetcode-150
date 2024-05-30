class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        min_so_far = nums[0]
        max_so_far = nums[0]
        result = nums[0]
        for num in nums[1:]:
            tmp = max_so_far
            max_so_far = max(min_so_far * num, max_so_far * num, num)
            min_so_far = min(tmp * num, min_so_far * num, num)
            result = max(max_so_far, result)
        return result
