class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ret = []
        candidates.sort()
        N = len(candidates)
        def dfs(index, tmp, currsum):
            if currsum == target:
                ret.append(tmp[:])
                return
            if currsum > target:
                return
            for i in range(index + 1, N):
                if i - 1 >= 0 and candidates[i] == candidates[i - 1] and i - 1 != index:
                    continue
                tmp.append(candidates[i])
                dfs(i, tmp, currsum + candidates[i])
                tmp.pop()
        dfs(-1, [], 0)
        return ret
