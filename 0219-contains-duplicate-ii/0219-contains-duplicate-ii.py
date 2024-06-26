class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        ret = False
        seen = {}
        for i, num in enumerate(nums):
            if num in seen:
                if abs(i - seen[num]) <= k:
                    return True
            seen[num] = i
        return False
        