class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:            
        ret = []
        N = len(candidates)
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
