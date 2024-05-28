class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        cache = {}
        currmax = -math.inf
        for i, num in enumerate(nums):
            if num in cache:
                cache[num]["right"] = i
                cache[num]["val"] += 1
            else:
                cache[num] = {
                    "left": i,
                    "right": i,
                    "val": 1
                }
            currmax = max(currmax, cache[num]["val"])
        ret = math.inf
        for k, v in cache.items():
            if v["val"] == currmax:
                ret = min(ret, v["right"] - v["left"] + 1)
        return ret
