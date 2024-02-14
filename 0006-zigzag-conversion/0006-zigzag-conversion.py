class Solution:
    def convert(self, s: str, numRows: int) -> str:
        N = len(s)
        matrix = [[] for _ in range(numRows)]
        i = 0
        j = -1
        flag = False
        while i < N:
            if not flag:
                j = min(numRows - 1, j + 1)
                matrix[j].append(s[i])
            else:
                j = max(0, j - 1)
                matrix[j].append(s[i])
            if (not flag and j == numRows - 1) or (flag and j == 0):
                flag = not flag
            i += 1
        ret = ["".join(arr) for arr in matrix]
        return "".join(ret)
