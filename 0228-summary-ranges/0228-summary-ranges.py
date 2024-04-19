class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []
        curr = []
        ret = []
        for i, num in enumerate(nums):
            if not curr:
                curr.append(num)
            if i - 1 >= 0 and num != nums[i - 1] + 1:
                if nums[i - 1] != curr[0]:
                    curr.append(nums[i - 1])
                ret.append(curr)
                curr = [num]
        if curr:
            ret.append(curr)
        if nums[-1] != ret[-1][-1]:
            curr.append(nums[-1])
        ret = [f"{l[0]}->{l[1]}" if len(l) == 2 else f"{l[0]}" for l in ret]
        return ret
