class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        def twoSum(i, val):
            left = i + 1
            right = len(nums) - 1
            pairs = []
            while left < right:
                if nums[left] + nums[right] == val:
                    triplets.append([nums[i], nums[left], nums[right]])
                    left += 1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1
                elif nums[left] + nums[right] < val:
                    left += 1
                elif nums[left] + nums[right] > val:
                    right -= 1
            return pairs

        triplets = []
        nums = sorted(nums)
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            num1 = nums[i]
            pairs = twoSum(i, -num1)
        
        return triplets
        