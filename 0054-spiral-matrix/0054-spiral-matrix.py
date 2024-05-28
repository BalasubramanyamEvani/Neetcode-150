class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        nr, nc = len(matrix), len(matrix[0])
        l, r, t, b = 0, nc, 0, nr
        ret = []
        while l < r and t < b:
            for i in range(l, r):
                ret.append(matrix[t][i])
            t += 1
            for i in range(t, b):
                ret.append(matrix[i][r - 1])
            r -= 1
            if l >= r or t >= b:
                break
            for i in range(r - 1, l - 1, -1):
                ret.append(matrix[b - 1][i])
            b -= 1
            for i in range(b - 1, t - 1, -1):
                ret.append(matrix[i][l])
            l += 1
        return ret
            