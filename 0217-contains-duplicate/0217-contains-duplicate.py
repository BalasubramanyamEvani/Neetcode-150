class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        arr_set = set()
        for num in nums:
            if num in arr_set:
                return True
            arr_set.add(num)
        return False
