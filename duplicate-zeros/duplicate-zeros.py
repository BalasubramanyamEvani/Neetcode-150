class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        N = len(arr)
        i = 0
        while i < N:
            if arr[i] == 0 and i < N - 1:
                for j in range(N - 2, i - 1, -1):
                    arr[j + 1] = arr[j]
                i += 2
            else:
                i += 1
