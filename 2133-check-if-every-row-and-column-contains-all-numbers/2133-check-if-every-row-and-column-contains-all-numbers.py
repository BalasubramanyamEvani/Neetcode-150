class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        n = len(matrix)
        
        for i in range(n):
            tmp = set()
            for j in range(n):
                tmp.add(matrix[i][j])
            if len(tmp) != n:
                return False
        
        for i in range(n):
            tmp = set()
            for j in range(n):
                tmp.add(matrix[j][i])
            if len(tmp) != n:
                return False
            
        return True
            