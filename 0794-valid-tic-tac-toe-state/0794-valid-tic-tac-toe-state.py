class Solution:
    def validTicTacToe(self, board: List[str]) -> bool:
        mem = {
            "O": 0,
            "X": 0
        }
        
        board_str = "".join(board)
        winspace = board + ["".join([board[i][i] for i in range(3)])] + ["".join(board[2 - i][i] for i in range(2, -1, -1))]
        
        for i in range(3):
            tmp = []
            for j in range(3):
                tmp.append(board[j][i])
            winspace.append("".join(tmp))
        
        for ch in board_str:
            if ch != " ":
                mem[ch] = mem.get(ch, 0) + 1
        if mem["O"] + mem["X"] == 1 and mem["O"] == 1:
            return False
        xwin = "XXX"
        owin = "OOO"
        if xwin in winspace and owin in winspace:
            return False
        diff = mem["X"] - mem["O"]
        if xwin in winspace:
            return mem["X"] - mem["O"] == 1
        if owin in winspace:
            return mem["X"] - mem["O"] == 0
        if diff >= 0 and diff <= 1:
            return True
        return False
