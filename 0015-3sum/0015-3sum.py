class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        def twoSum(i, val):
            left = i + 1
            right = len(nums) - 1
            pairs = []
            while left < right:
                if nums[left] + nums[right] == val:
                    pairs.append([left, right])
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
            if len(pairs) > 0:
                for pair in pairs:
                    if num1 > nums[pair[1]]:
                        triplets.append((nums[pair[0]], nums[pair[1]], num1))
                    elif num1 > nums[pair[0]]:
                        triplets.append((nums[pair[0]], num1, nums[pair[1]]))
                    else:
                        triplets.append((num1, nums[pair[0]], nums[pair[1]]))
        
        return triplets
        