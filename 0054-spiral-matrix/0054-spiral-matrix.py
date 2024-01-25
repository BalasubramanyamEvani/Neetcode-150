class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        A = matrix
        r, c = len(A), len(A[0])
        res = []
        left, right = 0, c
        top, bottom = 0, r
        while left < right and top < bottom:
            # going right
            for i in range(left, right):
                res.append(A[top][i])
            top += 1

            # going top to bottom
            for i in range(top, bottom):
                res.append(A[i][right - 1])
            right -= 1

            if not (left < right and top < bottom):
                break

            # going right to left
            for i in range(right - 1, left - 1, -1):
                res.append(A[bottom - 1][i])
            bottom -= 1

            # going bottom to up
            for i in range(bottom - 1, top - 1, -1):
                res.append(A[i][left])
            left += 1
        return res
