class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        def twoSum(i, val):
            left = 0
            right = len(nums) - 1
            pairs = []
            while left < right:
                if left == i:
                    left += 1
                if right == i:
                    right -= 1
                
                if left >= right:
                    break
                    
                if nums[left] + nums[right] == val:
                    pairs.append([left, right])
                    left += 1
                    right -= 1
                elif nums[left] + nums[right] < val:
                    left += 1
                elif nums[left] + nums[right] > val:
                    right -= 1
            return pairs

        triplets = []
        nums = sorted(nums)
        seen = set()
        for i in range(len(nums)):
            num1 = nums[i]
            if num1 in seen:
                continue
            seen.add(num1)
            pairs = twoSum(i, -num1)
            if len(pairs) > 0:
                for pair in pairs:
                    if num1 > nums[pair[1]]:
                        triplets.append((nums[pair[0]], nums[pair[1]], num1))
                    elif num1 > nums[pair[0]]:
                        triplets.append((nums[pair[0]], num1, nums[pair[1]]))
                    else:
                        triplets.append((num1, nums[pair[0]], nums[pair[1]]))
        
        triplets_set = set()
        for triplet in triplets:
            triplets_set.add(triplet)
        triplets = list(triplets_set)
        return triplets
        