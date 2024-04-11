class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:            
        ret = []
        N = len(candidates)
        # important things i noticed
        # 1. distinct numbers
        # 2. combination 2 2 3 can be written as
        # 2 3 2 or 3 3 2, but all are same, so its better
        # to just output the sorted order (indices) which
        # will be traversed while doing DFS
        def dfs(tmp, index, currsum):
            if currsum == target:
                ret.append(tmp[:])
                return
            if currsum > target:
                return
            for i in range(index, N):
                tmp.append(candidates[i])
                dfs(tmp, i, currsum + candidates[i])
                tmp.pop()
        
        dfs([], 0, 0)
        return ret
