class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        N = len(nums)
        def dfs(i, cache):
            if i == N:
                return 1 if cache else 0
            ret = dfs(i + 1, cache)
            if not cache[nums[i] - k] and not cache[nums[i] + k]:
                cache[nums[i]] += 1
                ret += dfs(i + 1, cache)
                cache[nums[i]] -= 1
            return ret
        return dfs(0, defaultdict(int))
