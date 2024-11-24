class Solution:
    def candyCrush(self, board: List[List[int]]) -> List[List[int]]:
        self.board = board
        self.nr, self.nc = len(board), len(board[0])
        while True:
            marked = self.mark()
            if not marked:
                break
            self.crush(marked)
            self.gravity()
        return board
    
    def mark(self):
        marked = set()
        for i in range(self.nr):
            for j in range(self.nc - 2):
                if self.board[i][j] == self.board[i][j + 1] == self.board[i][j + 2] != 0:
                    marked.update([(i, j), (i, j + 1), (i, j + 2)])

            for i in range(self.nr - 2):
                for j in range(self.nc):
                    if self.board[i][j] == self.board[i + 1][j] == self.board[i + 2][j] != 0:
                        marked.update([(i, j), (i + 1, j), (i + 2, j)])

        return marked
    
    def crush(self, marked):
        for r, c in marked:
            self.board[r][c] = 0
    
    def gravity(self):
        for c in range(self.nc):
            tmp = []
            for r in range(self.nr):
                if self.board[r][c] != 0:
                    tmp.append(self.board[r][c])
                    self.board[r][c] = 0
            ptr = len(tmp)
            i = 0
            for r in range(self.nr - ptr, self.nr):
                self.board[r][c] = tmp[i]
                i += 1
