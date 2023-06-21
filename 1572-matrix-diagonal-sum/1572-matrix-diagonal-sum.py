class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        pdiag = 0
        sdiag = 0
        n = len(mat)
        for i in range(n):
            pdiag += mat[i][i]
        for i in range(n - 1, -1, -1):
            sdiag += mat[n - 1 - i][i]
        res = pdiag + sdiag
        if n % 2 != 0:
            res -= mat[n // 2][n // 2]
        return res
    