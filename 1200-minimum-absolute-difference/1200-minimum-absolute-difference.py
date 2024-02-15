class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        N = len(arr)
        arr = sorted(arr)
        mindiff = math.inf
        for i in range(1, N):
            mindiff = min(arr[i] - arr[i - 1], mindiff)
        ret = []
        for i in range(1, N):
            if arr[i] - arr[i - 1] == mindiff:
                ret.append([arr[i - 1], arr[i]])
        return ret
