class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []
        # below will not work for duplicate numbers
        curr = []
        ret = []
        for i, num in enumerate(nums):
            if not curr:
                curr.append(num)
            if i - 1 >= 0 and num != nums[i - 1] + 1:
                # when consecutive numbers are not observed
                # add this range
                # before adding end point
                # ensure its not same as start point
                if nums[i - 1] != curr[0]:
                    curr.append(nums[i - 1])
                ret.append(curr)
                curr = [num]
        # to handle range end in the end
        # if any curr is left to add
        if curr:
            ret.append(curr)
        # above statement ensures the start point
        # of range was added below ensures the
        # last point was also added because last range
        # should end with last num in the array
        if nums[-1] != ret[-1][-1]:
            curr.append(nums[-1])
        ret = [f"{l[0]}->{l[1]}" if len(l) == 2 else f"{l[0]}" for l in ret]
        return ret
