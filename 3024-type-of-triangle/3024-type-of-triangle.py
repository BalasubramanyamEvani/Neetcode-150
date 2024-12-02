class Solution:
    def triangleType(self, nums: List[int]) -> str:
        is_triag = nums[0] + nums[1] > nums[2] and nums[0] + nums[2] > nums[1] and nums[1] + nums[2] > nums[0]
        if not is_triag:
            return "none"
        if nums[0] == nums[1] and nums[0] == nums[2]:
            return "equilateral"
        if nums[0] != nums[1] and nums[0] != nums[2] and nums[1] != nums[2]:
            return "scalene"
        return "isosceles"
