class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        r, c = len(matrix), len(matrix[0])
        def shuntrow(i):
            for k in range(c):
                matrix[i][k] = 0
        
        def shuntcol(i):
            for k in range(r):
                matrix[k][i] = 0
                
        rset, cset = set(), set()
        for i in range(r):
            for j in range(c):
                if matrix[i][j] == 0:
                    rset.add(i)
                    cset.add(j)
        
        for i in rset:
            shuntrow(i)
        
        for i in cset:
            shuntcol(i)
            
            
        