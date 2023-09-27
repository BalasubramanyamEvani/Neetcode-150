class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        nr, nc = len(matrix), len(matrix[0])
        def swap(r1, c1, r2, c2):
            matrix[r1][c1], matrix[r2][c2] = matrix[r2][c2], matrix[r1][c1]
        
        def transpose():
            for i in range(nr):
                for j in range(i + 1, nc):
                    swap(i, j, j, i)
        
        def reverse_rows():
            for i in range(nr):
                for j in range(nc // 2):
                    swap(i, j, i, nc - 1 - j)
        
        transpose()
        reverse_rows()
            