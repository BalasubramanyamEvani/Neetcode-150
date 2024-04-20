class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        nr, nc = len(mat), len(mat[0])
        total_elements = nr * nc
        if total_elements != r * c or (r == nr and c == nc):
            return mat
        new_mat = [[0] * c for _ in range(r)]
        for i in range(total_elements):
            new_col = i % c
            prev_col = i % nc
            new_row = i // c
            prev_row = i // nc
            new_mat[new_row][new_col] = mat[prev_row][prev_col]
        return new_mat
