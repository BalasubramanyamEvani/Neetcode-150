class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        N = len(nums)
        def binarySearchFirstOccurrence():
            nonlocal N
            low = 0
            high = N - 1
            res = -1
            while low <= high:
                mid = low + (high - low) // 2
                if nums[mid] < target:
                    low = mid + 1
                elif nums[mid] > target:
                    high = mid - 1
                else:
                    res = mid
                    if mid - 1 >= 0 and nums[mid - 1] == nums[mid]:
                        high = mid - 1
                    else:
                        break
            return res
        
        def binarySearchLastOccurrence():
            nonlocal N
            res = -1
            low = 0
            high = N - 1
            while low <= high:
                mid = low + (high - low) // 2
                if nums[mid] < target:
                    low = mid + 1
                elif nums[mid] > target:
                    high = mid - 1
                else:
                    res = mid
                    if mid + 1 < N and nums[mid + 1] == nums[mid]:
                        low = mid + 1
                    else:
                        break
            return res

        in1 = binarySearchFirstOccurrence()
        in2 = binarySearchLastOccurrence()
        return [in1, in2]
