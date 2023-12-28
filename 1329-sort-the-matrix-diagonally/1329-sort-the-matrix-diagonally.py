import heapq

class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        nr, nc = len(mat), len(mat[0])
        diagonals = {}
        for i in range(nr):
            for j in range(nc):
                if i - j not in diagonals:
                    diagonals[i - j] = []
                heapq.heappush(diagonals[i - j], mat[i][j])

        newmat = [[0 for _ in range(nc)] for _ in range(nr)]
        for i in range(nr):
            for j in range(nc):
                newmat[i][j] = heapq.heappop(diagonals[i - j])

        return newmat
        