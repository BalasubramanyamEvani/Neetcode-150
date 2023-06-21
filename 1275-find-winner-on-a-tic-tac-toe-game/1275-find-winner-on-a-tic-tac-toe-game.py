class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        nr = 3
        board = [["" * nr for j in range(nr)] for i in range(nr)]
        
        def checkrow(r):
            bazinga = True
            for i in range(1, nr):
                if board[r][i] != board[r][i - 1]:
                    bazinga = False
                    break
            return bazinga
        def checkcol(c):
            bazinga = True
            for i in range(1, nr):
                if board[i][c] != board[i - 1][c]:
                    bazinga = False
                    break
            return bazinga
        def checkdiag(primary=True):
            bazinga = True
            if primary:
                for i in range(1, nr):
                    if board[i][i] != board[i - 1][i - 1]:
                        bazinga = False
                        break
            else:
                for i in range(1, nr):
                    if board[i][nr - 1 - i] != board[i - 1][nr - i]:
                        bazinga = False
                        break
            return bazinga
        
        player = "A"
        for move in moves:
            r, c = move
            if player == "A":
                board[r][c] = "X"
            else:
                board[r][c] = "O"
            bazinga = False
            bazinga |= checkrow(r)
            bazinga |= checkcol(c)
            if r == c:
                bazinga |= checkdiag(primary=True)
            if r == nr - 1 - c:
                bazinga |= checkdiag(primary=False)
            
            if bazinga:
                return player
            
            if player == "A":
                player = "B"
            else:
                player = "A"
            
        return "Draw" if len(moves) == nr * nr else "Pending"
        