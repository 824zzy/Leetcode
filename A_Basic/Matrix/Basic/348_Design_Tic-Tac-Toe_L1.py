""" https://leetcode.com/problems/design-tic-tac-toe/
1. keep track of rows, cols, and diagonals count of each player
2. once a player has a count of n, return the player
"""
class TicTacToe:
    def __init__(self, n: int):
        self.n = n
        self.P = {
            1: [[0 for _ in range(n)] for _ in range(2)]+[[0, 0]],
            2: [[0 for _ in range(n)] for _ in range(2)]+[[0, 0]]
        }

    def move(self, r: int, c: int, p: int) -> int:
        R, C, D = self.P[p]
        R[r] += 1
        C[c] += 1
        if r==c: D[0] += 1
        if r+c==self.n-1: D[1] += 1
        
        if R[r]==self.n or C[c]==self.n or D[0]==self.n or D[1]==self.n:
            return p
        else:
            return 0
"""
["TicTacToe","move","move","move","move","move","move","move"]
[[3],[0,0,1],[0,2,2],[2,2,1],[1,1,2],[2,0,1],[1,0,2],[2,1,1]]
["TicTacToe","move","move","move"]
[[2],[0,0,2],[0,1,1],[1,1,2]]
"""