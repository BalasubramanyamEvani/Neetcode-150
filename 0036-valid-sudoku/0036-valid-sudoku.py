class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowmem = {}
        colmem = {}
        blockmem = {}
        def addtomem(num, i, mem):
            if i in mem and num in mem[i]:
                return False
            if i in mem and num not in mem[i]:
                mem[i].add(num)
            else:
                mem[i] = set()
                mem[i].add(num)
            return True
        
        nr, nc = len(board), len(board[0])
        for i in range(nr):
            for j in range(nc):
                block_row = i // 3
                block_col = j // 3
                blocknum = block_row * 3 + block_col
                if board[i][j] != ".":
                    if not (addtomem(board[i][j], i, rowmem) and addtomem(board[i][j], j, colmem) and addtomem(board[i][j], blocknum, blockmem)):
                        return False
        return True
        